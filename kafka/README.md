# Kafka Monitoring Template with Telegraf and Jolokia

## Visualized insights

   <img src="https://github.com/influxdata/community-templates/blob/kafka_template/kafka/kafka-dash.png" width="425"/> <img src="https://github.com/influxdata/community-templates/blob/kafka_template/kafka/kafka-dash-light.png" width="425"/>


## Requirements

* Set environment variables on host/s from which Telegraf will be sending metrics.  These are:
  - `INFLUX_ORG`, `INFLUX_TOKEN`, `INFLUX_HOST`, and `INFLUX_BUCKET`
* [Jolokia JVM Agent](https://jolokia.org/agent/jvm.html)
* [Apache Kafka](https://kafka.apache.org/documentation/)
* [Apache Zookeeper](https://zookeeper.apache.org/)

*Note: Kafka and Zookeper can be easily obtained and managed through the open source [Confluent Platform](https://www.confluent.io/download).*

## Quick Install
If you have your InfluxDB credentials configured in the CLI, you can install this template with:

`influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/kafka/{your_template_file}`

## Included Resources

- 1 label: `kafka`
- 1 Telegraf Configuration
- 1 Dashboards: `Kafka-metrics`
- 3 Variables: `bucket`, `broker_host`, and `kafka_topic`

## Pre-work

* This template does not require -- and therefore support -- TLS configurations.  If you have TLS enabled for Jolokia/Zookeeper, you will want to provide that information to the Telegraf configuration.  Simply follow [this](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/jolokia2#jolokia-agent-configuration) for Jolokia and [this](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/zookeeper#configuration) for Zookeeper.  Comprehensive TLS docs as it pertains to Telegraf can be found [here](https://github.com/influxdata/telegraf/blob/master/docs/TLS.md).

## Telegraf inputs
* [Jolokia](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/jolokia2)
* [Zookeeper](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/zookeeper)


## Schema (per broker)
*Note: Fields are verbose so the byte size of this dataset is larger than average.*


* Telegraf metrics ([lines of Line Protocol](https://v2.docs.influxdata.com/v2.0/reference/syntax/line-protocol/)): 143
* Tags per line (mean)': 3.50
* Fields per line (mean)': 9.90
* Tags per line (mode)': 3
* Fields per line (mode)': 4
* Tags per line (median)': 3
* Fields per line (median)': 4
* Total Measurements: 8


### Measurements
* kafka_broker (**still have to add Type=DelayedOperationPurgatory**)
  * Tags
    * host
    * jolokia_agent_url
    * topic
  * Fields
    * BytesInPerSec_FifteenMinuteRate
    **(come back)**
* kafka_controller
* kafka_replica_controller
* kafka_network
* zk_client (Kafka perspective)

**add ZK metrics**: https://github.com/influxdata/telegraf/tree/master/plugins/inputs/zookeeper#metrics

Author: Sam Dillard

Email: sam@influxdata.com

Github: samhld

Influx Slack: @sam