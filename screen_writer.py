from PIL import Image, ImageFont, ImageDraw
from inky.auto import auto

class ScreenWriter:
    inky_display = auto()

    def __init__(self):
        self.inky_display = auto()

    def show_route(self, text):
        img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        font = self.get_font(50)
        width, height = font.getsize(text)

        x = (self.inky_display.WIDTH / 2) - (width / 2)
        y = (self.inky_display.HEIGHT / 2) - (height / 2)

        draw.text((x, y), text, self.inky_display.BLACK, font)
    
    def get_font(self, size):
        return ImageFont.truetype('/home/andy/commute-route/Roboto-Medium.ttf', size) #change this