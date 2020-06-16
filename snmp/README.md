# SNMP Monitoring Template

Provided by: [bonitoo.io](.)

** This template provides several dashboards showing metrics provided via SNMP protoicol. It provides both example of generict SNMP metrics and examples from Microtik and Cisco devices.

### Dashboard examples

![Screenshot](img/snmp-dashboard.png)

### Quick Install

If you have your InfluxDB credentials [configured in the CLI](Vhttps://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx pkg -u https://raw.githubusercontent.com/influxdata/community-templates/master/{your_template_dir}/{your_template_file}
```

## Included Resources

This template includes the following:

    - 1 Bucket: `snmp`, 1d retention
    - 3 Labels: `inputs.net`,`inputs.system`,`SNMP`
    - 3 Telegraf Configurations
    - 0 Checks: 
    - 3 Dashboards: `SNMP System Monitoring`, `SNMP Cisco Monitoring`, `SNMP Mikrotik Monitoring`
    - 2 Variables: `snmp_host`, and `snmp_idName`

## Setup Instructions

Set up and install Telegraf `inputs.snmp` plugin into your Telegraf configmap.

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