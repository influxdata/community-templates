# Sample Data Template

This InfluxDB Template can be used to quickly load sample data into your InfluxDB Instance.

This includes the following sample datasets:

| Dataset Name             | Description | Source |
|--------------------------|-------------|-------:|
| Bitcoin Price Data | The current price for Bitcoin powered by CoinDesk - https://www.coindesk.com/price/bitcoin | https://www.coindesk.com/coindesk-api |
| USGS Earthquake Data | All the earthquake data for the last week. | https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php |
| NOAA National Bouy Data Center Data | The current reports from the NDBC annotated with station information. | https://www.ndbc.noaa.gov/realtime.shtml |
| Synthetic Sensor Data | An hour's worth of generated sensor data. | https://github.com/influxdata/influxdb2-sample-data/tree/master/air-sensor-data |


### Quick Install

#### InfluxDB UI

In the InfluxDB UI, go to Settings->Templates and enter this URL: https://raw.githubusercontent.com/influxdata/community-templates/master/sample-data/sample-data.yml

#### Influx CLI
If you have your InfluxDB credentials [configured in the CLI](https://v2.docs.influxdata.com/cloud/reference/cli/influx/config/), you can install this template with:

```
influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/sample-data/sample-data.yml
```

### Included Resources

- 1 Bucket: `sample_data`, 7d retention
- 1 Task: `Fetch Sample Data`

## Notes
If you prefer to only load some data into your InfluxDB instance, the individual data feeds are broken out into their own Templates as well.
    
## Contact

- Author: Russ Savage
- Email: russ@influxdata.com
- Github: [@russorat](https://github.com/russorat)
- Influx Slack: [@russ](https://influxdata.com/slack)
