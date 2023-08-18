# InfluxDB Community Templates

![verify-all-templates](https://github.com/influxdata/community-templates/workflows/verify-all-templates/badge.svg)
[![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://www.influxdata.com/slack)

InfluxDB 2.0 [introduces InfluxDB templates](https://www.influxdata.com/blog/introducing-community-influxdb-templates/)&mdash;prepackaged InfluxDB configurations that contain everything from dashboards and Telegraf configurations to notifications and alerts in a single manifest file. Use InfluxDB templates to get a fresh instance of InfluxDB set up quickly, create reusable templates for common setups, back up your own deployment setup, and share your templates with the community.

In true open source spirit, you can update InfluxDB templates with common use cases and share with other InfluxDB users, so they can get started faster, use known configurations, and contribute improvements to templates that benefit everyone in the community.

The purpose of this repository is to promote the creation, sharing, and reuse of templates among the InfluxDB community. Anybody can submit new templates or improvements upon existing templates and use these templates in their own InfluxDB instances.

## Templates

Start by reading [how to use a template](docs/use_a_template.md), then check each template's individual instructions for further setup and customization options.

| Template             | Description | Author |
|----------------------|-------------|:------:|
| [ADS-B Aircraft Tracking Metrics](ads-b/) | Visualize data gathered from an ADS-B receiver | [Tim Yocum](https://github.com/tkyocum) |
| [Air Quality](airquality/) | Retrieve air quality statistics from the US EPA website | [Kristina Robinson](https://github.com/kristinarobinson) |
| [Algorithmia](algorithmia/) | Monitor machine learning model performance metrics | [@koverholt](https://github.com/koverholt) |
| [Apex Legends](apex_legends/) | Collect player metrics from the game Apex Legends | [@b3vis](https://github.com/b3vis) |
| [AWS Cloudwatch Monitoring](aws_cloudwatch/) | Monitor AWS EC2 and ELB | [bonitoo.io](.) |
| [AWS Lambda](aws_lambda/) | Monitor AWS Lambda functions | [bonitoo.io](.) |
| [Azure SQL DB](azure_sql_db/) | View information of Azure SQL Database: CPU utilization, Memory, Database Size, Active Threads, Connections, Traffic and more. | [bonitoo.io](.) |
| [Ceph Cluster](ceph/) | Monitor your Ceph Cluster with Prometheus metrics | [@bonitoo.io](https://github.com/bonitoo-io) |
| [Counter Strike: Global Offensive](csgo/) | Get stats about your game. Kills, Deaths and stats by weapon. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Covid-19 in South America](covid19-southamerica/) | Current data and graphs covering Covid-19 cases and deaths in South America | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Covid-19 in The United States](covid19-usa-states/) | Current data, graphs, and maps covering Covid-19 cases, deaths, and vaccination rates in different states of the USA | [Sara Ghodsi](https://github.com/saraghds) |
| [Cribl LogStream](criblio_logstream/) | Monitor and visualize your metric data from Cribl LogStream. | [Clint Sharp](https://github.com/criblio) |
| [CSS Electronics](css_electronics/) | Visualize metric data from CSS electronics measuring. | [Wehmhőner Roman](https://github.com/sciator) |
| [Currency Exchange Rates](currency_exchange_rates/) | Visualize and analyze currency exchange rates using Quandl. | Wojciech Kocjan |
| [DigitalOcean Billing](do_billing/) | Get your balance, month consumption and month to date balance from your DigitalOcean account | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Docker](docker/) | Monitor your running docker containers. | [@russorat](https://github.com/russorat) |
| [Docker Hub](dockerhub/) | Track the stats of your Docker Hub Images | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Downsampling](downsampling/) | Downsample common Telegraf metrics. | [@russorat](https://github.com/russorat) |
| [Earthquake Monitoring](earthquake_usgs/) | Monitor earthquakes via USGS web service. | [@abalone23](https://github.com/abalone23) |
| [Elasticsearch](elasticsearch/) | Monitor your Elasticsearch single or multi-node deployment | [@bonitoo.io](https://github.com/bonitoo-io) |
| [Endpoint Security State](endpoint-security-state/) | Watch endpoint authentication availability and certificate status | [Darin Fisher](https://github.com/darinfisher) |
| [Enviro+](enviro_plus/) | View the air quality readings from a Pimoroni Enviro+ particulate matter sensor. | Russ Savage |
| [Fail2Ban](fail2ban/) | Monitor your Fail2Ban instance on multiple hosts and services. | [bonitoo.io](.) |
| [Fireboard](fireboard/) | Monitor data collected by a Fireboard thermometer. | [Scott Anderson](https://github.com/sanderson) |
| [Fortnite](fortnite/) | Track and analyze Fortnite player performance. | [@abalone23](https://github.com/abalone23) |
| [GCP Monitoring](gcp_monitoring/) | Monitor Google Cloud Platform.  | [bonitoo.io](.) |
| [Github](github/) | View information about your Github Repos. Forks, Issues, Stars and more. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [HAProxy](haproxy/) | Get metrics of your HAProxy instance. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [InfluxDB 1.x Monitor](monitoring_influxdb_1.x/) | Monitor your already running InfluxDB 1.x instance. | [@russorat](https://github.com/russorat) |
| [InfluxDB Enterprise 1.x Monitor](influxdb-enterprise-1x/) | Monitor your already running InfluxDB 1.x Enterprise instance. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [InfluxDB 2 OSS Metrics](influxdb2_oss_metrics/) | Monitor your InfluxDB 2 OSS instance using scrapers. | [@russorat](https://github.com/russorat) |
| [InfluxDB 2 Operational Monitoring](influxdb2_operational_monitoring/) | Monitor you tasks and cardinality on your already running InfluxDB 2 instance. | [@Anaisdg](https://github.com/Anaisdg) |
| [InfluxDB Cloud Usage Dashboard](usage_dashboard/) | Monitor your InfluxDB Cloud data usage and limit events. Send Slack alert when limit event is triggered. | [John Corrigan](https://github.com/corriganjohn) |
| [Island Pulse (Modbus)](modbus/) | Monitor Island Pulse energy gauge over Modbus | Ray Farias |
| [IoT Center example app](iot_center/) | Simple dashboard showing measured values from IoT devices. | [@bonitoo.io](https://github.com/bonitoo-io) |
| [Istio Service Mesh](istio/) | Istio is an open source service mesh that layers transparently onto existing distributed applications. Istio's powerful features provide a uniform and more efficient way to secure, connect, and monitor services. | [@bonitoo.io](https://github.com/bonitoo-io) |
| [Jboss Wildfly](jboss_wildfly/) | View information your Jboss Wildfly Instance using Jolokia. Uptime, Heap Memory, Non Heap Memory, Memory Pool, etc | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [JMeter](apache_jmeter/) | This template provides Apache JMeter dashboard | [bonitoo.io](.) |
| [Kafka](kafka/) | Monitor Kafka via Jolokia agent | [@samhld](https:/github.com/samhld) |
| [Kafka Kubernetes](kafka_kubernetes/) | Monitor Kafka broker running in Kubernetes | [bonitoo.io](.) |
| [Kubernetes Dashboards](k8s/) | Monitor your Kubernetes cluster. | [bonitoo.io](.) |
| [Linux System Monitor](linux_system/) | Monitor system resources on one or more Linux hosts. | [@russorat](https://github.com/russorat) |
| [Jenkins](jenkins/) | Monitor your Jenkins node and jobs. | Ray Farias |
| [Jetson Stats](jetson_stats/) | Monitor your Jetson device with Jetson Stats. | [@Jayclifford345](https://github.com/Jayclifford345)|
| [Micrometer](micrometer/) | Monitor your Java application using Micrometer. | [bonitoo.io](.) |
| [Microsoft SQL Server](mssql/) | View information of SQL Server Instance. Uptime, Databases Activities, Read and Write times and more. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [MinIO](minio/) | Monitor MinIO instance. Uptime, CPU process time, Memory allocated, s3 total and current request, Storage used and available and more. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [MongoDB](mongodb/) | View information of MongoDB Server. Uptime, Connectios, Queries, Documents Operations and more. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [MySQL / MariaDB](mysql_mariadb/) | View information of MySQL Instance. Uptime, Current Queries, Active Threads, Connections, Traffic and more. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Network Interface Monitor](network_interface_performance/) | Monitor network interfaces on one or more hosts. | [@russorat](https://github.com/russorat) |
| [Nextcloud](nextcloud/) | Show stats about your Nextcloud Instance. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Nginx Ingress Controller](nginx-ingress-controller/) | Monitor NGINX Ingress Controller with Prometheus metrics | [@bonitoo.io](https://github.com/bonitoo-io) |
| [Node.js](node_js/) | Monitor Node.js application. CPU, Memory, HTTP response time and more | [@bonitoo.io](https://github.com/bonitoo-io) |
| [Particle](particle/) | Sample dashboard displaying data published by Particle IoT devices | [bonitoo.io](.) |
| [Plant Buddy](plant_buddy/) | Monitor your plants health. | [@Jayclifford345](https://github.com/Jayclifford345)|
| [Postgres Monitor](postgresql/) | Monitor Postgres Server. CPU, Deadlocks, Data and more | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Prometheus Monitor](prometheus/) | Monitor Prometheus | [bonitoo.io](.) |
| [Raspberry Pi System Monitor](raspberry-pi/) | System overview monitoring for your Raspberry Pi with Raspbian. | [@bonitoo.io](https://github.com/bonitoo-io) |
| [Redis Monitor](redis/) | Monitor your Redis server. | [@russorat](https://github.com/russorat) |
| [Sample Data](sample-data/) | A collection of sample data that can be quickly imported into your instance. | [@russorat](https://github.com/russorat) |
| [Sensu Go](sensu_go/) | Monitor the performance of your Sensu Go observability tool. | [@nikkictl](https://github.com/nikkictl) |
| [sFlow Traffic Monitor](sflow/) | Monitor your sFlow traffic. | [@russorat](https://github.com/russorat) |
| [SNMP Monitoring](snmp/) | Dashboards showing metrics provided via SNMP protocol | [bonitoo.io](.) |
| [Speedtest Dashboard](speedtest/) | This template will show you information about the speed of your Internet connection using speedtest-cli | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Telegraf Dashboard](telegraf/) | View throughput and internal stats about your Telegraf instances | Steven Soroka |
| [The Things Network](thing_network/) | Monitor your Things Network devices and network. | [@Jayclifford345](https://github.com/Jayclifford345)|
| [Tomcat Dashboard](tomcat/) | Monitor your Tomcat instance. Include Threads, Commit Memory, Request Count, Traffic and more | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [vSphere System Monitor](vsphere/) | View information about vSphere system. CPU, RAM, Network, Disk Latency and more | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Weather Station](weather_station/) | Influxdata Weather Station is a smart IoT device that shows various information on the embedded OLED display. |
| [Website Monitor (Apache/Postgresql)](apache_postgresql/) | Monitor a website that uses Apache and Postgresql | [Michael Hall](https://github.com/mhall119) |
| [Website Monitor (NGINX/MySQL)](nginx_mysql/) | Monitor a website that uses NGINX and MySQL | Ray Farias |
| [Windows System Monitor](windows_system/) | Monitor system resources on one or more Windows hosts. | [@russorat](https://github.com/russorat) |
| [x509](x509/) | Simple dashboard for monitoring SSL certificates expiration. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |
| [Zookeeper](zookeeper/) | Dashboard for consuming data from Zookeeper client. | [Ignacio Van Droogenbroeck](https://github.com/xe-nvdk) |

To submit a new template, see our [contributing guide](docs/submit_a_template.md).

You can also ask the community to create a template for a specific use-case by creating a [Template Request](https://github.com/influxdata/community-templates/issues/new?template=template-request.md&labels=Template+Request).

## Support

Community InfluxDB templates are provided by members of the community. Template authors are solely responsible for supporting their templates. InfluxData does not test contributed templates, nor guarantee their quality or safety. If you have questions about or need help with a specific template, please contact the template author using the contact information provided in the template README.

InfluxData provides and supports the `influx` command-line tool and `influx apply` command for importing and exporting template manifests. You'll need the [InfluxDB 2.0.0 beta or greater](https://portal.influxdata.com/downloads/) for the `influx apply` command. For help with these tools, please join our [Community Slack](https://influxdata.com/slack) and ask for help in the `#community-support` channel.

[![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://www.influxdata.com/slack)
