const {InfluxDB, Point} = require('@influxdata/influxdb-client')
const {
  INFLUX_URL: url,
  INFLUX_TOKEN: token,
  INFLUX_ORG: org,
  INFLUX_BUCKET: bucket,
} = require('./env')
const responseTime = require('response-time')

// create Influx Write API to report application monitoring data
const writeAPI = new InfluxDB({url, token}).getWriteApi(org, bucket, 'ns', {
  defaultTags: {
    service: 'iot_center',
    host: require('os').hostname(),
  },
})
// write node resource/cpu/memory usage
function writeProcessUsage() {
  function createPoint(measurement, usage) {
    const point = new Point(measurement)
    for (const key of Object.keys(usage)) {
      point.floatField(key, usage[key])
    }
    return point
  }

  // https://nodejs.org/api/process.html#process_process_memoryusage
  writeAPI.writePoint(createPoint('node_memory_usage', process.memoryUsage()))
  // https://nodejs.org/api/process.html#process_process_cpuusage_previousvalue
  writeAPI.writePoint(createPoint('node_cpu_usage', process.cpuUsage()))
  // https://nodejs.org/api/process.html#process_process_resourceusage

  // available since node v12.6
  if (process.resourceUsage) {
    writeAPI.writePoint(
      createPoint('node_resource_usage', process.resourceUsage())
    )
  }
}
// write process usage now and then every 10 seconds
writeProcessUsage()
const nodeUsageTimer = setInterval(writeProcessUsage, 10000).unref()

// on shutdown
// - clear reporting of node usage
// - flush unwritten points and cancel retries
async function onShutdown() {
  clearInterval(nodeUsageTimer)
  try {
    await writeAPI.close()
  } catch (error) {
    console.error('ERROR: Application monitoring', error)
  }
  // eslint-disable-next-line no-process-exit
  process.exit(0)
}
process.on('SIGINT', onShutdown)
process.on('SIGTERM', onShutdown)

// export a monitoring function for express.js response time monitoring
module.exports = function (app) {
  app.use(
    responseTime((req, res, time) => {
      // print out request basics
      console.info(
        `${req.method} ${req.path} ${res.statusCode} ${
          Math.round(time * 100) / 100
        }ms`
      )
      // write response time to InfluxDB
      const point = new Point('express_http_server')
        .tag('uri', req.path)
        .tag('method', req.method)
        .tag('status', String(res.statusCode))
        .floatField('response_time', time)
      writeAPI.writePoint(point)
    })
  )
}
