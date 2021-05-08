<h1 align=center> Pi Bot - α</h1>
<p>
Welcome to π bot, it is the will be an all-purpose bot for competative programming, github and other stuff.

**NOTE**- For now the github integration is at hold, mainly focus is on [codeforces](https://codeforces.com).

</p>

To know more about bot commands visit [Command Docs](docs/COMMAND.md)

<h2> How to test the bot before running it on your server</h2>

To test the bot join the [Support Server](https://discord.gg/FjVVkTtbgp). And head over to the **\#playground**

## How to run the bot on your own server

[Invite the bot to your server](https://discordapp.com/oauth2/authorize?&client_id=833191736335400970&scope=bot)
[_NOTE- While uing the bot if you find any issue or bug please head over to the [issue](https://github.com/pvcodes/pi_bot/issues) and create an new issue elaborating the issue_]

[NOTE- The music cog is not yet setup in the hosted bot]

## Hosting the bot locally:

**NOTE**: To replicate this bot, you will need a bot **token**. Go get yours at https://discord.com/developers/ (If you need help with this step, feel free to ask for help in our [Support Server](https://discord.gg/FjVVkTtbgp)

- Clone this repo using `git clone`
- cd into the bot folder.
- Add the token in a `.env` file in the project root as follows:

```text
DISCORD_BOT_TOKEN=<your token>
```

- Install the `pipenv` via `pip install pipenv` and then run:

```
pipenv install
```

### [Optional] For having contest reminder command working locally, you will need a login in [Google Cloud Platform](https://console.cloud.google.com/) and perform these steps:

- Get an Google Calander API
- Get the `credentials.json` from &nbsp; `APIs and services -> Credentials` &nbsp; click on CREATE CREDENTIALS and follow required steps
- Copy and paste `credentials.json` file to [src](/src) folder 

### [Optional] For having music stuff working (make sure you have [JVM](https://www.java.com/en/download/) working), Follow these:

- Run the command `java -jar Lavalink.jar`


- Enjoy! (don't forget to add your own bot into your discord server by generating an invite link from the discord developers application page in [OAuth2 section](https://discord.com/developers/applications/) and choose application and check Oauth2 section)
- You may do bug-reporting or ask for help in on the SupportServer... or just open an issue on this repo.

<b>Note: </b>If you get `module not found error`, try to run `pip install -r requirenment.txt`

## How to contribute

Before contributing, here is some information that might help your **PR (Pull Request)** get merged.

### How to set up the development environment

Requirements:

- git
- pip
- python `3.8.6` or higher

1. Fork and clone the repository with `git clone https://github.com/<your-username>/pi_bot`
2. Get to the clone directory using the command `cd pi_bot`
3. Copy the contents of the `.env.sample` file into a new file - `.env` and add your DISCORD bot token in there.
4. Now follow these steps

   (Requires [pipenv](https://pipenv.pypa.io/en/latest/))
   \- Install pipenv\
   \- Run `pipenv sync --dev` to install project dependencies and development dependencies\
   \- Run `pipenv run start` to run the bot.\
   \- For downloading more libraries, use `pipenv install <package-name>`\
   \- If you're adding any development-dependencies, use-> `pipenv install <package-name> --dev`\

### To contribute changes follow these steps:

**Note**: Make sure you have been assigned the issue to which you are making a PR. If you make PR before being assigned, It will be labeled invalid and closed without merging.

1. Add a upstream link to main branch in your cloned repo

```
git remote add upstream https://github.com/pvcodes/pi_bot.git
```

2. Keep your cloned repo upto date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)

```
git pull upstream master
```

3. Create your feature branch

```
git checkout -b <feature-name>
```

4. Commit all the changes

```
git commit -am "Meaningful commit message"
```

5. Push the changes for review

```
git push origin <branch-name>
```

6. Create a PR from our repo on Github.

### How to report a bug

Submit an issue on GitHub and add as much information as you can about the bug, with screenshots of inputs to the bot and bot response if possible (if the issue is regarding bugs).

**Note**: For more detailed information about how to contribute, please refere to the [CONTRIBUTING.md](docs/CONTRIBUTING.md) file.

## Requirements:

- python 3
- discord(rewrite branch)
- python-dotenv
- requests
- wavelink
</p>

<div align="center">
<a href="docs/LICENSE.md"><img src="https://img.shields.io/github/license/Vyvy-vi/TearDrops?style=flat-square" alt="MIT license"></a>
<a href="https://github.com/Rapptz/discord.py/releases/tag/v1.5.0"><img src="https://img.shields.io/badge/discord.py-v1.6.0-7289da.svg?style=flat-square" alt="discord.py version"></a>
</div>
