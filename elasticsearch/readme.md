# Elasticsearch Template

Provided by: [bonitoo.io](.)

Elasticsearch is a modern search and analytics engine which is based on Apache Lucene. 
The Elasticsearch cluster is a group of one or more Elasticsearch nodes instances that are connected together. 
The power of an Elasticsearch cluster lies in the distribution of tasks, searching and indexing, across all the nodes in the cluster.
The nodes in the Elasticsearch cluster can be assigned different jobs or responsibilities.

This template can be used to monitor your Elasticsearch single or multi-node deployment with following dashboards:

![Elasticsearch Cluster Dashboard](img/elasticsearch_dashboard.jpg)

### Quick Install

#### InfluxDB UI

In the InfluxDB UI, go to Settings->Templates and enter this URL: https://raw.githubusercontent.com/influxdata/community-templates/master/elasticsearch/elasticsearch.yml

#### Influx CLI

If you have your InfluxDB credentials [configured in the CLI](https://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/elasticsearch/elasticsearch.yml
```

## Included Resources

- 1 Label: `Elasticsearch`
- 1 Telegraf Configuration: `Elasticsearch`
- 1 Dashboard: `Elasticsearch Dashboard`
- 2 Variables: `bucket`, `elasticsearch_cluster_node`

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.

### Requirements:

#### ES:

- Elasticsearch standalone installation: https://www.elastic.co/guide/en/elasticsearch/reference/8.1/install-elasticsearch.html
- ES Helm chart: https://github.com/elastic/helm-charts/tree/main/elasticsearch
- Elastic Cloud Operator: https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-install-helm.html or
  https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-deploy-eck.html

#### Telegraf:

Telegraf uses the Elasticsearch input plugin to query ES endpoints to obtain Node Stats and optionally Cluster-Health metrics.

Blog post: https://www.influxdata.com/blog/using-the-telegraf-elasticsearch-input-plugin/

The Telegraf configuration requires the following environment variables

- `INFLUX_HOST`
- `INFLUX_BUCKET`
- `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your operator token to get started.
- `INFLUX_ORG` - The name of your Organization.
- `ES_URLS` - Specify a list of one or more Elasticsearch servers, with addition of username and password to the url to use basic authentication, e.g. http://user:pass@localhost:9200.

> Any specific configuration reflecting custom Kubernetes or Elasticsearch deployment might require additional changes in Telegraf/Elasticsearch configuration.

You **MUST** set these environment variables before running Telegraf using something similar to the following commands

- This can be found on the `Load Data` > `Tokens` page in your browser: `export INFLUX_TOKEN=TOKEN`
- Your Organization name can be found on the Settings page in your browser: `export INFLUX_ORG=my_org`

## Contact

- Email: tomas.klapka@bonitoo.io
