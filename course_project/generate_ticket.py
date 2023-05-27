from io import BytesIO

import requests
from PIL import Image, ImageDraw, ImageFont

TEMPLATE_PATH = 'files/ticket_base.png'
FONT_PATH = 'files/Roboto-Regular.ttf'
FONT_SIZE = 25

URL = 'https://sun9-52.userapi.com/impg/D72JNYsLUWjlFgHncNxIPCbhjabgYOere6cLmw/_U_o7PILvWY.jpg?size=165x138&quality=95&sign=8abd67a7090606a25c4a6e0f2561b971&type=album/PL2eUSUrUbk.jpg?size=1080x1181&quality=95&sign=b4b9f78a05cf61b53d7738ef3c110ae6&type=album'
BLACK_COLOR = (0, 0, 0, 255)
NAME_OFFSET = (480, 440)
EMAIL_OFFSET = (480, 490)

AVATAR_OFFSET = (150, 410)


def generate_ticket(name, email):
    base = Image.open(TEMPLATE_PATH).convert('RGBA')
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    draw = ImageDraw.Draw(base)
    draw.text(NAME_OFFSET, name, font=font, fill=BLACK_COLOR)
    draw.text(EMAIL_OFFSET, email, font=font, fill=BLACK_COLOR)

    response = requests.get(url=URL)
    avatar_like_file = BytesIO(response.content)
    avatar = Image.open(avatar_like_file)

    base.paste(avatar, AVATAR_OFFSET)

    temp_file = BytesIO()
    base.save(temp_file, 'png')
    temp_file.seek(0)

    return temp_file


if __name__ == '__main__':
    generate_ticket('name', 'email')
