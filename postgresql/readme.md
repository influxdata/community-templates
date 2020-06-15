# Postgres Template for InfluxDB v2

Provided by: Ignacio Van Droogenbroeck

This Dashboard offers you information about your Postgres instance. CPU Usage, RAM Usage, Deadlocks, Fetch, Update, Return Data and more.

![Dashboard Screenshot](screenshot.png)

### Quick Install

If you have your InfluxDB credentials [configured in the CLI](Vhttps://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx pkg -u https://raw.githubusercontent.com/influxdata/community-templates/master/postgresql/postgres.yml
```

## Included Resources

    - 1 Telegraf Configuration: 'postgres-config
    - 1 Dashboards: 'Postgres'
    - 1 Label: 'postgres'
    - 1 Bucket: 'postgres'

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.
    
    Telegraf Configuration requires the following environment variables
    - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your master token to get started.
    - `INFLUX_ORG` - The name of your Organization.
    - `INFLUX_HOST` - The address of you InfluxDB
    - `INFLUX_BUCKET` - The name of the Bucket. If you going to use the bucket included, you need to export the variable. Ex: <code>export INFLUX_BUCKET=postgres</code>

In order to use this Dashboard, you need to specify the connection string to the Postgres instance as variable. The same needs to define user and password (read only recommended)

ex: <code>$ export PSQL_STRING_CONNECTIONG=postgres://postgres:mysecretpassword@localhost:5432</code>

## Contact

Author: Ignacio Van Droogenbroeck

Email: ignacio[at]vandroogenbroeck[dot]net

Github and Gitlab user: @xe-nvdk 

Influx Slack: Ignacio Van Droogenbroeck
