# Influx Community Templates

[![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://www.influxdata.com/slack)

InfluxDB 2.0 introduces Influx Templates – prepackaged InfluxDB configurations that contain everything from dashboards and Telegraf configurations to notifications and alerts in a single manifest file. Use Influx Templates to get a fresh instance of InfluxDB set up quickly, create reusable templates for common setups, backup your own deployment setup, and share them with the community.

In true open source spirit, these templates of common use cases can be shared with other users of InfluxDB, so they can get started faster, using known good configurations, and contribute their own improvements to those templates that will benefit the original author and the wider community.

The purpose of this repository is to promote the creation, sharing, and reuse of templates among the InfluxDB community. Anybody can submit new templates or improvements upon existing templates and use these templates in their own InfluxDB instances.

## Templates

Start by reading [how to use a Template](docs/use_a_template.md), then check each template's individual instructions for further setup and customization options.

| Template             | Description | Author |
|----------------------|-------------|:------:|
| [Linux System Monitor](linux_system/) | Monitor system resources on one or more Linux hosts. | Russ Savage |
| [InfluxDB 1.x Monitor](monitoring_influxdb_1.x/) | Monitor your already running InfluxDB 1.x instance. | Russ Savage |

To submit a new template, see our [contributing guide](docs/submit_a_template.md).

You can also ask the community to create a Template for a specific use-case by creating a [Template Request](https://github.com/influxdata/community-templates/issues/new?template=template-request.md&labels=Template+Request).


## Support

Community Influx Templates are provided by members of the community. Template authors are solely responsible for supporting their templates. InfluxData does not test contributed templates, nor guarantee their quality or safety. If you have questions about or need help with a specific template, please contact the template author using the contact information provided in the template README.

InfluxData provides and supports the `influx` command-line tool and `influx pkg` command for importing and exporting template manifests. For help with these tools, please join our [Community Slack](https://influxdata.com/slack) and ask for help in the `#community-support` channel.

[![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://www.influxdata.com/slack)
