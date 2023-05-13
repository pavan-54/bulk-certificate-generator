import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os
from dotenv import load_dotenv

load_dotenv()

df = pd.read_excel(os.getenv('STUDENTS_FILE'))


def generate_certificate(name):
    # Load the certificate template
    img = Image.open(os.getenv('CERTIFICATE_FILE'))

    # Create a draw object for the image
    draw = ImageDraw.Draw(img)

    # Set the font and size of the text
    font = ImageFont.truetype(os.getenv('FONT_FILE'),int(os.getenv('FONT_SIZE')))

    size = img.size

    # Calculate the coordinates of the text box
    x = (size[0] - font.getsize(name)[0]) // 2
    y = (size[1] - font.getsize(name)[1]) // 2

    x=x-int(os.getenv('X_REDUCTION_FACTOR'))
    y=y-int(os.getenv('Y_REDUCTION_FACTOR'))

    # Draw the text box
    draw.rectangle((x, y, x + font.getsize(name)[0], y + font.getsize(name)[1]), fill="white")

    # Draw the name of the participant in the text box
    draw.text((x + 10, y + 10), name, font=font, fill=os.getenv('TEXT_COLOUR','black'))

    # Save the certificate
    img.save(f"certificates/{name}.pdf")


for i, row in df.iterrows():

    name = row["name"]

    # Generate the certificate
    generate_certificate(name)

print("Certificates generated successfully!")