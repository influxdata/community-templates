# Reachability Trivial Client

This InfluxDB template will poll a specific address/port services and report success or failure along with simple timing results.

> Visuals help users know what to expect, and get them excited to try your template. Include a screenshot of a dashboard or something else something your template provides.

![Example Dashboard Screenshot](Example_Screenshot.png)

## Included Resources

- 1 Bucket: `networkservices`, 30d retention
- X Labels: 
- X Flux task for collection
- X Checks for failed access or open access
- X Dashboards: `Access Available`, `Authentication On/Off`
- X Variables: `bucket`, `influxdb_host`, `url`, `user`, `password`

## Setup Instructions

Describe any steps needed to finish setting up and running your template, including how to launch your Telegraf configurations and connect to any external services or data sources.

**Example:**
    
    Telegraf Configuration requires the following environment variables
    - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your master token to get started.
    - `INFLUX_ORG` - The name of your Organization

    You **MUST** set these environment variables before running Telegraf using something similar to the following commands
    - This can be found on the `Load Data` > `Tokens` page in your browser: `export INFLUX_TOKEN=TOKEN`
    - Your Organization name can be found on the Settings page in your browser: `export INFLUX_ORG=my_org`

## Customizations

Show off the flexibility of your template by letting users know different ways they can use it other than the defaults you provide.

**Example:**

    You can easily update the Telegraf configurations to point to a specific InfluxDB 1.x location by setting the options in the [InfluxDB Input](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/influxdb) or the [InfluxDB 2.0 Output](https://github.com/influxdata/telegraf/tree/master/plugins/outputs/influxdb_v2). 

## Contact

- Author: Darin Fisher
- Email: dfisher@influxdata.com
- Github: @darinfisher
- Influx Slack: @dfisher

