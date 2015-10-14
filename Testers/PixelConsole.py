from Lib.graphics import *
from ThirdParty import SystemPlus
from Testers import OneWayBuffer
import traceback

PADDING = 16
PIXEL_SIZE = 4
WINDOW_SIZE_X = 200
WINDOW_SIZE_Y = 500
WINDOW_COLUMN_COUNT = 3
AUTO_FLUSH = True
PIXEL_COUNT_X = int( ( WINDOW_SIZE_X - PADDING * 2 ) / PIXEL_SIZE )
PIXEL_COUNT_Y = int( ( WINDOW_SIZE_Y - PADDING * 2 ) / PIXEL_SIZE )
WINDOW_SIZE_X_TRUE = ( WINDOW_SIZE_X ) * WINDOW_COLUMN_COUNT + PADDING

class PixelConsole(object):

    def __init__(self, inputBuffer:"OneWayBuffer"):
        self.win = None
        self.quiting = False
        self.curCursorX = 0
        self.curCursorY = 0
        self.curCursorCol = 0
        self.totalString = []
        self.totalColors = []
        self.curColorIndex = 0
        self.isRunning = False
        self.inputBuffer = inputBuffer

    # $ Draw a string on the screen
    def _drawString(self):
        # * Draw pixels (sentence) on the screen :)
        # {} Start the loop
        while True:
            if self.curCursorX >= PIXEL_COUNT_X:
                self.curCursorX = 0
                self.curCursorY += 1
                self.clearNextNLines( 2 )
            if self.curCursorY >= PIXEL_COUNT_Y:
                self.curCursorX = 0
                self.curCursorY = 0
                self.curCursorCol += 1
            if self.curCursorCol >= WINDOW_COLUMN_COUNT:
                self.curCursorX = 0
                self.curCursorY = 0
                self.curCursorCol = 0
            # # Calculate the position for pixels
            W = PADDING + self.curCursorX * PIXEL_SIZE + self.curCursorCol * ( PIXEL_COUNT_X * PIXEL_SIZE + PADDING )
            H = PADDING + self.curCursorY * PIXEL_SIZE
            # ? If there're more colors to print
            if self.curColorIndex < len( self.totalColors ):
                # * Print the color
                color = self.totalColors[ self.curColorIndex ]
                self.curColorIndex += 1
                self.drawRectangle( W, H, color )
                # ? If the color is white
                if color == 'white':
                    # * Go to the next line and leave a blank line
                    self.curCursorX = 0
                    self.curCursorY += 1
                    self.clearNextNLines( 2 )
                    self.curCursorY += 1
                    continue
            else:
                break
            self.curCursorX += 1

    # $ Clear the whole screen
    def clearAll(self):
        self.curCursorX = 0
        self.curCursorY = 0
        self.curCursorCol = 0
        self.totalColors = []
        self.curColorIndex = 0
        self.drawFullScreen("black")

    # $ Draw a string on the screen
    def clearNextNLines(self, lines):
        saveCursorX = self.curCursorX
        saveCursorY = self.curCursorY
        saveCursorCol = self.curCursorCol
        newLineCount = 0
        # * Draw pixels (sentence) on the screen :)
        # {} Start the loop
        while True:
            self.curCursorX = 0
            if self.curCursorY >= PIXEL_COUNT_Y:
                self.curCursorX = 0
                self.curCursorY = 0
                self.curCursorCol += 1
            if self.curCursorCol >= WINDOW_COLUMN_COUNT:
                self.curCursorX = 0
                self.curCursorY = 0
                self.curCursorCol = 0
            # # Calculate the position for pixels
            W = PADDING + self.curCursorX * PIXEL_SIZE + self.curCursorCol * ( PIXEL_COUNT_X * PIXEL_SIZE + PADDING )
            H = PADDING + self.curCursorY * PIXEL_SIZE
            # ? If there're more colors to print
            if newLineCount < lines:
                # * Print the color
                self.drawRectangleSize( W, H, "black", PIXEL_COUNT_X, 1 )
                newLineCount +=1
            else:
                break
            self.curCursorY += 1
        self.curCursorX = saveCursorX
        self.curCursorY = saveCursorY
        self.curCursorCol = saveCursorCol

    def drawString(self, words):
        # * Convert letters to pixels
        for l in words:
            for c in self.letter2color(l):
                self.totalColors.append( c )
        self._drawString()
        self.clearNextNLines( 3 )
        # * Clear some lines
        # * Refresh the screen
        if AUTO_FLUSH is False:
            self.win.flush()

    # $ Open up a "console", which show letter's in colored pixels
    def open(self):
        self.win = GraphWin("Pixel Console", WINDOW_SIZE_X_TRUE, WINDOW_SIZE_Y, AUTO_FLUSH)
        self.win.setBackground( "black")

    # $ Started to receive and produce information
    def run(self):
        # [] Stop any false command from breaking the program
        try:
            # * Pause the system, waiting for a mouse click
            # self.testRun2()
            # * wait until it was tell (by other thread) to quit
            while self.quiting == False:
                # self.win.getMouse()
                self.drawString( self.inputBuffer.readNew() )
                self.win.update()
                time.sleep(.1) # give up thread
                self.isRunning = True
            # * quit after
            self.isRunning = False
            self.close()
        except Exception:
            SystemPlus.consolePrintL(traceback.format_exc())
            SystemPlus.consolePrintL( "You can still continue with the terminal:")
            SystemPlus.consolePrintL( "///////////////////////////////////////////////")

    # $ Close the "console"
    def close(self):
        self.win.close()


    def letter2color(self, letter):
        letter = letter.lower()
        m = {}
        # * Symbolic colors for symbols
        m['\n'] = ['black', 'white']
        m[' '] = ['black']
        m['!'] = ['black', 'red']
        m[','] = ['black', 'Dim Gray']
        m['.'] = ['black', 'gray']
        m['/'] = ['blue', 'green']
        # * Strong warm colors for A.E.I.O.U.
        m['a'] = ['Dark Orange']
        m['e'] = ['orange']
        m['i'] = ['gold']
        m['o'] = ['yellow']
        m['u'] = ['orange red']
        # * Cold colors for the front group
        m['b'] = ['Medium Aquamarine']
        m['c'] = ['Lime Green']
        m['d'] = ['#006400'] # 'Dark Green'
        m['f'] = ['Dodger Blue']
        m['g'] = ['Spring Green']
        m['h'] = ['#87ceeb'] # 'Sky Blue'
        m['j'] = ['Light Sea Green']
        m['k'] = ['Forest Green']
        # * light warm colors for the second group
        m['l'] = ['#cd5c5c'] # 'Indian Red'
        m['m'] = ['Saddle Brown']
        m['n'] = ['Peru']
        m['p'] = ['Tan']
        m['q'] = ['Sandy Brown']
        m['r'] = ['Brown']
        m['s'] = ['Firebrick']
        m['t'] = ['Rosy Brown']
        # * Cold warm mixed colors for the last group
        m['v'] = ['Hot Pink']
        m['w'] = ['#ff1493'] # 'Deep Pink'
        m['x'] = ['Maroon']
        m['y'] = ['Medium Purple']
        m['z'] = ['Dark Violet']

        if letter not in m:
            return ['green']
        else:
            return m[letter]

    # $ Draw a rectangle on the screen with a specific color
    def drawRectangleSize(self, x, y, color, gridCountX, gridCountY):
        c = Rectangle( Point( x, y ), Point( x + PIXEL_SIZE * gridCountX - 1, y + PIXEL_SIZE * gridCountY - 1) )
        c.setOutline( color )
        c.setFill( color )
        c.draw( self.win )

    # $ Draw a rectangle, fill the screen
    def drawFullScreen(self, color):
        c = Rectangle( Point( 0, 0 ), Point( WINDOW_SIZE_X_TRUE, WINDOW_SIZE_Y ) )
        c.setOutline( color )
        c.setFill( color )
        c.draw( self.win )

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
        self.drawString(words)
        self.drawString(words)
        self.drawString(words)
        self.drawString(words)
        self.drawString(words)
        self.drawString(words)
        self.drawString(words)
        self.drawString(words)
        self.drawString(words)
        self.drawString(words)
        self.drawString(words)
        self.drawString(words)
        self.drawString(words)
        self.drawString(words)
        self.drawString(words)