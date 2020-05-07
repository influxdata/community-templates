# Github Dashboard for InfluxDB v2

Provided by: Ignacio Van Droogenbroeck

This dashboard help you get metrics of your Github repository. 

![Dashboard Screenshot](screenshot.png)

## Included Resources

    - 1 Telegraf Configuration
    - 1 Dashboards: github.json

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.
    
    Telegraf Configuration requires the following environment variables
    - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your master token to get started.
    - `INFLUX_ORG` - The name of your Organization.

In order to use this dashboard, you need to get a Token Access Key from Github. You can generate one from this page: https://github.com/settings/tokens and export as variable.

Ex: <code>export GITHUB_ACCESS_TOKEN="your-token"</code>

Also, you need to specify your Github's repos in telegraf.conf.

Ex: <code>repositories = ["influxdata/telegraf", "influxdata/influxdb"]</code>

## Contact

Author: Ignacio Van Droogenbroeck

Email: ignacio[at]vandroogenbroeck[dot]net

Github and Gitlab user: @xe-nvdk 

Influx Slack: Ignacio Van Droogenbroeck