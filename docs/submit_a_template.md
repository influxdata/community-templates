# Submit a Template

To contribute a new template or enhance an existing template, submit a pull request to this repository.

> Submissions must be provided under the [Apache Public License v2](https://www.apache.org/licenses/LICENSE-2.0).



1. [Fork this repo](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) on Github, and then clone it locally on your machine.
   ```
   git clone https://github.com/<your_github_name>/community-templates
   ```


2. Apply your changes to the clone repository on your local machine.


    * To submit and entirely new template, create a new directory for your template and create a `README.md` that describes your template and how to use it. See the `Example_README.md` file in this repository. **Be sure to include a way for users to get in contact with you**.

        Use the following command to export the template and generate a manifest file ([Influx pkg requires InfluxDB 2.0.0 beta or greater](https://portal.influxdata.com/downloads/)):

        ```
        influx pkg export --file ~/path/to/template/manifest.yml
        ```

        > Exported manifest files will be YAML or JSON. The filename extension you provide will determine the format used.

    * To update an existing template, make the changes to template files in the appropriate directory.

    > **Tip:** Replace any hard-coded URLs to InfluxDB in your Telegraf configurations with the `$INFLUX_URL` environment variable so users can easily point it to their own InfluxDB instance location. For example: `urls = ["$INFLUX_URL"]`

3. If you are submitting a new Template, add it to the table of Templates in the main `README.md` file in the root of the repository.

    * The table lists templates alphabetically, so add a new row in the appropriate location
    * Use a short but descriptive name for your Template in the first column
    * Link that name to your Template's directory
    * Add a short (one sentence) description of what your Template's use case in the second column
    * Add your name, either your real name, nickname or GitHub username to the last column

    Your row should look like this:
    ```
    | [Template Name](template-directory/) | This is a description of the Template | Your Name |
    ```

    > **Note:** Be sure to include the trailing `/` after your directory name.

4. Add and commit your changes and push them to Github. Include the `--signoff` flag when committing your changes to include your author information in the commit message.

    ```
    # Add your changes
    git add .

    # Commit your changes with a commit message
    git commit --signoff -m "your commit message"

    # Push your changes to your forked repository on Github
    git push
    ```

5. [Create the pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork) for your changes. InfluxData community template maintainers will review your changes and, upon approval, will merge them into this repository. Our goal is to review every submission within 5 business days.

In the review process, we verify that you provide a manifest file and a README.md with instructions for using the template. We reserve the right to reject or remove a template from this repository for any reason.

Once your template has been merged, start sharing it with the community! Link to it on Twitter, Reddit, or whatever social media you use. Let people on the [InfluxDB Community Slack](https://influxdata.com/slack) know about it too!


> Need help? You can find [support](../README.md#support) information at the bottom of the main page.
