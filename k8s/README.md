# Kubernetes Dashboards Template

Provided by: [bonitoo.io](.)

**This template provides 2 basic Kubernetes dashboards:
`Kubernetes Node Metrics` and `Kubernetes Inventory`. The K8S infrastrucure
supports Google Cloud Platform, AWS as well as on-premise K8S environments.**


Screenshots

![Screenshot](img/k8s-nodemetrics-dashboard.png)
![Screenshot](img/k8s-inventory-dashboard.png)


## Included Resources

The solution composes of the following resources:

- 2 Labels: `inputs.kubernetes`, `inputs.kube_inventory`, `K8S`
- 2 Dashboards: `Kubernetes Node Metrics`, `Kubernetes Inventory`
- 1 Variables: `bucket`

## Setup Instructions

Set up and install Telegraf `kubernetes` and `kube_inventory` plugins into your
Telegraf configmap.

* https://github.com/influxdata/telegraf/tree/master/plugins/inputs/kubernetes
* https://github.com/influxdata/telegraf/tree/master/plugins/inputs/kube

Set the `v.bucket` variable in the dashboards or settings to let dashboards know
what bucket holds the data.

## Customizations

n/a

## Contact

Authors: Ivan Kudibal, Tomas Klapka, https://www.bonitoo.io

Github: @ivankudibal
