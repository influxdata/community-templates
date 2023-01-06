## InfluxDB TSM to IOx Migration Template

Provided by: [Scott Anderson](https://github.com/sanderson/)

Use this InfluxDB TSM to IOX Migration template to run and monitor data migrations
from **InfluxDB Cloud or OSS (backed by TSM)** to and InfluxDB Cloud organization
(backed by [InfluxDB IOx](https://www.influxdata.com/blog/intro-influxdb-iox/)).

![InfluxDB Cloud Migration Dashboard Screenshot](img/migration-dashboard.png)

**Important:** Install this template on the **InfluxDB Cloud or OSS** instance
you want to migrate data _from_.

## Quick Install

### InfluxDB UI

In the InfluxDB UI, go to **Settings > Templates** and enter the following URL:

```sh
https://raw.githubusercontent.com/influxdata/community-templates/master/influxdb-tsm-iox-migration/migration.yml
```

### Influx CLI

If you have your InfluxDB credentials [configured in the CLI](https://docs.influxdata.com/influxdb/latest/reference/cli/influx/config/), install this template with:

```sh
influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/influxdb-tsm-iox-migration/migration.yml
```

## Included Resources

- 1 Bucket: `migration`
- 1 Dashboard: `InfluxDB TSM to IOx Migration Progress`
- 3 Dashboard Variables:
  - `destination_org`
  - `destination_bucket`
  - `migrationTaskID`
- 1 Task: `Migrate data from TSM to IOx`
- 1 Label: `IOx migration`

## Setup Instructions

General instructions on using InfluxDB Templates can be found in [Use a template](../docs/use_a_template.md).

### Set up the migration

{{% note %}}
The migration process requires two buckets in your source InfluxDB
organization—one bucket to store the migrated data and another bucket to store migration metadata.
If the destination organization uses the [InfluxDB Cloud Free Plan](https://docs.influxdata.com/influxdb/cloud/account-management/limits/#free-plan),
any buckets in addition to these two will exceed the your plan's bucket limit.
{{% /note %}}

1.  **In the InfluxDB Cloud (IOx) organization you're migrating data _to_**:

    1. Create a bucket **to migrate data to**.
    2. Create an API token with **write access** to the bucket you want to migrate to.

2.  **In the InfluxDB Cloud (TSM) organization you're migrating data _from_**:

    1.  Add the **InfluxDB Cloud API token from the IOx-backed organization**
        as a secret using the key, `INFLUXDB_IOX_TOKEN`.
        _See [Add secrets](https://docs.influxdata.com/influxdb/cloud/security/secrets/add/) for more information._
    2.  [Create a bucket](https://docs.influxdata.com/influxdb/cloud/organizations/buckets/create-bucket/)
        **to store temporary migration metadata**.
    3.  Edit the **Migrate data from TSM to IOx** task installed with this
        template and update the `migration` record properties to suit your migration:

        **migration**:
        - **start**: Earliest time to include in the migration.
          _See [Determine your migration start time](https://docs.influxdata.com/influxdb/cloud/migrate-data/migrate-cloud-to-cloud/#determine-your-migration-start-time)._
        - **stop**: Latest time to include in the migration.
        - **batchInterval**: Duration of each time-based batch.
          _See [Determine your batch interval](https://docs.influxdata.com/influxdb/cloud/migrate-data/migrate-cloud-to-cloud/#determine-your-batch-interval)._
        - **batchBucket**: InfluxDB Cloud (TSM) bucket to store migration batch metadata in.
        - **sourceBucket**: InfluxDB Cloud (TSM) bucket to migrate data from.
        - **destinationHost**: [InfluxDB Cloud (IOx) region URL](https://docs.influxdata.com/influxdb/cloud-iox/reference/regions)
          to migrate data from.
        - **destinationOrg**: InfluxDB Cloud (IOx) organization to migrate data to.
        - **destinationToken**: InfluxDB Cloud (IOx) API token. To keep the API token secure, store
          it as a secret in InfluxDB Cloud (TSM).
        - **destinationBucket**: InfluxDB OSS bucket to migrate data to.

    4. Save and enable the task to begin the migration.

**After the migration is complete**, each subsequent migration task execution
will fail with the following error:

```
error exhausting result iterator: error calling function "die" @41:9-41:86:
Batch range is beyond the migration range. Migration is complete.
```

For detailed information about this data migration process, see
[Migrate data from TSM to IOx](https://docs.influxdata.com/influxdb/cloud-iox/migrate-data/migrate-tsm-to-iox/).

## Contact

- Author: Scott Anderson
- Email: scott@influxdata.com
- Github: [@sanderson](https://github.com/sanderson)
- Influx Slack: [@Scott](https://influxdata.com/slack)
