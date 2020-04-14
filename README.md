# InfluxDB Community Templates

[![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://www.influxdata.com/slack)

InfluxDB 2.0 [introduces InfluxDB templates](https://www.influxdata.com/blog/introducing-community-influxdb-templates/)&mdash;prepackaged InfluxDB configurations that contain everything from dashboards and Telegraf configurations to notifications and alerts in a single manifest file. Use InfluxDB templates to get a fresh instance of InfluxDB set up quickly, create reusable templates for common setups, back up your own deployment setup, and share your templates with the community.

In true open source spirit, you can update InfluxDB templates with common use cases and share with other InfluxDB users, so they can get started faster, use known configurations, and contribute improvements to templates that benefit everyone in the community.

The purpose of this repository is to promote the creation, sharing, and reuse of templates among the InfluxDB community. Anybody can submit new templates or improvements upon existing templates and use these templates in their own InfluxDB instances.

## Templates

Start by reading [how to use a template](docs/use_a_template.md), then check each template's individual instructions for further setup and customization options.

| Template             | Description | Author |
|----------------------|-------------|:------:|
| [Currency Exchange Rates](currency_exchange_rates/) | Visualize and analyze currency exchange rates using Quandl. | Wojciech Kocjan |
| [Enviro+](enviro_plus/) | View the air quality readings from a Pimoroni Enviro+ particulate matter sensor. | Simon Loffler |
| [InfluxDB 1.x Monitor](monitoring_influxdb_1.x/) | Monitor your already running InfluxDB 1.x instance. | Russ Savage |
| [InfluxDB 2 OSS Metrics](influxdb2_oss_metrics/) | Monitor your InfluxDB 2 OSS instance using scrapers. | Russ Savage |
| [Linux System Monitor](linux_system/) | Monitor system resources on one or more Linux hosts. | Russ Savage |
| [Jenkins](jenkins/) | Monitor your Jenkins node and jobs. | Ray Farias |
| [Network Interface Monitor](network_interface_performance/) | Monitor network interfaces on one or more hosts. | Russ Savage |
| [Website Monitor (Apache/Postgresql)](apache_postgresql/) | Monitor a website that uses Apache and Postgresql | Michael Hall |
| [Windows System Monitor](windows_system/) | Monitor system resources on one or more Windows hosts. | Russ Savage |
| [Telegraf Dashboard](telegraf/) | View throughput and internal stats about your Telegraf instances | Steven Soroka |


To submit a new template, see our [contributing guide](docs/submit_a_template.md).

You can also ask the community to create a template for a specific use-case by creating a [Template Request](https://github.com/influxdata/community-templates/issues/new?template=template-request.md&labels=Template+Request).


## Support

Community InfluxDB templates are provided by members of the community. Template authors are solely responsible for supporting their templates. InfluxData does not test contributed templates, nor guarantee their quality or safety. If you have questions about or need help with a specific template, please contact the template author using the contact information provided in the template README.

InfluxData provides and supports the `influx` command-line tool and `influx pkg` command for importing and exporting template manifests. You'll need the [InfluxDB 2.0.0 beta or greater](https://portal.influxdata.com/downloads/) for the `influx pkg` command. For help with these tools, please join our [Community Slack](https://influxdata.com/slack) and ask for help in the `#community-support` channel.

[![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://www.influxdata.com/slack)
