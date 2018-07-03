# NaiveBot

NaiveBot is a simple Telegram bot engine based on Flask and Gunicorn.

## Usage

Before using, you need to install Flask and Gunicorn, and set the configuration file of NaiveBot.

The configuration is in the file `naivebot/config.py`.

Then, import the package to a `.py` file you wanted to import to, like that `import naivebot`.

**DO NOT IMPORT THE MODULES IN THE PACKAGE DIRECTLY**

And then, define a global variable named 'application' and initialize it as `naivebot.application`,

and decorate the entry function (has 1 argument) with the decorator `naivebot.entry`.

Finally, use the command `gunicorn [options] <your-file>` (not `naivebot.server`) to start your server.
