# Build a scheduler Slack bot!

Build a Slack bot slash command that adds events to your personal calendar!

```
/scheduleme "Chocolate chip cookie competition" "Sunday at 2pm" "Sunday at 4pm"
```

Slack bots are fun ways to add new functionality into your Slack workspace. Using the Nylas API, you can create a bot  
with email, contacts or calendar functionality. In this tutorial, you are going to create a scheduler bot that adds 
events to your personal calendar with a simple Slack slash command. We’ll dive into the nitty gritty of how to build a 
Slack bot from scratch. 

#### Checkout [this post](https://www.nylas.com/blog/build-a-slack-bot-scheduler-in-30-minutes) for the full instructions!

## What You’ll Need Beforehand

There are a few technologies that we need to have in place before we embark on this DIY Slack bot journey!

- Git and Github account
- Heroku account
- Slack workspace
- An email address associated with a Google, iCloud, or Microsoft calendar
- A text editor of your choosing — PyCharm, Atom, Vim, Sublime, etc.



# Overview
### Part 0: Basic app setup
TLDR; Fork the starter code, run the setup script and run the app locally

### Part 1: Hook your repo up to Heroku and deploy it
TLDR; Create a Heroku app, hook it up to your Github repo, deploy it

### Part 2: Set up Heroku config variables
TLDR; Auth an account with Nylas to get the access token, use this to get the ID of the calendar, add these plus the calendar timezone as config variables in Heroku.

### Part 3: Connect your app to your Slack workspace
TLDR; Create a Slack App and configure a slash command to communicate with your app, add a route in your app that listens for the slash command 

### Part 4: Add text parsing functionality
TLDR; Parse the text sent from Slack into meaningful components for an event

### Part 5: Build scheduling functionality
TLDR; Send the parsed arguments to the /events endpoint of the Nylas API to create an event on your calendar.
  
