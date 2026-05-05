name: Generate Doc - Weekly Update
description: This skill generates a weekly update summarising the work that has happened over the last week. It gathers information from various sources such as Github commits, Slack channels, and Notion databases to create a concise summary of updates across different teams. The update is then stored in a Notion page for easy access and reference.

> Before starting, read `product-context/COMPANY.md` for internal URLs, repository names, Slack channel names, and Notion links. Read `product-context/PRODUCTS.md` for team names and product details.

## How to Generate the Weekly Update

This skill generates a weekly update summarising the work that has happened over the last week. This is a weekly task that should be completed every Wednesday morning (9am London time), and should take no more than 30 minutes to complete. The updates should be generated from:

- Any commits related to new tags in the front-end apps repository on Github (see `product-context/COMPANY.md` for the repo name): these are shipped front-end bugs and features
- Any commits related to new tags in the Pro Editor repository on Github (see `product-context/COMPANY.md` for the repo name): these are shipped front-end bugs and features for the advanced editing experience
- Any posts in the shipped channel in Slack (see `product-context/COMPANY.md` for the channel name): these are shipped features and updates across the company
- Any deals posted by Hubspot in the customer success ops channel in Slack (see `product-context/COMPANY.md` for the channel name): these are new customers that have signed up
- Any items where the status has changed in the Notion Product Status database (see `product-context/COMPANY.md` for the URL) — particularly the Launch status and the Project status. You can get more details about each project from the one pager in the database inside that specific item's page. These items also contain metadata that tells you the product it relates to, which team owns the project, and other useful information to help you understand the context of the update.
  - Do not include items that are not yet planned, so don't have a Quarter assigned (Q2, Q3 etc) as these are still with the product team and don't need to be discussed more widely yet.

The timeframe of data to cover is the last 7 days.

Summarise the updates in a concise way and store it in the Weekly Updates Notion page (see `product-context/COMPANY.md` for the URL). You can see previous weekly updates there — simply add a new one to the list. The updates should be grouped by team (see `product-context/PRODUCTS.md` for team names) and what has been done/shipped, what is in discovery/what is coming up, and how things that are in progress are going (including items in design and in progress). The updates should be written in a way that is easy to understand for someone who is not familiar with the technical details of the work, but still provides enough information to give a clear picture of what has been happening across the company.

List all the sources referenced so it is clear where the data comes from, and link to the relevant pages or posts where possible.

If there are no tags in the front-end Github repos for the last 7 days, you should state that any features completed below have not yet been released to customers, but will be soon. If there has been a tag (e.g. v0.4.8), give a summary of the front-end releases that have been made that week and what they contained, in simple to understand language which explains the features and bugs clearly.
