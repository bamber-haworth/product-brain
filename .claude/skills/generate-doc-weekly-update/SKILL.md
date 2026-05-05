name: Generate Doc - Weekly Update
description: This skill generates a weekly update summarising the work that has happened over the last week. It gathers information from various sources such as Github commits, Slack channels, and Notion databases to create a concise summary of updates across different teams. The update is then stored in a Notion page for easy access and reference.

> Before starting, read `product-context/COMPANY.md` for internal URLs, repository names, Slack channel names, and Notion links. Read `product-context/PRODUCTS.md` for team names and product details.

## How to Generate the Weekly Update

This skill generates a weekly update summarising the work that has happened over the last week. This is a weekly task that should be completed every Wednesday morning (9am London time), and should take no more than 30 minutes to complete. Read `product-context/COMPANY.md` for the full list of data sources (GitHub repositories, Slack channels, Notion URLs). Each entry has a comment explaining what content it contains. The updates should be generated from:

- **GitHub**: for each repository listed in `product-context/COMPANY.md`, check for new tags in the last 7 days. The comment next to each repo explains what shipped content those tags represent.
- **Slack**: for each channel listed in `product-context/COMPANY.md`, check for relevant posts. The comment explains what is posted there.
- **Notion**: check the Product Status database (URL in `product-context/COMPANY.md`) for items where the Launch status or Project status has changed. Fetch the one pager inside each item's page for fuller context on the project, team, and product area.
  - Do not include items that are not yet planned — i.e. those without a Quarter assigned (Q2, Q3 etc), as these are still in product discovery and not ready for wider visibility.

The timeframe of data to cover is the last 7 days.

Summarise the updates in a concise way and store it in the Weekly Updates Notion page (URL in `product-context/COMPANY.md`). You can see previous weekly updates there — simply add a new one to the list. The updates should be grouped by team (see `product-context/PRODUCTS.md` for team names) and what has been done/shipped, what is in discovery/what is coming up, and how things that are in progress are going (including items in design and in progress). The updates should be written in a way that is easy to understand for someone who is not familiar with the technical details of the work, but still provides enough information to give a clear picture of what has been happening across the company.

List all the sources referenced so it is clear where the data comes from, and link to the relevant pages or posts where possible.

If there are no tags in the front-end Github repos for the last 7 days, you should state that any features completed below have not yet been released to customers, but will be soon. If there has been a tag (e.g. v0.4.8), give a summary of the front-end releases that have been made that week and what they contained, in simple to understand language which explains the features and bugs clearly.
