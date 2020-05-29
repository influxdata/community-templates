# Template Name

Provided by: Your Name

Provide a short description of your template and use case here. Try to keep it to just a few sentences, there's room for more detail in the sections below.


> Visuals help users know what to expect, and get them excited to try your template. Include a screenshot of a dashboard or something else something your template provides.

![Example Dashboard Screenshot](Example_Screenshot.png)

### Quick Install

If you have your `INFLUX_HOST`, `INFLUX_ORG` and `INFLUX_TOKEN` environment variables setup, you can install this template with:

```
influx pkg -u https://raw.githubusercontent.com/influxdata/community-templates/master/{your_template_dir}/{your_template_file}
```

## Included Resources

List what resources your template provides in this section. That will allow users to know at a glance what comes with it.

**Example:**

    - 1 Bucket: `Telegraf`, 7d retention
    - 3 Labels: `InfluxDB1.x`,`Solution`,`Telegraf`
    - 1 Telegraf Configuration
    - 3 Checks: `Disk Usage Check`, `Host Deadman`, and `Memory Usage Check`
    - 2 Dashboards: `InfluxDB 1.x` and `Telegraf`
    - 3 Variables: `bucket`, `influxdb_host`, and `telegraf_host`

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.

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

Provide a way for users to get in touch with you if they have questions or need help using your template. What information you give is up to you, but we encourage providing those below.

Author: Your Name

Email: you@yourmail.com

Github: @your_username

Influx Slack: @your_username