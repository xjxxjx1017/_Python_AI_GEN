from Lib.graphics import *
from ThirdParty import SystemPlus
from ThirdParty import RandomEx
import traceback

PADDING = 16
PIXEL_SIZE = 8
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


    def testRun2(self):
        words = """Hello world!
This is my home, welcome to the new fancy world!
Lovely place, lovely grace.
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Hello world!
Hi there!
Good morning!
Good night!
"""
        words = words.lower()
        colors = []
        # * Convert letters to pixels
        for l in words:
            colors += self.letter2color(l)
        # * Draw pixels (sentence) on the screen :)
        # {} Start the loop
        countW = int( ( WINDOW_SIZE_X - PADDING * 2 ) / PIXEL_SIZE )
        countH = int( ( WINDOW_SIZE_Y - PADDING * 2 ) / PIXEL_SIZE )
        # * Count for the color index
        index = -1
        breakCount = 0
        for j in range( 0, countH ):
            for i in range( 0, countW ):
                # * Break again if needed
                if breakCount > 0:
                    breakCount -= 1
                    break
                # # Calculate the position for pixels
                W = PADDING + i * PIXEL_SIZE
                H = PADDING + j * PIXEL_SIZE
                # * Go to the next color
                index += 1
                # ? If there're more colors to print
                if index < len( colors ):
                    # * Print the color
                    self.drawRectangle( W, H, colors[ index ] )
                    # ? If the color is white
                    if colors[index] == 'white':
                        # * Go to the next line and leave a blank line
                        breakCount += 1
                        break
                else:
                    break
        # * Refresh the screen
        if AUTO_FLUSH is False:
            self.win.flush()


    def letter2color(self, letter):
        m = {}
        # * Symbolic colors for symbols
        m['\n'] = ['black', 'white']
        m[' '] = ['black']
        m['!'] = ['black', 'red']
        m[','] = ['black', 'Dim Gray']
        m['.'] = ['black', 'gray']
        # * Strong warm colors for A.E.I.O.U.
        m['a'] = ['Dark Orange']
        m['e'] = ['orange']
        m['i'] = ['gold']
        m['o'] = ['yellow']
        m['u'] = ['orange red']
        # * Cold colors for the front group
        m['b'] = ['Medium Aquamarine']
        m['c'] = ['Lime Green']
        m['d'] = ['Dark Green']
        m['f'] = ['Dodger Blue']
        m['g'] = ['Spring Green']
        m['h'] = ['Sea Green']
        m['j'] = ['Light Sea Green']
        m['k'] = ['Forest Green']
        # * light warm colors for the second group
        m['l'] = ['Indian Red']
        m['m'] = ['Saddle Brown']
        m['n'] = ['Peru']
        m['p'] = ['Tan']
        m['q'] = ['Sandy Brown']
        m['r'] = ['Brown']
        m['s'] = ['Firebrick']
        m['t'] = ['Rosy Brown']
        # * Cold warm mixed colors for the last group
        m['v'] = ['Hot Pink']
        m['w'] = ['Deep Pink']
        m['x'] = ['Maroon']
        m['y'] = ['Medium Purple']
        m['z'] = ['Dark Violet']
        return m[letter]

    def __init__(self):
        self.win = None
        self.quiting = False

    # $ Open up a "console", which show letter's in colored pixels
    def open(self):
        self.win = GraphWin("Pixel Console", WINDOW_SIZE_X, WINDOW_SIZE_Y, AUTO_FLUSH)
        self.win.setBackground( "black")

    # $ Started to receive and produce information
    def run(self):
        # [] Stop any false command from breaking the program
        try:
            # * Pause the system, waiting for a mouse click
            self.testRun2()
            # * wait until it was tell (by other thread) to quit
            while self.quiting == False:
                # self.win.getMouse()
                self.win.update()
                time.sleep(.1) # give up thread
            # * quit after
            self.close()
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

