# Nginx Ingress Controller

Provided by: @bonitoo.io

Ingress-nginx is an Ingress controller for Kubernetes using NGINX as a reverse proxy and load balancer.
This InfluxDB template can be used to monitor your Nginx Controller setup inside your Kubernetes cluster.

![Example Dashboard Screenshot](img/nginx_ingress_controller.jpg)

### Quick Install

#### InfluxDB UI

In the InfluxDB UI, go to Settings->Templates and enter this URL: https://raw.githubusercontent.com/influxdata/community-templates/master/nginx-ingress-controller/nginx-ingress-controller.yml

#### Influx CLI
If you have your InfluxDB credentials [configured in the CLI](https://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/nginx-ingress-controller/nginx-ingress-controller.yml
```

## Included Resources

  - 2 Labels: `nginx-ingress`
  - 1 Telegraf Configuration: `nginx-ingress-controller`
  - 1 Dashboard: `Nginx Ingress Controller`
  - 4 Variables: `bucket`,`controller_namespace`,`controller_pod`,`controller_class`

## Setup Instructions

General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.

### Requirements:

#### Nginx Ingress Controller:

> Github: https://github.com/kubernetes/ingress-nginx
>
> Helm chart sources: https://github.com/kubernetes/ingress-nginx/tree/main/charts/ingress-nginx

Flux queries rely on prometheus input plugin v2 metric version format. It is not compatible with v1 or with UI Scraper metric format. 

#### Telegraf:

If possible, use Telegraf Prometheus input plugin to scrape Prometheus metrics from Controller service endpoint.
The Prometheus input plugin can be also configured to scrape Controller pod(s) directly via annotations.
    
Telegraf configuration requires the following environment variables
  - `INFLUX_HOST`
  - `INFLUX_BUCKET`
  - `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `telegraf` bucket. You can just use your operator token to get started.
  - `INFLUX_ORG` - The name of your Organization
  - `CONTROLLER_SVC_URLS` - URLs to Ingress Controller metrics endpoint service(s) e.g. `http://ingress-nginx-controller-metrics.default.svc.cluster.local:10254/metrics`. 

To reflect specific Kubernetes or Ingress Controller setup it may require additional Telegraf plugin configuration.  

You **MUST** set these environment variables before running Telegraf using something similar to the following commands
  - This can be found on the `Load Data` > `Tokens` page in your browser: `export INFLUX_TOKEN=TOKEN`
  - Your Organization name can be found on the Settings page in your browser: `export INFLUX_ORG=my_org`

## Contact

Author: Tomas Klapka, Bonitoo s.r.o.

Github: Bonitoo.io