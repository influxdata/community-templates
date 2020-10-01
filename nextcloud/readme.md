# MySQL / MariaDB Dashboard for InfluxDB v2

Provided by: Ignacio Van Droogenbroeck

This Dashboard offers you information about your Nextcloud instance. CPU Load, Storage, Users, Sharing files stats and more.

![Dashboard Screenshot](screenshot.png)

### Quick Install

#### InfluxDB UI

In the InfluxDB UI, go to Settings->Templates and enter this URL: https://raw.githubusercontent.com/influxdata/community-templates/master/nextcloud/nextcloud.yml

#### Influx CLI
If you have your InfluxDB credentials [configured in the CLI](https://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/nextcloud/nextcloud.yml
```

## Included Resources

  - 1 Telegraf Configuration: 'nextcloud'
  - 1 Dashboards: 'nextcloud'
  - 1 Label: 'nextcloud'
  - 1 Bucket: 'nextcloud'

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.

Telegraf Configuration requires the following environment variables
  - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your operator token to get started.
  - `INFLUX_ORG` - The name of your Organization.
  - `INFLUX_HOST` - The address of you InfluxDB

In order to use this Dashboard, you need to pass as variable the information about your user and password and Nextcloud server.

ex: ```$ export NEXTCLOUD-URL=https://user:password@your-server.com```

## Contact

Author: Ignacio Van Droogenbroeck

Email: ignacio[at]vandroogenbroeck[dot]net

Github and Gitlab user: @xe-nvdk

Influx Slack: Ignacio Van Droogenbroeck
