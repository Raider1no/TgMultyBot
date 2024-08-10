# Intro
This is a bot for telegram, that can chat with users, create images using any SD3 midel, create songs with Suno or image_to_video with Kling and even knows weather in any city.
# Get Started
## Installation
1) Bot uses [python 3.12](https://www.python.org/downloads/release/python-3120/)
2) Install requirements from requirements.txt:
   ```
   pip install -r requirements.txt
   ```
3) Now go to api_keys.py and change it with your api keys.
## How To Use
Once you created your Bot with BotFather - you ready to go! Try type /help to your bot.
If u reply on bot message or tag it with @ - bot will answer you using Gemini API.
If bot sees any voice message - this message will be translated in text automatically.
All commands can be found(and chanched as you wish) in [main](main.py) file.
## Base commands
This is list of commands that you already can use:
> /help - to get desc. of how to use chatBot and some commands  
> /weather (city) - to get actual weather in any city. If you didn't type any city it will return weather in Krasnodar =)  
> /img_to_video (prompt) - this command requires Kling cookie and creates 5 sec video from last picture bot saw.  
> /song (prompt) - this command requires Suno cookie and creates 2 songs from your prompt.  
> /image (prompt) - Creates an image with Swarm UI(must be opened).  
