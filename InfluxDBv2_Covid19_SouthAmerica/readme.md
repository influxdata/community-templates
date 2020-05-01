# COVID-19 Dashboard focused in South America Data. 

Provided by: Ignacio Van Droogenbroeck

This Dashboard graph information about COVID-19 focused in Argentina, Bolivia, Brasil, Chile, Paraguay and Uruguay. Current data, new cases, graph about totals of cases and deaths. Also overall worldwide information about cases and deaths.  

![Dashboard Screenshot](screenshot.png)

## Included Resources

    - 1 Telegraf Configuration
    - 5 .sh files that get the information from the API and convert in JSON.
    - 1 Dashboards: datos_coronavirus_cono_sur_y_resto_del_mundo.json

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.
    
    Telegraf Configuration requires the following environment variables
    - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your master token to get started.
    - `INFLUX_ORG` - The name of your Organization.

    Also requiere adjust the information about the location of the executables files and set the agent interval to at least 10m, this for not hit to the api too much and cause service disruption. 

## Contact

Author: Ignacio Van Droogenbroeck

Email: ignacio[at]vandroogenbroeck[dot]net

Github and Gitlab user: @xe-nvdk 

Influx Slack: Ignacio Van Droogenbroeck