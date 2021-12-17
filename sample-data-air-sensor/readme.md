# Sample Data Template – Air Sensors

This InfluxDB Template can be used to quickly load and visualize sample air
sensor data your InfluxDB Instance.
Data includes temperature, humidity, and carbon monoxide metrics.

![Air Sensor Sample Data Dashboard Screenshot](img/air-sensor-dashboard.png)

### Quick Install

#### InfluxDB UI

In the InfluxDB UI, go to Settings->Templates and enter this URL: https://raw.githubusercontent.com/influxdata/community-templates/master/sample-data-air-sensor/sample-data-air-sensor.yml

#### Influx CLI
If you have your InfluxDB credentials [configured in the CLI](https://docs.influxdata.com/cloud/reference/cli/influx/config/), you can install this template with:

```
influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/sample-data-air-sensor/sample-data-air-sensor.yml
```

### Included Resources

- 1 Bucket: `sampledata`, 7d retention
- 1 Dashboard: `Air Sensors`
- 1 Task: `Sample Data - Air Sensors`
- 1 Variable: `temperature_unit`
- 1 Label: `Sample data`
    
## Contact

- Author: Scott Anderson
- Email: scott@influxdata.com
- Github: [@sanderson](https://github.com/sanderson)
- Influx Slack: [@scott](https://influxdata.com/slack)
