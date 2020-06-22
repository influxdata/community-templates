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

## Pre-work

* This template does not require -- and therefore support -- TLS configurations.  If you have TLS enabled for Jolokia/Zookeeper, you will want to provide that information to the Telegraf configuration.  Simply follow [this](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/jolokia2#jolokia-agent-configuration) for Jolokia and [this](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/zookeeper#configuration) for Zookeeper.  Comprehensive TLS docs as it pertains to Telegraf can be found [here](https://github.com/influxdata/telegraf/blob/master/docs/TLS.md).

## Telegraf inputs
* [Jolokia](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/jolokia2)
* [Zookeeper](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/zookeeper)


## Schema
*Note: Fields are verbose so the byte size of this dataset is larger than average.*


* Telegraf metrics ([lines of Line Protocol](https://v2.docs.influxdata.com/v2.0/reference/syntax/line-protocol/)): 143
* Mean tags per line': 3.50
* Mean fields per line': 9.90
* Tags mode': 3
* Fields mode': 4
* Tags median': 3
* Fields median': 4
* Measurements: 8



<!-- ### Cardinality per broker
* Floor: **count this when fully instrumented**
* Ceiling: dependent on number of topics, partitions, error *types* incurred
* **provide information on how to predict cardinality with scale** -->

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
