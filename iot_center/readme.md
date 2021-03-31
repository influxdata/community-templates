# IoT Center Template

Provided by: [bonitoo.io](.)

This template provides a dashboard for [IoT Center](https://github.com/bonitoo-io/iot-center-v2) dev demo application.
  
### Dashboard example

![Screenshot](iot_center_dashboard.png)

### Quick Install

#### InfluxDB UI

In the InfluxDB UI, go to Settings->Templates and enter this URL: https://github.com/influxdata/community-templates/tree/master/iot_center/iot_center.yml

#### Influx CLI
If you have your InfluxDB credentials [configured in the CLI](https://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx apply https://github.com/influxdata/community-templates/tree/master/iot_center/iot_center.yml
```

## Included Resources

This template includes the following:

  - 1 Bucket: `iot_center`
  - 1 Label: `IoT`
  - 1 Dashboards: `IoT Center Application Monitoring`
  - 1 Variable: `IoT_Device`

## Setup Instructions

1. Load the dashboard according to the the paragraph above
1. Run IoT Center application according to the [installation steps](https://github.com/bonitoo-io/iot-center-v2)
1. Generate demo data using Virtual device

## Contact

Author: Miroslav Malecha, https://www.bonitoo.io
