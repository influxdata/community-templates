# ZooKeeper Dashboard for InfluxDB v2

Provided by: Ignacio Van Droogenbroeck

This Dashboard offers you information about your ZooKeeper. Almost all of the metrics can be exploted are in this dashboard. https://github.com/influxdata/telegraf/tree/master/plugins/inputs/zookeeper

![Dashboard Screenshot](screenshot.png)

## Included Resources

    - 1 Telegraf Configuration
    - 1 Dashboards: zookeeper.json

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.
    
    Telegraf Configuration requires the following environment variables
    - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your master token to get started.
    - `INFLUX_ORG` - The name of your Organization.

    In orden to use this Dashboard, you need to specify the address to the ZooKeeper client (EX: https://localhost:2181).

## Contact

Author: Ignacio Van Droogenbroeck

Email: ignacio[at]vandroogenbroeck[dot]net

Github and Gitlab user: @xe-nvdk 

Influx Slack: Ignacio Van Droogenbroeck