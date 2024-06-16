from PIL import Image, ImageFont, ImageDraw
from inky.auto import auto

class ScreenWriter:
    inky_display = auto()

    def __init__(self):
        self.inky_display = auto()

    def show_route(self, route, duration, at_time):
        img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        font = self.get_font(20)

        draw.text((0, 0), f'At {at_time}', self.inky_display.BLACK, font)
        draw.text((0, 30), f'Use {route}', self.inky_display.BLACK, font)
        draw.text((0, 60), f'{duration} mins', self.inky_display.BLACK, font)

        self.inky_display.set_image(img)
        self.inky_display.show()
    
    def get_font(self, size):
        return ImageFont.truetype('/home/andy/commute-route/Roboto-Medium.ttf', size) #change this