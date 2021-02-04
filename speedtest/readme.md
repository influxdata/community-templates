# Speedtest template for InfluxDB v2.0

Provided by: Ignacio Van Droogenbroeck

This template offers you a view of the speed of your Internet connection.

You can view the Ping, Jitter, Download and Upload, current, and historical data. 

This template was updated on 01/11/2020. 

![Dashboard Screenshot](screenshot.png)

### Quick Install

#### InfluxDB UI

In the InfluxDB UI, go to Settings->Templates and enter this URL: https://raw.githubusercontent.com/influxdata/community-templates/master/speedtest/speedtest.yml

#### Influx CLI
If you have your InfluxDB credentials [configured in the CLI](https://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/speedtest/speedtest.yml
```

## Included Resources

  - 1 Telegraf Configuration: 'speedtest-config'
  - 1 Dashboards: 'speedtest'
  - 1 Label: 'speedtest'
  - 1 Bucket: 'speedtest'

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.

Telegraf Configuration requires the following environment variables
  - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `speedtest` bucket. You can just use your operator token to get started.
  - `INFLUX_ORG` - The name of your Organization.
  - `INFLUX_HOST` - The address of you InfluxDB

In order to use this template, you must install speedtest. Don't use the package of the repos, install according to [these instructions](https://www.speedtest.net/apps/cli).

## Contact

Author: Ignacio Van Droogenbroeck

Email: ignacio[at]vandroogenbroeck[dot]net

Github and Gitlab user: @xe-nvdk

Influx Slack: Ignacio Van Droogenbroeck
