/** InfluxDB URL */
const INFLUX_URL = process.env.INFLUX_URL || 'http://localhost:8086'
/** InfluxDB authorization token */
const INFLUX_TOKEN = process.env.INFLUX_TOKEN || 'my-token'
/** Organization within InfluxDB  */
const INFLUX_ORG = process.env.INFLUX_ORG || 'my-org'
/** InfluxDB bucket  */
const INFLUX_BUCKET = 'iot_center'

// Defaults when on boarding a fresh new InfluxDB instance
/** InfluxDB user  */
const onboarding_username = 'my-user'
/** InfluxDB password  */
const onboarding_password = 'my-password'

/** recommended interval for client's to refresh configuration in seconds */
const configuration_refresh = 3600

function logEnvironment() {
  console.log(`INFLUX_URL=${INFLUX_URL}`)
  console.log(`INFLUX_TOKEN=${INFLUX_TOKEN ? '***' : ''}`)
  console.log(`INFLUX_ORG=${INFLUX_ORG}`)
  console.log(`INFLUX_BUCKET=${INFLUX_BUCKET}`)
}

module.exports = {
  INFLUX_URL,
  INFLUX_TOKEN,
  INFLUX_ORG,
  onboarding_username,
  onboarding_password,
  configuration_refresh,
  INFLUX_BUCKET,
  logEnvironment,
}
