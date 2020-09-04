# Currency Exchange Rates Sample Template

Provided by: InfluxData

Uses [www.quandl.com](https://www.quandl.com/) for retrieving of data. It requires a free API key to use.

This InfluxDB Template can be used to analyze and monitor exchange rates and build indexes.

The included dashboard retrieves daily indexes from [European Central Bank](https://www.quandl.com/data/ECB-European-Central-Bank) data source.

The dashboard includes 4 sample exchange rates:
- EUR-USD
- EUR-GBP
- EUR-CHR
- USD-CHR

The goal of the template is to show how easy it is to use InfluxDB and Telegraf to retrieve time-series data from any source, add it to InfluxDB and be able to process it.

It also shows how to use functions such as [timedMovingAverage()](https://v2.docs.influxdata.com/v2.0/reference/flux/stdlib/built-in/transformations/aggregates/timedmovingaverage/) to perform basic analysis.

![Exchange Rates Screenshot](img/exchange-rates-dashboard.png)

### Quick Install

#### InfluxDB UI

In the InfluxDB UI, go to Settings->Templates and enter this URL: https://raw.githubusercontent.com/influxdata/community-templates/master/currency_exchange_rates/currency_exchange_rates.yml

#### Influx CLI
If you have your InfluxDB credentials [configured in the CLI](https://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/currency_exchange_rates/currency_exchange_rates.yml
```

## Included Resources

  - 1 Bucket: `quandl`, 30d retention
  - 2 Labels: `Exchange Rates`, `outputs.influxdb_v2`
  - 1 Telegraf Configuration: `Exchange Rates Data Retrieval.conf`
  - 1 Dashboards: `Exchange Rates`
  - 1 Variables: `bucket`

## Setup Instructions

  General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.
    
  The data for the dashboard is populated by the included Telegraf configuration. The Telegraf Configuration requires the following environment variables
    
  - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your operator token to get started.
  - `INFLUX_ORG` - The name of your Organization
  - `INFLUX_HOST` - The URL of your InfluxDB host (this can your localhost, a remote instance, or InfluxDB Cloud)
  - `QUANDL_API_KEY` - The API key for quandl

  You **MUST** set these environment variables before running Telegraf using something similar to the following commands
    
  - This can be found on the `Load Data` > `Tokens` page in your browser: `export INFLUX_TOKEN=TOKEN`
  - Your Organization name can be found on the Settings page in your browser: `export INFLUX_ORG=my_org`
  - Quandl API key can be retrieved from [Your Profile](https://www.quandl.com/account/profile) page

  You can start Telegraf using the instructions from the `Telegraf` > `Setup Instructions` link in the UI.

## Usage Instructions

  The source of the data shown in this dashboard is updated every weekday. Therefore, it is recommended to set the Time Range in the top-right corner of the dashboard to *Past 30d*.

  Please note that this telegraf configuration will retrieve the data every minute. This helps getting the data added  to InfluxDB fast. However, the data used in this example does not change often. After sending the initial data to InfluxDB, it is recommended to change the `interval` and `flush_interval` settings in Telegraf configuration to `12h` and restart Telegraf.

## Contact

- Author: Wojciech Kocjan
- Email: wkocjan@influxdata.com
- Github: [@wojciechka](https://github.com/wojciechka)
- Influx Slack: [@wojciechka](https://influxdata.com/slack)
