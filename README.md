# poetrysgbot

PoetrySG bot is a Twitter bot that tweets quotes from Singaporean poets every 6 hours. You can find it at twitter.com/poetrysgbot.

## Why PoetrySGBot?

I'm a big fan of literary bots like @VitaVirginiaBot and @carsonbot that inject a bit of poetry and magic into the endless doomscrolling. Inspired by them, I wanted to make a bot that showcased Singaporean poets (I am Singaporean). I started out with a different bot that just tweeted one poet. Now, with support from the fine folks at poetry.sg and SingLitStation, this bot runs off a spreadsheet of quotes from 70+ poets.

## How PoetrySGBot?

PoetrySGBot is written in Python and runs on Heroku.

I primarily followed this tutorial: https://dev.to/emcain/how-to-set-up-a-twitter-bot-with-python-and-heroku-1n39
And drew some inspiration from this tutorial: http://www.adamhammond.com/botguide/

I used Heroku Scheduler to schedule tweet times. I also wrote a script (charCheck.py) to check that the formatted quotes are below 280 characters, which is the maximum tweet length.

## How to use PoetrySGBot?

I would love for people to use PoetrySGBot to make their own literary Twitter bots, especially for their own country's poets!

Using the code should be pretty straightforward - just replace quotes.csv with a CSV file containing the quotes you want to use. You can adjust the way the quotes are formatted in the file getquotes.py. Also, when setting it up in Heroku, don't forget to set the environment variables to reflect your own access tokens for the Twitter API.

Feel free to email me at michelle.lee0896@gmail.com or DM at twitter.com/unselving if you have any questions.
