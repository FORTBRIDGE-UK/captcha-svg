import sys
import os
import time
import cairosvg
from PIL import Image
import pytesseract
import io


sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', 'bced6d104eed4997fe3751685e7308c5')

solver = TwoCaptcha(api_key)


# Step 1: Convert SVG to PNG (in-memory)
with open("./svg.svg", "rb") as svg_file:
    svg_data = svg_file.read()

#channge the backround to white, to make the image more clear!
png_data = cairosvg.svg2png(url='./svg.svg', write_to='./temp.png', background_color='white')

  
attempts = 1000
for i in range(attempts):
    try:
        result = solver.normal('./temp.png')
        print("result e", result)
        sys.exit('solved: ' + str(result))
    except Exception as e:
        print(f"Attempt {i+1} failed with error: {e}")
        time.sleep(1)  # optional delay between retries
else:
    sys.exit("All attempts failed.")
