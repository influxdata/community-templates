# Jetson_Stats and Telegraf
This InfluxDB Template can be used to gather system metrics from a Jetson Stats instance. 
![Jetson Stats Dashboard Screenshot](img/jetson-stats-dashboard.png)

The goal of this template is to provide an example of using Telgraf's exec input plugin to gather system stats from a Jetson device such as a Jetson nano then insert it into infux for storage and processing.

This template makes use of [Jetson_Stats](https://github.com/rbonghi/jetson_stats) make sure you install this package on your Jetson device. 



## Guide
For instructions on how to install Jetson Stats and configure the Exec Pluglin follow this blog [here](https://www.influxdata.com/blog/nvidia-jetson-series-part-1-jetson-stats/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
