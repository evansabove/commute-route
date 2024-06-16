from PIL import Image, ImageFont, ImageDraw
from inky.auto import auto

class ScreenWriter:
    inky_display = auto()

    def __init__(self):
        self.inky_display = auto()

    def show_route(self, route, duration, at_time):
        img = Image.new("P", (self.inky_display.WIDTH, self.inky_display.HEIGHT))
        draw = ImageDraw.Draw(img)

        font_xs = self.get_font(15)
        font_sm = self.get_font(20)
        font_lg = self.get_font(40)

        draw.text((0, 0), f'{at_time. strftime("%a %d %b at %H:%M")}', self.inky_display.BLACK, font_xs)
        draw.text((0, 30), 'Go via', self.inky_display.BLACK, font_xs)
        draw.text((0, 40), route, self.inky_display.BLACK, font_lg)
        draw.text((0, 90), f'{duration} mins', self.inky_display.BLACK, font_sm)

        self.inky_display.set_image(img)
        self.inky_display.show()
    
    def get_font(self, size):
        return ImageFont.truetype('/home/andy/commute-route/Roboto-Medium.ttf', size) #change this