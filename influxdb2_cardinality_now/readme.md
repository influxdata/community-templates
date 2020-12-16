# InfluxDB 2 Operational Monitoring

Provided by: InfluxData

This InfluxDB Template can be used to monitor your current InfluxDB cardinality on your already running InfluxDB 2 instance when you hit your cardinality limit. This template is only compatible with the Cloud version of InfluxDB 2.

This is a slimmed down version of the [influxdb2_operational_monitoring](../influxdb2_operational_monitoring) template. This version allows you to monitor your currently cardinality without increasing the cardinality of your instance. 

This `Cardinality Now` dashboard can help you identify your source of runaway cardinality.
![Cardinality Explorer Screenshot](img/cardinality-explorer-dashboard2.png)
Use this dashboard to drill into the cardinality of specific measurements to identify the source of runaway cardinality. 

### Quick Install

#### InfluxDB UI

In the InfluxDB UI, go to Settings->Templates and enter this URL: https://raw.githubusercontent.com/influxdata/community-templates/master/influxdb2_operational_monitoring/influxdb2_operational_monitoring.yml

#### Influx CLI
If you have your InfluxDB credentials [configured in the CLI](https://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/influxdb2_operational_monitoring/influxdb2_operational_monitoring.yml
```

## Included Resources
  - 1 Labels: `cardinality` 
  - 1 Dashboard: `Cardinality Now`

## Setup Instructions

  General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.

## Contact

- Author: Anais Dotis-Georgiou
- Email: anais@influxdata.com
- Github: [@Anaisdg](https://github.com/Anaisdg)
- Influx Slack: [@Anais](https://influxdata.com/slack)
