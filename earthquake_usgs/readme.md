# Earthquake Command Center

Provided by: Adam Silverman

This InfluxDB template uses the [United States Geological Survey (USGS) web service](https://earthquake.usgs.gov/fdsnws/event/1/) to monitor earthquakes around the world. The dashboard displays earthquakes that can be filtered based on `magnitude`, `location`, `location radius` (km or miles), and `time`.

Feed consumption is performed within an automated task so it is entirely serverless when run within [InfluxDB Cloud](https://www.influxdata.com/products/influxdb-cloud/). [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/), [client libraries](https://docs.influxdata.com/influxdb/cloud/tools/client-libraries/) and the [CLI](https://docs.influxdata.com/influxdb/cloud/tools/clis/) are **not** required. Additional data cleansing and shaping operations are performed using Flux. [[1]](https://www.github.com/influxdata/community-templates/tree/master/earthquake_usgs#additional-notes)

Slacks alerts are sent via a task, with customizable options such as separate magnitude thresholds for global and regional earthquakes, time zones, and delayed triggering. Links to the associated USGS earthquake summary and Google Maps pages are listed as well. [[2]](https://www.github.com/influxdata/community-templates/tree/master/earthquake_usgs#tasks)

**Dashboard**
![Earthquake Monitoring Dashboard](earthquake_monitoring.png)

### Quick Install

#### InfluxDB UI
In the InfluxDB UI, go to Settings->Templates and enter this URL: https://raw.githubusercontent.com/influxdata/community-templates/master/earthquake_usgs/earthquake_usgs_template.yml

#### Influx CLI
Although the CLI is not required, if you have your InfluxDB credentials
[configured in the CLI](https://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/),
you can install this template with:

```sh
influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/earthquake_usgs/earthquake_usgs_template.yml
```

## Included Resources
  - 1 Bucket: `apis`, 30d retention
  - 1 Label: `Earthquake`
  - 2 Tasks: `Earthquake Feed Ingestion`, `Earthquake Alerts`
  - 1 Dashboard: `Earthquake Command Center`
  - 4 Variables: `Magnitude_Threshold`, `Location`, `Radius`, and `Units`

## Setup Instructions
General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.

The `Earthquake Alerts` task is disabled by default since it requires a valid [Slack webhook](https://api.slack.com/messaging/webhooks) to send alerts.
Edit the task to update the webhook:
```
slack_webhook = https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
```

## Customizations
### Dashboard

The dashboard features the following locations to filter on:
- Hilo, Hawaii
- Los Angeles, California
- Oklahoma City, Oklahoma
- San Francisco, California
- Tokyo, Japan
- World

Additonal locations (with coordinates) can be added in the InfluxDB UI Settings->Variables->`Location` variable. Geographic coordinates can be found by entering the city in [Google Maps](https://www.google.com/maps/).

[Location emojis](https://emojipedia.org/travel-places/) used in the dashboard are stored in a [Flux dictionary](https://docs.influxdata.com/influxdb/v2.0/reference/flux/stdlib/dict/):
```
globe_dictionary = dict.fromList(pairs: [
    {key: "Hilo, HI", value: "🌋"},
    {key: "Los Angeles, CA", value: "🏖️"},
    {key: "Oklahoma City, OK", value: "🌪️"},
    {key: "San Francisco, CA", value: "🌉"},
    {key: "Tokyo, Japan", value: "🗾"}
])
```
From [USGS FAQ](https://www.usgs.gov/faqs/why-earthquake-was-reportedrecorded-network-x-or-i-felt-not-latest-earthquakes-maplist): "earthquakes smaller than 5.0 outside the U.S. [may not be recorded] unless they have caused significant damage or are widely felt (earthquakes this small rarely cause significant damage)"

### Tasks
Task options may be configured as well:

- `global_mag_threshold`
    - Default: `6`
    - Options: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`
    - Minimum earthquake magnitude to trigger an alert for a global earthquake
- `regional_mag_threshold`
    - Default: `3`
    - Options: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`
    - Minimum earthquake magnitude to trigger an alert for a regional earthquake
- `units`
    - Default: `miles`
    - Options: `miles`, `km`
    - Unit to display earthquake depth and distance
- `tz`
    - Default: `PST`
    - Options: `UTC`, `EST`, `EDT`, `CST`, `PST`, `PDT`
    - Timezone to display earthquake event
- `city`
    - Default: `San Francisco:37.7576948:-122.4726194`
    - City and geographic coordinates to alert for regional earthquakes (separated by colons)
- `city_radius`
    - Default: `1000.0`
    - Radius of city area
- `alert_delay_min`
    - Default: `5`
    - Delay (minutes) before sending alert
    - From [USGS FAQ](https://www.usgs.gov/faqs/why-do-some-earthquakes-disappear-maplist): "trade off between the speed of earthquake notifications and number of false alarms."

## Additional Notes
The `Earthquake Feed Ingestion` task used to consume the CSV web service requires that CSV data be in [annotated CSV](https://docs.influxdata.com/influxdb/v2.0/reference/syntax/annotated-csv/) format. The annotated CSV headers are located in [earthquake_usgs_headers.csv](https://raw.githubusercontent.com/influxdata/community-templates/master/earthquake_usgs/earthquake_usgs_headers.csv). The task also prepends the required metadata to each data record, which can then be written to InfluxDB.

Before ingestion, the following data cleansing and data shaping operatons are performed:
- Data Cleansing
    - Drop fields
    - Remove 0 kilometer distances from location string
    - Generate and standardize new country field based on location string
    - Specify tags
- Data Shaping (for Flux [Geo package](https://docs.influxdata.com/influxdb/v2.0/reference/flux/stdlib/experimental/geo/))
    - Add [S2 cell ID tokens](https://docs.influxdata.com/influxdb/v2.0/reference/flux/stdlib/experimental/geo/s2cellidtoken/) 
    - Rename geographic coordinate fields

The web service feed is:
```
https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&starttime=" + onedayago + "&includedeleted=true&orderby=time-asc
```
Note that the USGS web service [query parameters](https://earthquake.usgs.gov/fdsnws/event/1/#parameters) include:
- `format=csv`
    - CSV format
- `starttime=$onedayago`
    - Existing earthquake events may be updated later with more accurate details
- `includedeleted=true`
    - Include earthquake events that have been removed
- `orderby=time-asc`
    - Order earthquake events by ascending time

The fields are listed in [ComCat Documentation - Event Terms](https://earthquake.usgs.gov/data/comcat/data-eventterms.php)

## Contact

Author: Adam Silverman

Email: <a href="mailto:asilverman@influxdata.com">asilverman@influxdata.com</a>

Github: <a href="https://github.com/abalone23">@abalone23</a>

Influx Slack: <a href="https://influxdata.com/slack" rel="nofollow">@Adam2</a>