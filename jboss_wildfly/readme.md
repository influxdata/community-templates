# jBoss-Wildfly template for InfluxDB v2

Provided by: Ignacio Van Droogenbroeck

This Dashboard offers you information about your jBoss-Wildfly instance. Uptime, CPU Usage, Heap Memory, Non Heap Memory, Memory Pool Collections, Networking and Disk IO.

![Dashboard Screenshot](screenshot.png)

### Quick Install

If you have your InfluxDB credentials [configured in the CLI](Vhttps://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/jboss_wildfly/jboss_wildfly.yml
```

## Included Resources

    - 1 Telegraf Configuration: 'jboss-wildfly-config'
    - 1 Dashboards: 'jboss-wildfly'
    - 1 Label: 'jboss-wildfly'
    - 1 Bucket: 'jboss-wildfly'

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.
    
    Telegraf Configuration requires the following environment variables
    - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your master token to get started.
    - `INFLUX_ORG` - The name of your Organization.
    - `INFLUX_HOST` - The address of you InfluxDB
    - `INFLUX_BUCKET` - The name of the Bucket. If you going to use the bucket included, you need to export the variable. Ex: <code>export INFLUX_BUCKET=jboss-wildfly</code>

In order to use this Dashboard, you need to specify the connection string to connect to the jBoss Wildfly / Jolokia instance as variable.

ex: <code>$ export $JBOSS_CONNECTION_STRING=http://localhost:8080/jolokia</code>

## Contact

Author: Ignacio Van Droogenbroeck

Email: ignacio[at]vandroogenbroeck[dot]net

Github and Gitlab user: @xe-nvdk 

Influx Slack: Ignacio Van Droogenbroeck
