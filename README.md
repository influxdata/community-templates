# InfluxDB Community Templates

[![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://www.influxdata.com/slack)

InfluxDB 2.0 [introduces InfluxDB templates](https://www.influxdata.com/blog/introducing-community-influxdb-templates/)&mdash;prepackaged InfluxDB configurations that contain everything from dashboards and Telegraf configurations to notifications and alerts in a single manifest file. Use InfluxDB templates to get a fresh instance of InfluxDB set up quickly, create reusable templates for common setups, back up your own deployment setup, and share your templates with the community.

In true open source spirit, you can update InfluxDB templates with common use cases and share with other InfluxDB users, so they can get started faster, use known configurations, and contribute improvements to templates that benefit everyone in the community.

The purpose of this repository is to promote the creation, sharing, and reuse of templates among the InfluxDB community. Anybody can submit new templates or improvements upon existing templates and use these templates in their own InfluxDB instances.

## Templates

Start by reading [how to use a template](docs/use_a_template.md), then check each template's individual instructions for further setup and customization options.

| Template             | Description | Author |
|----------------------|-------------|:------:|
| [AWS Cloudwatch Monitoring](aws_cloudwatch/) | Monitor AWS EC2 and ELB | [bonitoo.io](.) |
| [Counter Strike: Global Offensive](csgo/) | Get stats about your game. Kills, Deaths and stats by weapon. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Currency Exchange Rates](currency_exchange_rates/) | Visualize and analyze currency exchange rates using Quandl. | Wojciech Kocjan |
| [Covid-19 in South America](InfluxDBv2_Covid19_SouthAmerica/) | Current data and graphs covering Covid-19 cases and deaths in South America | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Docker](docker/) | Monitor your running docker containers. | [@russorat](https://github.com/russorat) |
| [Endpoint Security State](endpoint-security-state/) | Watch endpoint authentication availability and certificate status | [Darin Fisher](https://github.com/darinfisher) |
| [Enviro+](enviro_plus/) | View the air quality readings from a Pimoroni Enviro+ particulate matter sensor. | Simon Loffler |
| [GCP Monitoring](gcp_monitoring/) | Monitor Google Cloud Platform.  | [bonitoo.io](.) |
| [Github](github/) | View information about your Github Repos. Forks, Issues, Stars and more. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [HAProxy](haproxy/) | Get metrics of your HAProxy instance. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [InfluxDB 1.x Monitor](monitoring_influxdb_1.x/) | Monitor your already running InfluxDB 1.x instance. | [@russorat](https://github.com/russorat) |
| [InfluxDB 2 OSS Metrics](influxdb2_oss_metrics/) | Monitor your InfluxDB 2 OSS instance using scrapers. | [@russorat](https://github.com/russorat) |
| [Island Pulse (Modbus)](modbus/) | Monitor Island Pulse energy gauge over Modbus | Ray Farias |
| [Kafka](kafka/) | Monitor Kafka via Jolokia agent | [@samhld](https:/github.com/samhld)
| [Kubernetes Dashboards](k8s/) | Monitor your Kubernetes cluster. | [bonitoo.io](.) |
| [Linux System Monitor](linux_system/) | Monitor system resources on one or more Linux hosts. | [@russorat](https://github.com/russorat) |
| [Jenkins](jenkins/) | Monitor your Jenkins node and jobs. | Ray Farias |
| [MongoDB](mongodb/) | View information of MongoDB Server. Uptime, Connectios, Queries, Documents Operations and more. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Microsoft SQL Server](mssql/) | View information of SQL Server Instance. Uptime, Databases Activities, Read and Write times and more | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [MySQL / MariaDB](mysql_mariadb/) | View information of MySQL Instance. Uptime, Current Queries, Active Threads, Connections, Traffic and more. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Network Interface Monitor](network_interface_performance/) | Monitor network interfaces on one or more hosts. | [@russorat](https://github.com/russorat) |
| [Postgres Monitor](postgresql/) | Monitor Postgres Server. CPU, Deadlocks, Data and more | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Redis Monitor](redis/) | Monitor your Redis server. | [@russorat](https://github.com/russorat) |
| [sFlow Traffic Monitor](sflow/) | Monitor your sFlow traffic. | [@russorat](https://github.com/russorat) |
| [Telegraf Dashboard](telegraf/) | View throughput and internal stats about your Telegraf instances | Steven Soroka |
| [Tomcat Dashboard](tomcat/) | Monitor your Tomcat instance. Include Threads, Commit Memory, Request Count, Traffic and more | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [vSphere System Monitor](vsphere/) | View information about vSphere system. CPU, RAM, Network, Disk Latency and more | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Website Monitor (Apache/Postgresql)](apache_postgresql/) | Monitor a website that uses Apache and Postgresql | [Michael Hall](https://github.com/mhall119) |
| [Website Monitor (NGINX/MySQL)](nginx_mysql/) | Monitor a website that uses NGINX and MySQL | Ray Farias |
| [Windows System Monitor](windows_system/) | Monitor system resources on one or more Windows hosts. | [@russorat](https://github.com/russorat) |
| [x509](x509/) | Simple dashboard for monitoring SSL certificates expiration. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Zookeeper](zookeeper/) | Dashboard for consuming data from Zookeeper client. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |

To submit a new template, see our [contributing guide](docs/submit_a_template.md).

You can also ask the community to create a template for a specific use-case by creating a [Template Request](https://github.com/influxdata/community-templates/issues/new?template=template-request.md&labels=Template+Request).


## Support

Community InfluxDB templates are provided by members of the community. Template authors are solely responsible for supporting their templates. InfluxData does not test contributed templates, nor guarantee their quality or safety. If you have questions about or need help with a specific template, please contact the template author using the contact information provided in the template README.

InfluxData provides and supports the `influx` command-line tool and `influx pkg` command for importing and exporting template manifests. You'll need the [InfluxDB 2.0.0 beta or greater](https://portal.influxdata.com/downloads/) for the `influx pkg` command. For help with these tools, please join our [Community Slack](https://influxdata.com/slack) and ask for help in the `#community-support` channel.

[![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://www.influxdata.com/slack)
