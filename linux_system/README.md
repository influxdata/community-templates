## Linux System Monitoring Template

This InfluxDB Template can be used to monitor your Linux System.

### Included Resources

- 1 Bucket: `telegraf`, 7d retention
- Labels: `Linux System Template` + Telegraf Plugin Labels
- 1 Telegraf Configuration
  - Required environment variables
    - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your master token to get started.
    - `INFLUX_ORG` - The name of your Organization
  - You **MUST** set these environment variables before running Telegraf using something similar to the following commands
    - This can be found on the `Load Data` > `Tokens` page in your browser: `export INFLUX_TOKEN=TOKEN`
    - Your Organization name can be found on the Settings page in your browser: `export INFLUX_ORG=my_org`
- 1 Dashboard: `Linux System`
- 2 Variables: `bucket` and `linux_host`