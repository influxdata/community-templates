## Modbus Monitoring Template

This InfluxDB Template can be used to gather data from a Modbus slave

![Website Monitoring Dashboard Screenshot](img/Dashboard.png)

### Included Resources

- 1 label: `island_pulse`
- 1 bucket: 'node8'
- 9 Alerts: Threshold checks for all areas in `area_names`
- 2 Variables: `area_names`, `energy_types`
- 1 Dashboard: `Island Pulse`  (see screenshot above)

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.

### Telegraf
  See `[[inputs.modbus]]` section in this template for [more information](./modbus.yml).

## Customizations


## Contact

- Author: Ray Farias
- Email: ray@sudokrew.com
- Github: [@sgnl](https://github.com/sgnl)
- Influx Slack: [@Ray Farias](https://influxdata.com/slack)