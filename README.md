## Auto Game Configuration Tester & Generator
I'm trying to make an auto testing tool for game developers. It supposed to automatically test and suggest best configurations for games.

### Current Flow
1. Run main.py to start
2. A console pops up
3. The user types in a command
4. The console runs the "Survival Game" simulation with randomly generated configuration for multiple times
5. The console give out a summary, a list of reports
6. The user can type in an integer to check details of a report and the configuration that runs the simulation
7. Return to step 3

### Current Features
* A tiny simulation game, the survival game
* Text console, which supports command line input & output
* Pixel console, which shows letters in pixels

### Development Route Map
````
	1	A  ___________	Instant game
	2		|	|_____	Real time game
	3		|_____________	Graphic for data analyse
	4				|_____  Graphic for game
	
	1	B  ___________	Analyse
	2			|_____	Modularize
	3			|_____	Graphics
	4			|_____	Hacking & Data Fetching
````
### Upcoming Development
````
* A1    A super fast, instant game, legendary fighter
* A3    Show data in pixel colors!	A reports for all generations.
* A2    A real simulation game, game is not instant, shooting

* B2    Modularize - auto parameter tester
* B4    PixelGraphic mode for command input XD, for hacking

* B1    time limit, or cycle limit, 100ms - break & give results
* B1    normal distribution
* B1    Parameters range/mid report ! with weight !
````
### Command List
````
////////////// HELP //////////////////
help                For help
quit                Quit the console
start               Run a standard test
filter x x x x      Run a filter test, only record the test we wanted
                        p1: min years
                        p2: max years
                        p3: min creatures
                        p4: max creatures
single x x          Run series of tests for a single configuration generated
                    by a certain seed
                        p1: a fixed seed for the simulation
                        p2: number of times for the simulation
r (x)               Redo the last 'n' command
                        p1 (=1): the previous 'n' test that you want to execute
[integer]           If the input is an integer, print the detail of a test has
                    the same ID as the integer
//////////////////////////////////////
````
