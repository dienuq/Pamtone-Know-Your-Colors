# Pamtone
 A discord bot with a PhD in colors.

"Know-Your-Colors" is a Discord bot whose only purpose is to help you broaden your color knowledge.

It will generate and send you a random color name, its hex code and a picture with the actual color.

Use /help to see the whole commands list.

Huge thanks to Chirag Mehta for creating this website: https://chir.ag/projects/name-that-color

How this works:
1. The bot generates a random hexcolor
2. Accesses Chirag Mehta's website to get the name of the color and RGB value
4. Generates an image with the color
5. Temporarily saves the image
6. Send all the info to Discord (Color name, Hex Code and picture)
7. Deletes the image

How to use this:
1. Clone the git repo
2. Create a virtual environment
3. Install all the libraries
4. Replace "TOKEN" with your discord token
5. Replace "guild" and "channel" with your discord server info
6. Replace filepath
7. Add the bot to your server
8. Run "main.py"

Possible issues and how to fix:
If the bot is not sending any image, modify line 72 in main.py. 
WebDriverWait is by default 2 seconds, but maybe it takes more time for the page to load, so increase that number.