from Testers import TextConsole
from Testers import PixelConsole
from Testers import OneWayBuffer
import threading

class DoubleConsole:

    def __init__(self):
        # * Buffer fot the communication of two consoles
        self.messageBuffer = OneWayBuffer.OneWayBuffer()
        # * Initial consoles
        self.pixelConsole = PixelConsole.PixelConsole( self.messageBuffer )
        self.textConsole = TextConsole.TextConsole( self.messageBuffer )

    # Func - Run a text console and pixel console at the same time
    def run(self):
        # * Start a thread that runs the console
        backendThread = threading.Thread( target = self.runTestConsole )
        backendThread.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
        backendThread.start()
        # * Run the Pixel Console
        self.pixelConsole.open()
        self.pixelConsole.run()

    # Func - A text console that controls the Pixel Console
    def runTestConsole(self):
        # * Print help and wait for input
        self.textConsole.printHelp()
        command = input("")
        while command != 'quit' and command != 'die':
            # * Run a tester
            self.textConsole.run( command, False )
            command = input("")
        self.pixelConsole.quiting = True
