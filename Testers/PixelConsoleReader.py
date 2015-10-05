
from PIL import ImageGrab

class PixelConsoleReader(object):

    # $ Capture a screen-shot and get a color of a pixel
    def getScreenShot(self):
        image = ImageGrab.grab()
        image.save("screen_capture.bmp", "BMP")
        rgb = image.getpixel((0,0))
        return rgb

        # c = Rectangle(Point(200,200), Point(300,300))
        # color = color_rgb( rgb[0], rgb[1], rgb[2] )
        # print( color )
        # c.setOutline( color )
        # c.draw(self.win)