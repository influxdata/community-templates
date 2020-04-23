# Kubernetes Node Metrics Template

Provided by: bonitoo.io

**This dashboard can be used to display Kubernetes Node metrics. The K8S infrastrucure supports Google Cloud Platform.**


![Screenshot](img/k8s-nodemetrics-dashboard.png)

## Included Resources

List what resources your template provides in this section. That will allow users to know at a glance what comes with it.

**Example:**

- 3 Labels: `inputs.kubernetes`, `GCP`
- 1 Dashboard: `GCP Kubernetes Node Metrics`
- 1 Variables: `bucket`

## Setup Instructions

[Download](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/kubernetes) and install Telegraf `Kubernetes` input plugin to your monitoring configmap to collect data. The measurement `kubernetes_node` is used. Set `v.bucket` variable.

## Customizations

n/a

## Contact

Provide a way for users to get in touch with you if they have questions or need help using your template. What information you give is up to you, but we encourage providing those below.

Authors: Ivan Kudibal, Tomas Klapka

Email: n/a

Github: @ivankudibal

Influx Slack: n/a