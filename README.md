# Influx Community Templates

[![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://www.influxdata.com/slack)

InfluxDB 2.0 introduces Influx Templates – prepackaged InfluxDB configurations that contain everything from dashboards and Telegraf configurations to notifications and alerts in a single manifest file. Use Influx Templates to get a fresh instance of InfluxDB set up quickly, create reusable templates for common setups, backup your own deployment setup, and share them with the community.

In true open source spirit, these templates of common use cases can be shared with other users of InfluxDB, so they can get started faster, using known good configurations, and contribute their own improvements to those templates that will benefit the original author and the wider community.

The purpose of this repository is to promote the creation, sharing, and reuse of templates among the InfluxDB community. Anybody can submit new templates or improvements upon existing templates and use these templates in their own InfluxDB instances.

## Use a Template

Each template provides a manifest file and instructions for using the template.
To import a template, use the following command:

```
 influx pkg --org <organization_name> --file ~/path/to/template/manifest.yml
 ```

This imports the specified `manifest.yml` into an instance of InfluxDB running on `localhost`.

> Manifest files can be YAML, JSON or Jsonnet.

If you don't want to download the manifest file locally, you can point to its remote location using the `--url` flag, for example:
```
 influx pkg --org <organization_name> --url https://raw.githubusercontent.com/influxdata/community-templates/master/template/manifest.yml
 ```

### Use Templates in InfluxDB Cloud

If using InfluxDB Cloud or running InfluxDB on a remote server, provide the URL of your InfluxDB instance using the `--host` flag and provide your InfluxDB authentication token using the ``--token`` flag:

```
 influx pkg --org <organization_name> --file ~/path/to/template/manifest.yml --host <hostname> --token <token>
```

> Need help? You can find [support](#support) information at the bottom of this page.

## Submit a Template

To contribute a new template or enhance an existing template, submit a pull request to this repository.

> Submissions must be provided under the [Apache Public License v2](https://www.apache.org/licenses/LICENSE-2.0).



1. [Fork this repo](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) on Github, and then clone it locally on your machine.
   ```
   git clone https://github.com/<your_github_name>/community-templates
   ```


2. Apply your changes to the clone repository on your local machine.


    * To submit and entirely new template, create a new directory for your template and create a `README.md` that describes your template and how to use it. See the `Example_README.md` file in this repository. **Be sure to include a way for users to get in contact with you**.

        Use the following command to export the template and generate a manifest file:

        ```
        influx pkg export --file ~/path/to/template/manifest.yml
        ```

        > Exported manifest files will be YAML or JSON. The filename extension you provide will determine the format used.

    * To update an existing template, make the changes to template files in the appropriate directory.

3. Add and commit your changes and push them to Github. Include the `--signoff` flag when committing your changes to include your author information in the commit message.

    ```
    # Add your changes
    git add .

    # Commit your changes with a commit message
    git commit --signoff -m "your commit message"

    # Push your changes to your forked repository on Github
    git push
    ```

4. [Create the pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork) for your changes. InfluxData community template maintainers will review your changes and, upon approval, will merge them into this repository. Our goal is to review every submission within 5 business days.

In the review process, we verify that you provide a manifest file and a README.md with instructions for using the template. We reserve the right to reject or remove a template from this repository for any reason.

Once your template has been merged, start sharing it with the community! Link to it on Twitter, Reddit, or whatever social media you use. Let people on the [InfluxDB Community Slack](https://influxdata.com/slack) know about it too!

## Support

Community Influx Templates are provided by members of the community. Template authors are solely responsible for supporting their templates. InfluxData does not test contributed templates, nor guarantee their quality or safety. If you have questions about or need help with a specific template, please contact the template author using the contact information provided in the template README.

InfluxData provides and supports the `influx` command-line tool and `influx pkg` command for importing and exporting template manifests. For help with these tools, please join our [Community Slack](https://influxdata.com/slack) and ask for help in the `#community-support` channel.

[![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://www.influxdata.com/slack)
