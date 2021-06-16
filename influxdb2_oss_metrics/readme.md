# InfluxDB Open Source (OSS) Metrics Template

Provided by: InfluxData

This InfluxDB Template can be used to monitor one or many InfluxDB OSS instances using the included Telegraf configuration. This template is designed to send your InfluxDB OSS monitoring information to your InfluxDB Cloud account.

![InfluxDB 2 Dashboard Screenshot](img/influxdb2-dashboard.png)

### Quick Install

See the [InfluxDB Documentation](link TBD) for detailed instructions for using this template to monitor your InfluxDB Open Source instances.

#### InfluxDB UI
In the InfluxDB UI, go to Settings->Templates and enter this URL: https://raw.githubusercontent.com/influxdata/community-templates/master/influxdb2_oss_metrics/influxdb2_oss_metrics.yml

#### Influx CLI
If you have your InfluxDB credentials [configured in the CLI](https://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can also install this template with:

```
influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/influxdb2_oss_metrics/influxdb2_oss_metrics.yml
```

## Included Resources

- 1 Bucket: `oss_metrics`, 7d retention
- 2 Labels: `InfluxDB2`,`prometheus`
- 1 Dashboard: `InfluxDB OSS Metrics`
- 1 Telegraf Config: `Scrape InfluxDB OSS Metrics`
- 1 Check: `InfluxDB OSS Deadman`

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.

The data for the dashboard is populated by the included Telegraf configuration. Using the Telegraf configuration allows you to use this template in your InfluxDB Cloud account to monitor your open source instances. The best way to set this up is to first follow the instructions for installing any template. That will create the labels, bucket, dashboard and Telegraf config for you.
  
When installing this into your InfluxDB Cloud account, you would want to install a Telegraf agent on each host where InfluxDB OSS is running and start it with the included config. You will need to configure the following ENV variables for your Telegraf config to run:
    
- INFLUX_URL: This is the url for your cloud account such as https://us-west-2-1.aws.cloud2.influxdata.com
- INFLUX_ORG: This is your organization name for your InfluxDB Cloud account.
- INFLUX_TOKEN: This is a token that Telegraf would use to fetch the remote config from your InfluxDB Cloud account and write data to the `oss_metrics` bucket. If you are just getting started, the easiest way is to just use an All Access token generated from the UI.

Once you set those ENV variables, you can use the setup instructions for the Telegraf config found in your InfluxDB Cloud account.

Once you have your Telegraf agents scraping metrics from your InfluxDB OSS instances, and the data is showing up in your InfluxDB Cloud Account, you can complete the deadman monitoring. The template installed a Deadman Check for data flowing from your OSS instance, but in order to be notified of any issues, you will need to configure a Notification Endpoint and a Notification Rule. For more information on configuring those, please see the [Monitoring & Alerting documentation](https://docs.influxdata.com/influxdb/cloud/monitor-alert/).

## Customizations

There are many more metrics collected than the ones displayed on the dashboard. Check outlocalhost:8086/metrics for a full list. They are also available by exploring the data populated inthe `oss_metrics` bucket.

## Contact

- Author: Russ Savage
- Email: russ@influxdata.com
- Github: [@russorat](https://github.com/russorat)
- Influx Slack: [@russ](https://influxdata.com/slack)
