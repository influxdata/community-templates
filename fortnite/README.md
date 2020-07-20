# Fortnite

Provides performance insights and metrics tracking for both professional and amateur Fortnite players such as friends and family using the unofficial [Fortnite API](https://fortniteapi.io/) service.

**Fortnite - All Players** Dashboard
- Track pros and friends/family separately.
- Click on any player to view detailed individual stats.

![Fortnite - All Players Screenshot](fortnite-all-players-screenshot.png)

**Fortnite - Individual Stats** Dashboard
- Track `squads`, `duos` and `solo` matches including total aggregated results.
- `K/D Ratio` dynamically changes `red`, `yellow` and `green` based on performance.

![Fortnite - Individual Stats Screenshot](fortnite-individual-stats-screenshot.png)

**Fortnite - Player Comparison** Dashboard:
- Compare stats between any two players to see who comes out on top.
- Final decision displays emoji based on custom metric to crown winner!

![Fortnite - Player Comparison Screenshot](fortnite-player-comparison-screenshot.png)

**Alerts**:
- Get alerted on Slack when your favorite Fortnite player wins!

![Slack Task Screenshot](fortnite-task-slack-screenshot.png)

### Quick Install

If you have your InfluxDB credentials [configured in the CLI](Vhttps://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx apply -u https://raw.githubusercontent.com/influxdata/community-templates/master/fortnite/fn-template.yml
```

## Included Resources
- 1 Bucket: `fortnite`
    - 30d retention
    - `fn_bucket` - user-definable resource name
- 1 Label: `fortnite`
- 1 Telegraf Configuration
    - `exec` input plugin
    - `influxdb_v2` output plugin
- 1 Task: `wins`
    - uses Slack webhook
- 3 Dashboards:
    - `Fortnite - All Players`
    - `Fortnite - Individual Stats`
    - `Fortnite - Player Comparison`
- 4 Query Variables:
    - `bucket`
    - `player`
    - `player2`
    - `season`
- 1 Python script: `get_fn_stats.py`
    - used by Telegraf exec plugin to access Fortnite API endpoint
- 1 CSV file: `players.csv`
    - seeded with professional Fortnite player ids

## Setup Instructions

1. Register for an account at [fortniteapi.io](fortniteapi.io)
2. Retrieve your API key at [dashboard.fortniteapi.io](dashboard.fortniteapi.io)
3. Look up Fortnite account ids with the following curl request:
```
curl --request GET 'https://fortniteapi.io/lookup?username=<USERNAME>' \
     --header 'Authorization: <API_KEY>'`
```
4. Add accounts to track in `players.csv`. For example:
    - `4735ce9132924caf8a5b17789b40f79c,yes,Ninja`
    - The second column indicates professional status: `yes`|`no`
5. Apply template: `./influx apply -f fn-template.yml`
    - General instructions on using InfluxDB Templates can be found in the [use a template](../docs/use_a_template.md) document.
6. You will be prompted for the bucket name (which will be created if it doesn't exist):
    - `Please provide environment reference value for key fn_bucket:`
    - The default bucket name is `fortnite`. If another bucket is used, the bucket name will need to be updated in the `wins` task, and the `player`, `player2` and `season` query variables.

### Telegraf
The Telegraf configuration requires the following environmental variables:
- `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `<FORTNITE>` bucket.
- `INFLUX_ORG` - The name of your organization found on the profile page.
- `INFLUX_BUCKET` - The name of the bucket to write to.
- `FORTNITE_API_TOKEN` - The [Fortnite API](https://fortniteapi.io/) token.

Information on using enviromental variables can be found in the [Telegraf Configuration documentation](https://github.com/influxdata/telegraf/blob/master/docs/CONFIGURATION.md#environment-variables).

The Telegraf `exec` input plugin requires the following files:
- `get_fn_stats.py` - Python script used to ingest metrics via the unofficial [Fortnite API](https://fortniteapi.io/)
    - `requests` module required
    - The current season is hardcoded: `season = 13`
        - Update this once the new season starts.

- `players.csv` - CSV file containing a list of players to track using the following fields:
    - `acct_id` - Fortnite Account ID
    - `pro` - **yes** for professional, **no** for friends and family
    - `player_name` - not used by Telegraf
    - Note: This file is populated with several professional players. Add friends, family and others that will be tracked separately from the pro players.

### Dashboards
The `Fortnite - All Players` dashboard displays a url drilldown to the `Fortnite - Individual Stats` dashboard. This url must be changed in the `Friends & Family` and `Pros` cells:
```
<INFLUX_HOST>/orgs/<INFLUX_ORG_ID>/dashboards/<FORTNITE_INDIVIDUAL_STATS_DASHBOARD_ID>
```
To get the full link, open the `Fortnite - Individual Stats` dashboard and copy the url up to but not including the "?".

### Tasks
The Influx task requires the following [influx secret](https://v2.docs.influxdata.com/v2.0/reference/cli/influx/secret/):

- `SLACK_WEBHOOK` - The Slack webhook is used to send a message when a player wins a match.
    - https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX

## Customizations

In order to make telemetry graphs more comprehensible due to large differences in performance between professionals and non-pros (friends and family), each group is tracked separately. You can add players, both professionals and friends/family by adding them to the `players.csv` file mentioned in the Telegraf setup section above.

### Tasks
Alerts are sent when any player wins a match:
```
|> filter(fn: (r) => (r["pro"] == "no" or r["pro"] == "yes"))
```
This can be updated to only track friends/family ie:
```
|> filter(fn: (r) => (r["pro"] == "no"))
```

### Fortnite Player Comparison
 - The formula used to calculate overall performance is:
```
kd_ratio * (wins * winrate)
```

Other metrics ingested from Telegraf but not used include:
- placetop3
- placetop5
- placetop10
- placetop25
- matchesplayed
- minutesplayed

These are available for `squads`, `duos` and `solo` matches.

## Contact

Author: Adam Silverman

Email: asilverman@influxdata.com

Github: @abalone23

Influx Slack: @Adam2