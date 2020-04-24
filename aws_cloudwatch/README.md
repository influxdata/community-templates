# AWS Cloudwatch Monitoring Template

Provided by: [bonitoo.io](.)

**Display data from AWS EC2 andn ELB using the AWS Cloudwatch Service.**

1. The AWS Cloudwatch Network Load Balancers monitoring dashboard displays data from `cloudwatch_aws_network_elb` measurement.
2. The AWS Cloudwatch Instance Monitoring dashboard displays data from the `cloudwatch_aws_ec2` measurement.

Dashboard examples

![AWS Cloudwatch Instance Monitoring](img/aws-cloudwatch-instance-monitoring.png)
![AWS Cloudwatch NLB Monitoring](img/aws-cloudwatch-nlb-monitoring.png)

## Included Resources

The solution composes of the following resources:

- 2 Labels: `inputs.cloudwatch`, `AWS`
- 2 Dashboards: `AWS Cloudwatch Instance Monitoring`, `AWS Cloudwatch NLB Monitoring`
- 1 Variable: `bucket`

## Setup Instructions

Load the dashboards and use the [Telegraf Cloudwatch plugin](https://github.com/influxdata/telegraf/tree/master/plugins/inputs/cloudwatch) into your
environment.

Set the `v.bucket` variable in the dashboards or settings to let dashboards know
what bucket holds the data.


## Customizations

n/a

## Contact

Author: Ivan Kudibal, Tomas Klapka, https://www.bonitoo.io

Github: @ivankudibal
