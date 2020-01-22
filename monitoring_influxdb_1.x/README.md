## InfluxDB 1.x Open Source Monitoring Template

This InfluxDB Template can be used to monitor your already running InfluxDB 1.x instance. It provides a quick way to get started on InfluxDB 2.0 if you are an existing InfluxDB user.

### Included Resources

- 1 Bucket: `Telegraf`, 7d retention
- 3 Labels: `InfluxDB1.x`,`Solution`,`Telegraf`
- 1 Telegraf Configuration
  - Required environment variables
    - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your master token to get started.
    - `INFLUX_ORG` - The name of your Organization
  - You **MUST** set these environment variables before running Telegraf using something similar to the following commands
    - This can be found on the `Load Data` > `Tokens` page in your browser: `export INFLUX_TOKEN=TOKEN`
    - Your Organization name can be found on the Settings page in your browser: `export INFLUX_ORG=my_org`
- 3 Checks: `Disk Usage Check`, `Host Deadman`, and `Memory Usage Check`
- 2 Dashboards: `InfluxDB 1.x` and `Telegraf`
- 3 Variables: `bucket`, `influxdb_host`, and `telegraf_host`

## Customizations
You can easily update the Telegraf configurations to point to a specific InfluxDB 1.x location by setting the options in the [InfluxDB Input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/influxdb) or the [InfluxDB 2.0 Output](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/influxdb_v2). 