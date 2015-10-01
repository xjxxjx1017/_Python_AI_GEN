from testers import tester_console

# * Run a tester
tester = tester_console.TesterConsole()
tester.run()

# * Prevent the console from shutting down.
r = input( "Press any key to exit.\n")