# Google Cloud Platform Monitoring Template

Provided by: bonitoo.io

**Query data from Google Cloud Monitoring -- formerly Stackdriver -- using the Cloud Monitoring API v3.**

1. MySQL database hosted in Google Cloud SQL
2. The Compute dashboard provides deeper insight into the GCP compute services provided by GCP Stackdriver.
3. HTTPS LoadBalancing dashboard monitors network load balancing in the cluster.

Dashboard examples

![GCP Monitoring Cloud SQL](img/gcp-monitoring-cloudsql.png)
![GCP Monitoring Compute](img/gcp-monitoring-compute.png)
![GCP Monitoring LoadBalancing](img/gcp-monitoring-loadbalancing.png)

## Included Resources

The solution composes of the following resources:

- 3 Dashboards: `CloudSQL`, `Compute` and `HTTPS LoadBalancing`
- 1 Variable: `bucket`

## Setup Instructions

Load the dashboards and use the Telegraf Stackdriver plugin in your GCP cloud account.

## Customizations

n/a

## Contact

Provide a way for users to get in touch with you if they have questions or need help using your template. What information you give is up to you, but we encourage providing those below.

Author: Ivan Kudibal

Email: n/a

Github: @ivankudibal

Influx Slack: n/a
