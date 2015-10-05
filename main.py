from Testers import TesterConsole
from Testers import PixelConsole

import PIL



def main():
    pC = PixelConsole.PixelConsole()
    pC.open()
    pC.run()
    pC.close()

main()

# * Run a tester
tester = TesterConsole.TesterConsole()
tester.run()

# * Prevent the console from shutting down.
r = input( "Press any key to exit.\n")