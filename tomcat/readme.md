# Tomcat Dashboard for InfluxDB v2

Provided by: Ignacio Van Droogenbroeck

This Dashboard offers you information about your Apache Tomcat instance. Current Threads, Processing Time, Traffic, Request Count and more.

![Dashboard Screenshot](screenshot.png)

## Included Resources

    - 1 Telegraf Configuration
    - 1 Dashboards: apache_tomcat.json

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.
    
    Telegraf Configuration requires the following environment variables
    - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your master token to get started.
    - `INFLUX_ORG` - The name of your Organization.

    In orden to use this Dashboard, you need to specify the address to the Apache Tomcat instance /manager/status/all?XML=true instance, also, you need to provide username and password in Telegraf Configuration. Please. Don't use "root", use a user with read only permissions. 

## Contact

Author: Ignacio Van Droogenbroeck

Email: ignacio[at]vandroogenbroeck[dot]net

Github and Gitlab user: @xe-nvdk 

Influx Slack: Ignacio Van Droogenbroeck