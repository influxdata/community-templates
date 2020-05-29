# MySQL / MariaDB Dashboard for InfluxDB v2

Provided by: Ignacio Van Droogenbroeck

This Dashboard offers you information about your MySQL/MariaDB instance. Uptime, Current Queries. Active Threads, Connections, Locks, Traffic and more.

![Dashboard Screenshot](screenshot.png)

### Quick Install

If you have your `INFLUX_HOST`, `INFLUX_ORG` and `INFLUX_TOKEN` environment variables setup, you can install this template with:

```
influx pkg -u https://raw.githubusercontent.com/influxdata/community-templates/master/mysql_mariadb/mysql_mariadb.yml
```

## Included Resources

    - 1 Telegraf Configuration: 'mysql-mariadb'
    - 1 Dashboards: 'MySQL - MariaDB'
    - 1 Label: 'mysql'
    - 1 Bucket: 'mariadb'

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.
    
    Telegraf Configuration requires the following environment variables
    - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your master token to get started.
    - `INFLUX_ORG` - The name of your Organization.
    - `INFLUX_HOST` - The address of you InfluxDB
    - `INFLUX_BUCKET` - The name of the Bucket. If you going to use the bucket included, you need to export the variable. Ex: <code>export INFLUX_BUCKET=mariadb</code>

In order to use this Dashboard, you need to specify the connection string to the mySQL/MariaDB instance as variable. The same needs to define user and password (read only recommended)

ex: <code>$ export $MYSQL_CONNECTION_STRING=user@tcp(127.0.0.1:3306)/?tls=false</code>

## Contact

Author: Ignacio Van Droogenbroeck

Email: ignacio[at]vandroogenbroeck[dot]net

Github and Gitlab user: @xe-nvdk 

Influx Slack: Ignacio Van Droogenbroeck
