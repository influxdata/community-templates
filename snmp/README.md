# SNMP Monitoring Template

Provided by: [bonitoo.io](.)

This template provides several dashboards showing metrics provided via SNMP protocol. It provides both an example of standard SNMP stats and examples from Mikrotik and Cisco devices.

### Dashboard examples

![Screenshot](img/snmp-dashboard.png)

### Quick Install

If you have your InfluxDB credentials [configured in the CLI](Vhttps://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx pkg -u https://raw.githubusercontent.com/influxdata/community-templates/master/snmp/snmp.yml
```

## Included Resources

This template includes the following:

    - 1 Bucket: `snmp`, 1d retention
    - 3 Labels: `inputs.net`,`inputs.system`,`SNMP`
    - 3 Telegraf Configurations
    - 0 Checks: 
    - 3 Dashboards: `SNMP System Monitoring`, `SNMP Cisco Monitoring`, `SNMP Mikrotik Monitoring`
    - 2 Variables: `snmp_host`, and `snmp_ifName`

## Setup Instructions

Load the dashboards and use the [SNMP plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/snmp) into your
environment.

Include the Telegraf `inputs.snmp` plugin in your Telegraf configuration and start Telegraf. There are multiple configuration files per specific device.
SNMP tools must be installed on the device with telegraf. If labels are used in OIDs, appropritae MIB files must be installed as well.

Example for Ubuntu: `sudo apt install snmp snmp-mibs-downloader`

For Linux SNMP monitoring SNMP server must be installed and proprely configured.

Example for Ubuntu: `sudo apt install snmpd`

## Customizations

Extend the telegraf configuration using SNMP OID codes to process more metrics.

## Contact


Author: Miroslav Malecha, https://www.bonitoo.io

Github: @devmirek