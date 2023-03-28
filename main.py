import discord
import os
import time
import logging
from discord.ext import tasks

# for webscraping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# for generating random color
import random
import randomcolor
from PIL import Image
import colorsys

TOKEN='YOUR-TOKEN-HERE'

g = XXX #guild | insert your guild number, for e.g -> g = 1238761326312
ch = XXX #channel | insert your channel number, for e.g -> ch = 3128132132

intents = discord.Intents.default()
intents.message_content = True

# set the path and the name for the temporary PNG image of the color
filepath = "C:/Users/diana/Desktop/ITPMA Master/Anul2/CC4/Pamtone"
tempname = "temp_img.png"
filepath = filepath + tempname

# set catchphrases for loading time
loading_text = ["Mhmmm, let's see...","I bet you've never heard of this one before.", "Do you know this one?", 
                "Let me think, what new colors are there?", "I have updates for you...",
                "Allow me to find a color made especially just for you"]


def generate_color():

    global color_hex
    # generate a random color and get its hex number. the output is a list, and we need a string  
    color_hex = randomcolor.RandomColor().generate()

    # create an empty string and convert the list to string
    color_string= ''

    for x in color_hex:
        color_string +=''+ x
        color_hex = color_string # this is just a string for e.g #ab2f42

    return color_hex


def get_color_info(color_hex):

    global color_name
    global r, g ,b

    web = 'https://chir.ag/projects/name-that-color/'

    # to create the complete website url joing the web link with the color_hex 
    url = web + color_hex # it should be something like https://chir.ag/projects/name-that-color/#ab2f42
    
    # Use a headless browser to simulate a web browser without opening a window
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    # Wait for the color name element to appear before getting its text
    color_name_element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, 'colorname'))
    )
            
    color_name = color_name_element.text
            
    # Get the RGB values
    color_rgb_element = WebDriverWait(driver, 0.01).until(
        EC.presence_of_element_located((By.ID, 'colorrgb')) #for eg color_rgb_element = RGB: 125, 239, 110
    )
        
    color_rgb = color_rgb_element.text[4:] #parse only the tuple of RGB values; for eg: "125, 239, 110"
            
    # split and convert the string into list and then convert each item of the list in int numbers for R,G,B values
    color_rgb = color_rgb.split(',')
    r = int(color_rgb[0])
    g = int(color_rgb[1])
    b = int(color_rgb[2])
        
    # create image with RGB values
    img = Image.new('RGB', (300, 200), (r,g,b))
            
    # temporarily save the image to the path
    img.save(filepath)

    # Remove the approx. or solid. substring from the color name text
    color_name = color_name.replace("approx.","").replace("solid.","")

    # Close the browser
    driver.quit()

def generate_random_blue():
    # Set the hue to a random value in the blue range (200-260)
    h = random.randint(200, 260)
    # Set the saturation to a random value (50-100)
    s = random.randint(50, 100)
    # Set the value to a random value (50-100)
    v = random.randint(50, 100)
    # Convert the HSV color to RGB color | Hue: 0-360 degree -> 0.0-1.0; Saturation: 0-100% -> 0.0-1.0; Value: 0-100% -> 0.0-1.0
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h/360, s/100, v/100))
     # Convert RGB color to hex code
    blue_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return blue_hex

def generate_random_red():
    # Set hue to a random value in the range of red colors
    h = random.uniform(0, 10)/360 + random.uniform(0, 3)/360
    # Set saturation to a random value between 50% and 100%
    s = random.uniform(50, 100) / 100
    # Set value to a random value between 50% and 100%
    v = random.uniform(50, 100) / 100
    # Convert HSV color to RGB color
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
    # Convert RGB color to hex code
    red_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return red_hex

def generate_random_orange():
    # Set hue to a random value in the range of orange colors
    h = random.uniform(10, 40)/360 + random.uniform(0, 10)/360
    # Set saturation to a random value between 50% and 100%
    s = random.uniform(50, 100) / 100
    # Set value to a random value between 50% and 100%
    v = random.uniform(50, 100) / 100
    # Convert HSV color to RGB color
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
    # Convert RGB color to hex code
    orange_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return orange_hex

def generate_random_purple():
    # Generate a random hue value in the range 280 to 320 degrees
    h = random.uniform(255, 280) / 360
    # Set saturation and value to 100%
    s = random.uniform(0.5, 1.0)
    v = random.uniform(0.7, 1.0)
    # Convert HSV to RGB
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
    # Convert RGB to hex code
    purple_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return purple_hex

def generate_random_pink():
    # Generate a random hue value in the range 280 to 320 degrees
    h = random.uniform(290, 340) / 360
    # Set saturation and value to 100%
    s = random.uniform(0.5, 1.0)
    v = random.uniform(0.7, 1.0)
    # Convert HSV to RGB
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
    # Convert RGB to hex code
    pink_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return pink_hex

def generate_random_yellow():
    # Generate a random hue value in the range 50 to 60 degrees
    h = random.uniform(50, 60) / 360
    # Set saturation and value to 100%
    s = random.uniform(0.5, 1.0)
    v = random.uniform(0.7, 1.0)
    # Convert HSV to RGB
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
    # Convert RGB to hex code
    yellow_hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return yellow_hex

def generate_random_green():
    # Hue values for green range from approximately 90 to 180 degrees
    h = random.uniform(90, 180)/360 + random.uniform(-5, 5)/360
    s = random.uniform(50, 100) / 100
    v = random.uniform(50, 100) / 100
    r, g, b = tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))
    green_hex = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return green_hex


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
        # if somebody types /color, the bot responds
        if message.content == '/color':

            await message.channel.send(loading_text[random.randint(0,5)])   # have the bot reply with one of the loading catchphrases   
            
            generate_color()
            get_color_info(color_hex)

            # send message and image on Discord server
            await message.channel.send(f"{color_name} or {color_hex}")
            await message.channel.send(file=discord.File(filepath))  #send image
            
            # delete the image after x seconds
            time.sleep(1)
            os.remove(filepath)   
        
        if message.content == '/blue':
            
            await message.channel.send("Let me think of a blue color for you...")

            blue_shade = generate_random_blue()
            get_color_info(blue_shade)

            # send message and image on Discord server
            await message.channel.send(f"There are many shades of blue color, for example {color_name} or {blue_shade}")
            await message.channel.send(file=discord.File(filepath))  #send image
            
            # delete the image after x seconds
            time.sleep(1)
            os.remove(filepath)

        if message.content == '/green':
            
            await message.channel.send("Let me think of a green color for you...")

            green_shade = generate_random_green()
            get_color_info(green_shade)

            # send message and image on Discord server
            await message.channel.send(f"There are many shades of green color, for example {color_name} or {green_shade}")
            await message.channel.send(file=discord.File(filepath))  #send image
            
            # delete the image after x seconds
            time.sleep(1)
            os.remove(filepath)
        
        if message.content == '/red':
            
            await message.channel.send("Let me think of a red color for you...")

            red_shade = generate_random_red()
            get_color_info(red_shade)

            # send message and image on Discord server
            await message.channel.send(f"There are many shades of red color, for example {color_name} or {red_shade}")
            await message.channel.send(file=discord.File(filepath))  #send image
            
            # delete the image after x seconds
            time.sleep(1)
            os.remove(filepath)

        if message.content == '/yellow':
            
            await message.channel.send("Let me think of a yellow color for you...")

            yellow_shade = generate_random_yellow()
            get_color_info(yellow_shade)

            # send message and image on Discord server
            await message.channel.send(f"There are many shades of yellow color, for example {color_name} or {yellow_shade}")
            await message.channel.send(file=discord.File(filepath))  #send image
            
            # delete the image after x seconds
            time.sleep(1)
            os.remove(filepath)

        if message.content == '/purple':
            
            await message.channel.send("Let me think of a purple color for you...")

            purple_shade = generate_random_purple()
            get_color_info(purple_shade)

            # send message and image on Discord server
            await message.channel.send(f"There are many shades of purple color, for example {color_name} or {purple_shade}")
            await message.channel.send(file=discord.File(filepath))  #send image
            
            # delete the image after x seconds
            time.sleep(1)
            os.remove(filepath)

        if message.content == '/orange':
            
            await message.channel.send("Let me think of a orange color for you...")

            orange_shade = generate_random_orange()
            get_color_info(orange_shade)

            # send message and image on Discord server
            await message.channel.send(f"There are many shades of orange color, for example {color_name} or {orange_shade}")
            await message.channel.send(file=discord.File(filepath))  #send image
            
            # delete the image after x seconds
            time.sleep(1)
            os.remove(filepath)
        
        if message.content == '/pink':
            
            await message.channel.send("Let me think of a pink color for you...")

            pink_shade = generate_random_pink()
            get_color_info(pink_shade)

            # send message and image on Discord server
            await message.channel.send(f"There are many shades of pink color, for example {color_name} or {pink_shade}")
            await message.channel.send(file=discord.File(filepath))  #send image
            
            # delete the image after x seconds
            time.sleep(1)
            os.remove(filepath)
        
        if message.content == "/help":
            with open("help.txt", "r") as f:
                help_text = f.read()
            await message.author.send(help_text) # private text sent by bot
            await message.author.send("Pssst, you can also chat with me in private :shushing_face: :spy: :wink:")
            await message.channel.send(help_text) # text send on the channel
            
            

client = MyClient(intents=intents)

@client.event
async def on_ready():
    logging.info(f'{client.user} has connected to Discord!')
    print("Bot connected to the server!")
    channel = client.get_guild(g).get_channel(ch)
    await channel.send("Are you ready to become the world's finest color connoisseur?")
    await myLoop.start()

@tasks.loop(seconds = 3600) # repeat every hour
async def myLoop():
    await client.wait_until_ready()
    channel = client.get_guild(g).get_channel(ch)

    generate_color()
    get_color_info(color_hex)

    # send message and image on Discord server
    await channel.send(f"The new color of the moment is {color_name} or {color_hex}")
    await channel.send(file=discord.File(filepath))  #send image
            
    # delete the image after x seconds
    time.sleep(1)
    os.remove(filepath)    

client.run(TOKEN)