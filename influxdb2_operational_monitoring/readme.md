# InfluxDB 2 Operational Monitoring

Provided by: InfluxData

This directory contains two InfluxDB Templates, [Operational Monitoring Template](./influxdb2_operational_monitoring.yml) and [Cardinality Now Template](./cardinality_now.yml), that can be used to monitor your InfluxDB tasks and cardinality on your already running InfluxDB 2 instance. These templates are only compatible with the Cloud version of InfluxDB 2.

### Operational Monitoring Template

Monitoring your tasks allows you to:
1) Verify that critical downsampling and data transforation tasks are succeeding. 
2) Respond to task failures quickly. 

![Task Summary Dashboard Screenshot](img/task-summary-dashboard.png)

Monitoring your cardinality allows you to: 
1) Ensure that you're not experiencing runaway cardinality.
2) Verify that your downsampling tasks and retention policies are successfully reducing your series cardinality. 

This `Cardinality Explorer` dashboard is used by InfluxData to monitor the cardinality of InfluxData's own production monitoring InfluxDB instance.  The `cardinality` bucket is populated by the `cardinality_by_bucket` task which summarizes schema data about your InfluxDB instance. 
![Cardinality Explorer Screenshot](img/cardinality-explorer-dashboard1.png)
If the cardinality of a bucket is increasing exponentially, use this dashboard to drill into the cardinality of specific measurements to identify the source of runaway cardinality. 
![Cardinality Explorer Screenshot](img/cardinality-explorer-dashboard2.png)

#### Included Resources

  - 1 Bucket: `cardinality`, Forever
  - 1 Task: `cardinality_by_bucket`, 1h
  - 2 Labels: `operational_monitoring` 
  - 2 Dashboard: `Task Summary Dashboard`, `Cardinality Explorer`

### Cardinality Now 

This is a slimmed down version of the [Operational Monitoring Template](../influxdb2_operational_monitoring). This version allows you to monitor your currently cardinality without adding additional buckets or tasks to your instance (i.e. without increasing the cardinality of your instance). 

This `Cardinality Now` dashboard can help you identify your source of runaway cardinality when you have reached your cardinality limit.
![Cardinality Explorer Screenshot](img/cardinality-explorer-dashboard2.png)
Use this dashboard to drill into the cardinality of specific measurements to identify the source of runaway cardinality. 

#### Included Resources
  - 1 Labels: `cardinality` 
  - 1 Dashboard: `Cardinality Now`

### Quick Install

#### InfluxDB UI

In the InfluxDB UI, go to Settings->Templates and enter the URL for the template you wish to apply.
- For the Operational Monitoring Template: https://raw.githubusercontent.com/influxdata/community-templates/master/influxdb2_operational_monitoring/influxdb2_operational_monitoring.yml
- For the Cardinality Now Template: https://raw.githubusercontent.com/influxdata/community-templates/master/influxdb2_operational_monitoring/influxdb2_cardinality_now.yml

#### Influx CLI
If you have your InfluxDB credentials [configured in the CLI](https://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install each template with their respective URLs:
- For the Operational Monitoring Template:
  ```
  influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/influxdb2_operational_monitoring/influxdb2_operational_monitoring.yml
  ```
- For the Cardinality Now Template:
  ```
  influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/influxdb2_operational_monitoring/influxdb2_cardinality_now.yml
  ```
### Setup Instructions

  General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.

#### Setup Instruction for the Operational Monitoring Template

  The data for the `Task Summary Dashboard` is populated by data collected from the default `_tasks` bucket. The `Cardinality Explorer` dashboard is populated by data collected from the `cardinality` bucket. The best way to set this up is to first follow the instructions for installing any template. That will create the label, bucket, and dashboards for you.

  You must already have a task running in order to populate the `Task Summary Dashboard` with data. [Get started with InfluxDB tasks](https://docs.influxdata.com/influxdb/v2.0/process-data/get-started/) to create a task and populate the dashboard.  

#### Setup Instructions for the Cardinality Now Template 

 You must at least one bucket and have written data to that bucket for the `Cardinality Now` dashboard to be populated with data.  


## Contact

- Author: Anais Dotis-Georgiou
- Email: anais@influxdata.com
- Github: [@Anaisdg](https://github.com/Anaisdg)
- Influx Slack: [@Anais](https://influxdata.com/slack)


