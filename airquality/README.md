Provided by: Kristina Robinson

Air Quality (Ozone and Small Particulates per Million) by zipcode from the U.S. EPA AirNow.gov API.

Quick Install

InfluxDB UI

In the InfluxDB UI, go to Settings-> Templates and enter this URL: http://raw.githubusercontent.com/influxdata/community-templates/master/airquality/airquality.yml

Influx CLI

If you have your InfluxDB credentials configured in teh CLI, you can install this template with: 
```influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/airquality/airquality.yml```


Included Resources

* 1 Bucket: `airquality`, 30 day retention (or you may use your own bucket)
* 1 Label: `airquality`
* 1 Telegraf Configuration `airquality-telegraf-config`
* 1 Dashboard: `Air Quality`
* 1 Variable: `bucket` (allows any bucket to be used)

Setup Instructions

Go to https://docs.airnowapi.org/account/request/ to request account access.
Go to https://docs.airnowapi.org/forecastsbyzip/query, and build your URL as follows:
* Enter the zip code of interest
* Select `application/json` from the Format dropdown
* Click `Build`
* Copy the URL string.
* Create an environment variable call `INFLUX_AIRQUAL_URL` and use the copied URL string, but remove the date parameter (this allows the call to always retrieve the current date).

Example URL String:
```
"https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=99999&distance=25&API_KEY=A1B2C3D4-A1B2-A1B2-A1B1-A1B2C3D4E5F6"
```

Telegraf Configuration requires the following environment variables:

INFLUX_TOKEN - The token with the permissions to read Telegraf configs and write data to the telegraf bucket. You can just use your operator token to get started.
INFLUX_ORG - The name of your Organization
INFLUX_HOST - The url of the cloud instance where InfluxDB runs
INFLUX_BUCKET - The name of the bucket to put data into.  Default is `airquality`.
INFLUX_AIRQUAL_URL - The constructed URL to call the airnow API.  Instructions above.
You MUST set these environment variables before running Telegraf using something similar to the following commands

* This can be found on the Load Data > Tokens page in your browser: export INFLUX_TOKEN=TOKEN
* Your Organization name can be found on the Settings page in your browser: export INFLUX_ORG=my_org
* The host is the base URL of your cloud instance: export INFLUX_HOST=https://my-cloud.cloud2.influxdata.com
* INFLUX_BUCKET is the bucket to store the Air Quality data.  export INFLUX_BUCKET=airquality
* INFLUX_AIRQUAL_URL should be set to the airnow API URL, without a date param.  export INFLUX_AIRQUAL_URL=https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=99999&distance=25&API_KEY=A1B2C3D4-A1B2-A1B2-A1B1-A1B2C3D4E5F6

Start Telegraf on your local machine with the instructions provided from the Setup Instructions popup (click Data, Telegraf, Setup Instructions).


Contact

Author: Kristina Robinson

Email: kristina@influxdata.com

GitHub: @kristinarobinson

Slack: @Kristina Robinson
