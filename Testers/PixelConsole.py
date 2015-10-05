from Lib.graphics import *
from ThirdParty import SystemPlus
from ThirdParty import RandomEx
import traceback

PADDING = 16
PIXEL_SIZE = 2
WINDOW_SIZE_X = 500
WINDOW_SIZE_Y = 500
AUTO_FLUSH = True

class PixelConsole(object):

    def testRun(self):
        colors = ["white", "green", "blue", "red"]
        for j in range( PADDING, WINDOW_SIZE_Y - PADDING, PIXEL_SIZE ):
            for i in range( PADDING, WINDOW_SIZE_X - PADDING, PIXEL_SIZE ):
                self.drawRectangle( i, j, colors[ RandomEx.r.randomInt(0,3) ] )
        for j in range(0,PIXEL_SIZE * 4,PIXEL_SIZE):
            for i in range( PADDING, 100, PIXEL_SIZE * 4):
                self.drawRectangle( i+j, i+j, colors[ int(j/PIXEL_SIZE) ] )
        if AUTO_FLUSH is False:
            self.win.flush()

    def __init__(self):
        self.win = None

    # $ Open up a "console", which show letter's in colored pixels
    def open(self):
        self.win = GraphWin("Pixel Console", WINDOW_SIZE_X, WINDOW_SIZE_Y, AUTO_FLUSH)
        self.win.setBackground( "black")

    # $ Started to receive and produce information
    def run(self):
        # [] Stop any false command from breaking the program
        try:
            # * Pause the system, waiting for a mouse click
            self.testRun()
            self.win.getMouse()
        except Exception:
            SystemPlus.consolePrintL(traceback.format_exc())
            SystemPlus.consolePrintL( "You can still continue with the terminal:")
            SystemPlus.consolePrintL( "///////////////////////////////////////////////")

    # $ Close the "console"
    def close(self):
        self.win.close()

    # $ Draw a rectangle on the screen with a specific color
    def drawRectangle(self, x, y, color):
        c = Rectangle( Point( x, y ), Point( x + PIXEL_SIZE - 1, y + PIXEL_SIZE - 1) )
        c.setOutline( color )
        c.setFill( color )
        c.draw( self.win )

    # $ Draw a point on the screen with a specific color
    def drawPoint(self, x, y, color):
        c = Point( x, y )
        c.setOutline( color )
        c.draw( self.win )

