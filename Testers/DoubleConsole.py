from Testers import TesterConsole
from Testers import PixelConsole
import threading

class DoubleConsole:

    def __init__(self):
        self.pixelConsole = PixelConsole.PixelConsole()

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
        testConsole = TesterConsole.TesterConsole()
        testConsole.printHelp()
        command = input("")
        while command != 'quit' and command != 'die':
            # * Run a tester
            testConsole.run( command, False )
            command = input("")
        self.pixelConsole.quiting = True
