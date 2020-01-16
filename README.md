# Influx Community Templates

InfluxDB 2.0 introduces a new `pkg` command which lets you export your entire configuration, from dashboards to Telegraf scripts to notifications and alters, as a single YAML manifest file, and then re-load those configurations into a fresh instance of InfluxDB. Not only is this useful for backing up your own deployment setup, but it also allows you to create reusable templates for common setups, such as monitoring a service or network traffic, that can be quickly deployed by you or others. 

In true Open Source spirit, these templates of common use cases can be shared with other users of InfluxDB, so they can get started faster, using known-good configurations, and contribute their own improvements to those templates that will benefit the originaly author and the wider community.

The purpose of this site is to promote the creation, sharing, and reuse of templates among the InfluxDB community. Anybody can use these templates in their own InfluxDB instance, and submit improvements or entirely new templates.

## Using a Template

* Template manifest YAML files
* Loading into an Influx instance with `influx pkg -f`
* Telegraf & Kapacitor scripts

Each template will provide a manifest YAML file, in addition to instructions specific to it's use. Using a template always startes with importing the template, which you can do with the following command:

```
 influx pkg --org $INFLUX_ORG -file ~/path/to/template/manifest.yml
 ```

This will import the specified `manifest.yml` into an instance of InfluxDB running on `localhost`. 

If you don't want to download the manifest file locally, you can point to its remote location using the `--url` flag, for example:
```
 influx pkg --org $INFLUX_ORG --url https://raw.githubusercontent.com/influxdata/community-templates/master/template/manifest.yml
 ```

### Using Templates in the Cloud

If your instance is not on localhost, say it's running on your own servers or you are using the InfluxDB Cloud service, you can specify the remote location with the `--host` flag. In that case you will also need to provide an authentication token to make changes to the remote instance:
```
 influx pkg --org $INFLUX_ORG --file ~/path/to/template/manifest.yml --host <hostname> --token <token>
```

> Need help? You can find [support](#support) information at the bottom of this page.

## Submitting a Template

> Submissions must be provided under the Apache Public License v2.


If you have an InfluxDB configuration that you want to contribute as a template, or enhancements to an existing template that you want to share, you can do so by submitting a pull request to this repository.

The first step, if you haven't already, is to [fork this repo](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) on Github, and then clone it locally on your computer or development environment.

If you are updating an existing template, you can now apply your changes directly to the manifest file and README in that template's directory. If you are adding a new template you will need to create a new directory, giving it a descriptive name for your template.

You can export your current configuration as a template manifest with the following command:

```
influx pkg export > ~/path/to/template/manifest.yml
```

Next you will need to create or update the README for your template. Because every template's usage is different, and each one will have different steps and parameters needed to get it fully operational, it's important that you clearly and fully document the process for users. If you are creating a new README, start by copying the `Example_README.md` into your template directory as `README.md` and then filling out each of the defined sections.

> Be sure to include a way for users to get in contact with you if they need help! This can be an email address, Slack username, or Github account.

Once your additions are ready, it's time to submit them! With Git, you start by calling `git add` on any files you created or changed. At a minimum this should be your `README.md` and `manifest.yml` files. You can add everything for your template with:

```
git add ~/path/to/template/*
```

Next you will commit those changes to your local Git checkout. When prompted, use the commit message to describe what changes you've made, or what the use-case for your template is if you are adding a new one.

```
git commit --signoff
```

Be sure to include the `--signoff` flag to add your author information to the commit message.

Now it's time to send your changes to Github. You will push them to your fork of the repository first, and from there you will be able to create a pull request to have it added to this one.

```
git push
```

Your last step is to [create the pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork) for your changes. This will send them to the Influx Data community templates maintainers, who will review the submission and either merge it into this repository, or ask you for more information or changes if needed.

Once your template has been merged, you can start sharing it with the community! Link to it on Twitter, Reddit, or whatever social media you use. And let people on the [InfluxDB Community Slack](https://influxdata.com/slack) know about it too!

## Support

The InfluxDB Community Templates are provided by members of the community, who are solely responsible for their content and supporting them. InfluxData does not test contributed templates, nor guarantees their quality or safety. If you have questions or need help with the use a specific template, please contact that template's author using the contact information they provide in the README of the template.

InfluxData provides and supports the `influx` command-line tool and `influx pkg` command for importing and exporting template manifests. For help with these tools, please join our [Community Slack](https://influxdata.com/slack) and ask for help in the `#community-support` channel.