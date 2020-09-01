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

If you have your InfluxDB credentials [configured in the CLI](https://v2.docs.influxdata.com/v2.0/reference/cli/influx/config/), you can install this template with:

```
influx apply -f https://raw.githubusercontent.com/influxdata/community-templates/master/fortnite/fn-template.yml --env-ref=fn_bucket=<INFLUX_BUCKET>
```
Note: If `fortnite` is not used for the `fn_bucket` name, the bucket name will need to be updated in the `wins` task, and the `player`, `player2` and `season` query variables.

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
    - used by Python script

## Setup Instructions

1. Register for an account at [fortniteapi.io](https://fortniteapi.io/)
2. Retrieve your Fortnite API token at [dashboard.fortniteapi.io](https://dashboard.fortniteapi.io)
3. Look up Fortnite account ids with the following curl request:
    ```
    curl --request GET 'https://fortniteapi.io/lookup?username=<USERNAME>' \
         --header 'Authorization: <FORTNITE_API_TOKEN>'
    ```
4. Check that the account returns metrics:
    ```
    curl --request GET 'https://fortniteapi.io/stats?account=<PLAYER_ID>&season=<SEASON>' \
         --header 'Authorization: <FORTNITE_API_TOKEN>'
    ```
    - Note: If the response contains `"global_stats":null` it's likely that that the **Show on Career Leaderboard** setting is set to **OFF** in the **Account and Privacy** section of the player's profile.

5. Add accounts to track in `players.csv`. For example:
    - `4735ce9132924caf8a5b17789b40f79c,yes,Ninja`
    - The second column indicates professional status: `yes`|`no`

### Telegraf
The Telegraf configuration requires the following environmental variables:
- `INFLUX_HOST` - The connection URL to your Cloud 2 account.
- `INFLUX_TOKEN` - The token with the permissions to read Telegraf configs and write data to the `<FORTNITE>` bucket.
- `INFLUX_ORG` - The name of your organization found on the profile page.
- `INFLUX_BUCKET` - The name of the bucket to write to.
- `FORTNITE_API_TOKEN` - The [Fortnite API](https://fortniteapi.io/) token.

Information on using enviromental variables can be found in the [Telegraf Configuration documentation](https://github.com/influxdata/telegraf/blob/master/docs/CONFIGURATION.md#environment-variables).

The Telegraf `exec` input plugin requires the following files:
- `get_fn_stats.py` - Python script used to ingest metrics via the unofficial [Fortnite API](https://fortniteapi.io/)
    - `requests` module required
    - The current season is hardcoded: `season = 14`
        - Update this when a new season starts.

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
```
influx secret update -k SLACK_WEBHOOK
```
Note: You will be prompted for the secret to add the Slack webhook.

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
