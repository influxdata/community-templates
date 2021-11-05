# CSS Electronics OBD2 Monitoring Template

Provided by: [bonitoo.io](.)

This template provides a dashboard for [CSS electronics](https://www.csselectronics.com/) data example.

Want to deploy free, custom browser dashboards to display data from your CANedge devices?

The simplest bundle is the following:

* [CANedge1 (8 GB)](https://www.csselectronics.com/products/can-logger-sd-canedge1)
* [OBD2-DB9 adapter](https://www.csselectronics.com/products/obd2-db9-adapter-cable)

With this, you can log your own data from your own car to an SD card, which you can then extract to PC. Using the [Python script](https://github.com/CSS-Electronics/dashboard-writer) you can then decode the data and send it to your InfluxDB account for visualization through the template.

[Step-by-step guide CSS Electronics offers on this topic](https://canlogger.csselectronics.com/canedge-getting-started/log-file-tools/browser-dashboards/)

### Dashboard example

![Screenshot](css_electronics_dashboard.png)

### Quick Install

#### InfluxDB UI

In the InfluxDB UI, go to Settings->Templates and enter this URL: https://github.com/influxdata/community-templates/tree/master/css_electronics/css_electronics.yml

#### Influx CLI

If you have your InfluxDB credentials [configured in the CLI](https://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx apply https://github.com/influxdata/community-templates/tree/master/css_electronics/css_electronics.yml
```

## Included Resources

This template includes the following:

  - 1 bucket `test-bucket-new`
  - 1 dashboard `Truck dashboard with variables`
  - 2 variable `bucket` `_measurement`


## Setup Instructions

1. Load the dashboard according to the the paragraph above.
2. The [entire process of how to log data with a CANedge1/CANedge2 to an SD card or S3 bucket](https://grafana.com/blog/2021/09/21/with-grafana-and-influxdb-css-electronics-visualizes-can-iot-data-to-monitor-vehicles-and-machinery/).

## Contact

Author: Roman Wehmhőner, https://www.bonitoo.io

