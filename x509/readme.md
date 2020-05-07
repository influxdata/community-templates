# x509 SSL Certificates Monitoring Dashboard

Provided by: Ignacio Van Droogenbroeck

This Dashboard is very simple but can help you with information about your x509 certificates about to expire. You can know how much certificates you're monitoring and the days to expire to each one of them.

![Dashboard Screenshot](screenshot.png)

## Included Resources

    - 1 Telegraf Configuration
    - 1 Dashboards: x509.json

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.
    
    Telegraf Configuration requires the following environment variables
    - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your master token to get started.
    - `INFLUX_ORG` - The name of your Organization.


In orden to use this Dashboard, you need to specify the url of the address you wish monitor in the file telegraf.conf Also, you can monitor files stored locally.

ex: <code>sources = ["/etc/ssl/certs/ssl-cert-snakeoil.pem", "https://google.com:443", "https://influxdata.com:443"]</code>


## Contact

Author: Ignacio Van Droogenbroeck

Email: ignacio[at]vandroogenbroeck[dot]net

Github and Gitlab user: @xe-nvdk 

Influx Slack: Ignacio Van Droogenbroeck
