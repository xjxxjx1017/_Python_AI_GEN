from Testers import TesterConsole
from Testers import PixelConsole

from Testers import PixelConsoleReader



def main():
    # pcr = PixelConsoleReader.PixelConsoleReader()
    # pcr.getScreenShot()

    pc = PixelConsole.PixelConsole()
    pc.open()
    pc.run()
    pc.close()

main()

# * Run a tester
tester = TesterConsole.TesterConsole()
tester.run()

# * Prevent the console from shutting down.
r = input( "Press any key to exit.\n")