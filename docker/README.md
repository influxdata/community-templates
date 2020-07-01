## Docker Monitoring Template

This InfluxDB Template can be used to monitor Docker.

![Docker Dashboard Screenshot](img/docker_dashboard.png)

### Quick Install

If you have your InfluxDB credentials [configured in the CLI](Vhttps://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/docker/docker.yml
```

### Included Resources

- 1 Bucket: `docker`, 7d retention
- Labels: Telegraf Plugin Labels
- 1 Telegraf Configuration
- 1 Dashboard: `Docker`
- 1 Variable: `bucket`
- 4 Alerts: Container cpu, mem, disk, non-zero exit
- 1 Notification Endpoint: Http Post
- 1 Notification Rules: Crit Alert

## Setup Instructions

  General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.
    
  The data for the dashboard is populated by the included Telegraf configuration which includes the Docker Input. You may need to customize the input configuration, specific the `endpoint` value, depending on how you are running Docker. More information can be found in the [Telegraf Docker Input documentation](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/docker).
  
  The Telegraf Configuration requires the following environment variables:
    
  - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your master token to get started.
  - `INFLUX_ORG` - The name of your Organization (this will be your email address on the InfluxDB Cloud free tier)
  - `INFLUX_HOST` - The URL of your InfluxDB host (this can your localhost, a remote instance, or InfluxDB Cloud)

  You **MUST** set these environment variables before running Telegraf using something similar to the following commands
    
  - This can be found on the `Load Data` > `Tokens` page in your browser: `export INFLUX_TOKEN=TOKEN`
  - Your Organization name can be found on the Settings page in your browser: `export INFLUX_ORG=my_org`

## Running Telegraf

  To get resource data from your Docker hosts, [download and install Telegraf](https://portal.influxdata.com/downloads/) on those hosts. InfluxData provides native packages for a number of distributions as well as binaries that can be executed directly.

  Start Telegraf using the instructions from the `Load Data` > `Telegraf` > `Setup Instructions` link in the UI.

## Customizations

You can customize it based on your Docker installation. More information can be found in the [Telegraf Docker Input documentation](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/docker).

## Contact

- Author: Russ Savage
- Email: russ@influxdata.com
- Github: [@russorat](https://github.com/russorat)
- Influx Slack: [@russ](https://influxdata.com/slack)