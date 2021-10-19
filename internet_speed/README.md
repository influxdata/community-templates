# Internet Speed Monitoring Template

Provided by: Samantha Wang

Collect and monitor your internet data speeds. 


![Internet Speed Monitoring Dashboard Screenshot](https://github.com/sjwang90/community-templates/blob/internet-speed/internet_speed/internet-speed-dashboard.png)

### Quick Install

#### InfluxDB UI

In the InfluxDB UI, go to Settings->Templates and enter this URL: https://raw.githubusercontent.com/influxdata/community-templates/master/internet_speed/internet-speed.yml

#### Influx CLI
If you have your InfluxDB credentials [configured in the CLI](https://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/internet_speed/internet-speed.yml
```

## Included Resources

List what resources your template provides in this section. That will allow users to know at a glance what comes with it.

**Example:**

  - 1 Bucket: `internet`
  - 1 Label: `internet-speed`
  - 1 Telegraf Configuration: `Internet`
  - 1 Dashboards: `Internet Speed`
  - 1 Variables: `bucket`

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.

Describe any steps needed to finish setting up and running your template, including how to launch your Telegraf configurations and connect to any external services or data sources.

**Example:**
    
Telegraf Configuration requires the following environment variables
  - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your operator token to get started.
  - `INFLUX_ORG` - The name of your Organization
  - `INFLUX_HOST` - The address of your InfluxDB instance

You **MUST** set these environment variables before running Telegraf using something similar to the following commands
  - This can be found on the `Load Data` > `Tokens` page in your browser: `export INFLUX_TOKEN=TOKEN`
  - Your Organization name can be found on the Settings page in your browser: `export INFLUX_ORG=my_org`


## Contact

Provide a way for users to get in touch with you if they have questions or need help using your template. What information you give is up to you, but we encourage providing those below.

Author: Samantha Wang

Email: swang@influxdata.com

Github: @sjwang90

Influx Slack: @Samantha Wang
