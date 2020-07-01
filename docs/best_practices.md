# Creating Useful Templates

InfluxDB makes it easy to export your current setup as a Template, but there's more to making a good Template than just exporting it. You want your Template to be easy to use, easy to customize, and easy to extend as well. Fortunately InfluxDB provides all the tools you need to do just that! Here are some things to consider using or including to improve the quality and usefulness of your Template.

## InfluxDB Resources

Almost any InfluxDB resource (those data objects you can see and create in the InfluxDB UI) can be exported as part of a Template, how many or how few you provide is up to you. Try to strike a balance between providing a complete solution and allowing flexibility for combining it with existing resources. See the [full list of resources supported](https://v2.docs.influxdata.com/v2.0/influxdb-templates/#template-resources) in our documentation.

### Effective Dashboards

At a minimum your Template should include a Dashboard. Dashboards are the primary way a user is going to experience your Template. Your Dashboard should provide a cohesive view of related data over a span of time. 

Rather than duplicating graphs to show filtered views of the same data, use [Variables](https://v2.docs.influxdata.com/v2.0/visualize-data/variables/) in your graph queries (more on that below) to let the user easily switch between views in the same graph. Define Variables using a static list of values or dynamically with a Flux query.

> **Tip:** If you have multiple perspectives to share on a data set, consider providing multiple Dashboards rather than trying to put everything into one. There are no limits on dashboard in templates.

### Bucket Choices

When using Buckets in your Template, you can:

 - Provide a default Bucket with your Template
 - Reuse an existing Bucket by name
 - Let the user choose their Bucket

#### Provide a default Bucket with your Template
You can include a uniquely-named [Bucket](https://v2.docs.influxdata.com/v2.0/reference/key-concepts/data-elements/#bucket) with your Template and use it as the default in Dashboards and Telegraf configurations.

> **Note:** While including a bucket with your template can simplify things for the user, those using the InfluxDB Cloud free tier have a limited number of buckets and may not be able to use your template. It also makes it harder to use the template with data in an existing bucket.

#### Reuse an existing Bucket by name
It's common for Telegraf to write to a Bucket named `telegraf`. Existing users likely already have a `telegraf` Bucket your template can use. Include information about Bucket dependencies in your Template's `README.md` with instructions for creating the Bucket if it doesn't exist.

#### Let the user choose their Bucket
The most flexible option is to let the user choose a Bucket instead. You can do this with a Variable that will provide them a drop-down list of their existing Buckets to choose from. Simply create a Query Variable called `bucket` with the following Flux query. Our documentation has some [common Variable queries](https://v2.docs.influxdata.com/v2.0/visualize-data/variables/common-variables/) you might find useful.

```
buckets()
  |> filter(fn: (r) => r.name !~ /^_/)
  |> rename(columns: {name: "_value"})
  |> keep(columns: ["_value"])
```
> **Note:** the `filter()` call removes the system Buckets `_monitoring` and `_tasks` from the list

Use the `v.bucket` Variable in your Dashboard cell queries:

```
from(bucket: v.bucket) 
```

Once a Variable is used in a cell query, the variable drop-down menu appears at the top of the page where users can select which value to use for the Variable.

![Bucket Variable](img/bucket_variable.png)

> **Tip:** If your Template includes a Telegraf configuration in your Template, use an environment variable such as `$INFLUX_BUCKET` so the user can define which Bucket they want it to send data to.

### Use Variables

[Variables](https://v2.docs.influxdata.com/v2.0/visualize-data/variables/) give users flexibility over your Template without having to make any changes to it. Create a Variable from the `Settings` -> `Variables` page of the InfluxDB UI.

![Create a Variable](img/create_variable.png)

#### Static Variables

There are two ways to create a static Variable. The first is to provide a simple list of options as comma-separated values (CSV):

```
value1,value2,value3
```

The other is to provide a map of values and display names:

```
display1:value1
display2:value2
display3:value3
```

#### Variables from tags

A common use case is in InfluxDB is to filter data by one of the `tags` in the measurement. You can make this configurable in your Dashboard by making a Variable out of them. Create a Query Variable with a Flux query like this one:

```
import "influxdata/influxdb/v1"
v1.measurementTagValues(bucket: "your_bucket_name", measurement: "your_measurement_name", tag: "your_tag_name")
```

This will give the user a drop-down menu with all of the unique values of the tag `your_tag_name` from the specified measurements.

### Use Labels

[Labels](https://v2.docs.influxdata.com/v2.0/visualize-data/labels/) let you tag your resources for easier identification in the UI and make it easier to export resources into a Template. If you have a mix of resources in your InfluxDB instance you will have to individually specify which ones to export so that you don't export them all. However, if you use unique Labels to identify resources, you can filter resources by Label when exporting your Template:

```
influx export all --filter=labelName=your_label_name
```

## Telegraf Configurations

A good Template needs to be more than just a Dashboard. It should also include ways to send data to a user's InfluxDB instance. This can be done in a number of ways, from making calls directly to the [InfluxDB API](https://v2.docs.influxdata.com/v2.0/write-data/#influxdb-api), using the [InfluxDB Client libraries](https://v2.docs.influxdata.com/v2.0/reference/api/client-libraries/), or by [using Telegraf](https://v2.docs.influxdata.com/v2.0/write-data/use-telegraf/) and it's many plugins that do the bulk of the work for you.

Telegraf is a widely used data collection agent with a large community that has contributed plugins for gathering data from a variety of sources. Whatever data you're collecting, chances are there's a Telegraf plugin that can help you do it. We recommend that Templates to include a Telegraf configuration for collecting data. If you use another method of sending data to InfluxDB, include that information and instructions in your Template's `README.md`.

### Use Environment Variables

To make your Telegraf configurations easily usable by others, use [environment variables](https://github.com/influxdata/telegraf/blob/master/docs/CONFIGURATION.md#environment-variables) for customizable options. In your template's `README.md`, include information about what environment variables need to be set.

The most common settings to replace with environment variables are in the `[[outputs.influxdb_v2]]` section of your Telegraf configuration:

```
urls = ["$INFLUX_HOST"]

token = "$INFLUX_TOKEN"

organization = "$INFLUX_ORG"
```

If your template allows users to choose their own `bucket` values, include a bucket variable in your Telegraf configuration also:

```
bucket = "$INFLUX_BUCKET"
```

Depending on what Telegraf input plugins you use, there may be other settings to replace with environment variables, such as host names, databases, or authentication credentials.

> **Note:** Document all environment variables in your Template's `README.md` so users will know what environment variables they need to set before using Telegraf.

### Telegraf Configuration Labels

Sometimes, it's handy to group Telegraf configurations by specific plugins. For example, if I want to make a change to an input plugin, being able to quickly find all Telegraf configurations using that plugin is helpful. Use Labels such as `inputs.plugin_name` to your Telegraf configurations to help users filter in the UI. 

### Add custom Telegraf configurations to your Template

To add a custom Telegraf configuration file to your template:

 1. Export your template using the command in the [submitting a template](submit_a_template.md) doc.
   
 2. Add the following to the end of the file, being sure to give a name for your Telegraf configuration:
    ```
    ---
    apiVersion: influxdata.com/v2alpha1
    kind: Telegraf
    metadata:
        name: unique-name-for-your-config
    spec:
        name: The Name Of Your Configuration
        config: |
    ```
        
 3. Copy and paste the contents of your Telegraf configuration file below what you just added, indenting it all until it is 4 spaces further indented than the `config:` line.
    

## Test Your Template

After you export your finished Template, test it to make sure that it applies cleanly, has everything you want to include, and that the instructions your provide in your `README.md` have all the necessary steps.

To create a clean, ephemeral InfluxDB testing environment, run InfluxDB inside of a Docker container:

```
 docker run -p 8086:8086 -p 9999:9999 quay.io/influxdb/influxdb:2.0.0-beta

```

After you create a new `Organization` and `Token` in your Docker instance (available at http://localhost:9999), follow the [instructions for using a Template](./use_a_template.md) to apply your Template.
