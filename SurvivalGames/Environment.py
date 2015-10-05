from ThirdParty import SystemPlus
from ThirdParty import RandomEx
from . import Creature
from . import AutoConfig

class Environment(object):

    # $ A randomly generated config file that can be tracked
    def __init__(self):
        self.seed = 0
        self.rlt_endYear = 0
        self.rlt_creatureCount = 0
        self.config = None

    # $ run the simulation
    def run(self, seed):
        cList = []
        self.seed = seed
        self.config = AutoConfig.generate( self.seed )
        # * Initialize limits
        timeCount = 1000
        cCount = 1000
        cMax = 10000
        scaleSize = 100
        currentYear = 0
        # * Generate cs
        i = 0
        while i < cCount:
            newc = Creature.createFromGen([
                RandomEx.r.randomInt(0, scaleSize), RandomEx.r.randomInt(0, scaleSize),
                RandomEx.r.randomInt(0, scaleSize), RandomEx.r.randomInt(0, scaleSize),
                RandomEx.r.randomInt(0, scaleSize), RandomEx.r.randomInt(0, scaleSize),
                RandomEx.r.randomInt(0, scaleSize), RandomEx.r.randomInt(0, scaleSize) ], self.config)
            cList += [ newc ]
            i += 1
        # * Run simulation
        for i in range(0, timeCount):
            # {} Loop through cs
            for c in cList:
                # ? Check whether the unit is still alive
                if c.isAlive == False:
                    continue
                # * Chance for an event!
                dice20 = RandomEx.r.randomInt( 1, 20 )
                # ? Chance for event or wandering
                if dice20 >= self.config.chance_of_0_19_event:
                    # * Get a random c B
                    B = cList[ RandomEx.r.randomInt( 0, len(cList) - 1) ]
                    # ? Chance for encounter or reproduce
                    if RandomEx.r.randomInt( 1, 20 ) > self.config.chance_of_0_19_encounter: # 50%
                        Creature.encounter(self.config, c, B)
                    else:
                        Creature.reproduce(self.config, c, B)
                else:
                    Creature.wandering(self.config, c)
                # * Time pass!
                Creature.timePass(self.config, c)
            # * Remove dead cs
            cList = [c for c in cList if c.isAlive == True ]
            # [] Debug outputs
            SystemPlus.consoleClear()
            SystemPlus.consolePrintL(str(i) + "|" + str(len(cList)))
            SystemPlus.consolePrintL(str(i) + "|" + str(len(cList)))
            SystemPlus.consolePrintL(str(i) + "|" + str(len(cList)))
            currentYear = i
            # [] Time to stop debugging
            if len(cList) < 10 or len(cList) > cMax:
                break
        # * A list of cs that still remain on the battle field.
        self.rlt_remainList = {}
        # [] Time to stop debugging
        SystemPlus.consoleClear()
        SystemPlus.consolePrintL("")
        SystemPlus.consolePrintL("")
        SystemPlus.consolePrintL("")
        SystemPlus.consolePrintL("")
        SystemPlus.consolePrintL("")
        # * Set up the result set
        # {} Loop through remained ced
        for c in cList:
            # [] Output remained c's name and energy.
            SystemPlus.consolePrintL(c.name + "|" + str( c.energy ) + ", ")
            # ? Check if it's the same type of c.
            if c.name in self.rlt_remainList:
                # * Add them together, if it is.
                self.rlt_remainList[c.name].Add += c
            else:
                # * Create a new list if it's not
                self.rlt_remainList[c.name] = [ c ]
        # * Set up general result information
        self.rlt_endYear = currentYear
        self.rlt_creatureCount = len(cList)
        # [] Print the end year and total c count
        SystemPlus.consolePrintL("")
        SystemPlus.consolePrintL("")
        SystemPlus.consolePrintL("Year: " + str(self.rlt_endYear))
        SystemPlus.consolePrintL("Alive: " + str(self.rlt_creatureCount))
        # [] Print general creature types and counts.
        for key, value in self.rlt_remainList.items():
            SystemPlus.consolePrintL( str( key ) + "|" + str(len( value )) + ", " )

    # $ Return a string of detail information about this universe
    def toStringLimit(self, limit):
        rlt = ""
        # [] Print the end year and total c count
        rlt += "Year: " + str(self.rlt_endYear) + '\n'
        rlt += "Alive: " + str(self.rlt_creatureCount) + '\n'
        # [] Print general creature types and counts.
        count = 0
        for key, value in self.rlt_remainList.items():
            rlt += key + "|" + str(len(value)) + ", "
            count += 1
            if count > limit:
                break
        # [] Create a creature gen summary
        # # 1D: gen category, 2D: gen rank
        mark = ['A', 'B', 'C', 'D', 'E', 'F']
        genDiagram2D = [[0 for x in range(Creature.attribute_rank_count)]
                        for x in range(Creature.attribute_count)]
        for keys, values in self.rlt_remainList.items():
            for c in values:
                # * Get creature gen summary
                for i in range( 0, len(c.gen) ):
                    # * Find the rank and the sequence
                    value = c.gen[i]
                    gen = Creature.generateNameChar( value )
                    rank = mark.index( gen )
                    # * Add the count
                    genDiagram2D[i][rank] += 1
        # [] Print the creature gen summary
        SystemPlus.consolePrint("Creature attribute summary: \n")
        SystemPlus.consolePrint("+\tA\tB\tC\tD\tE\tF\n")
        for i in range(0, Creature.attribute_count):
            SystemPlus.consolePrint("" + str(i) + ": ")
            for j in range(0, Creature.attribute_rank_count):
                SystemPlus.consolePrint("\t")
                if genDiagram2D[i][j] != 0:
                    SystemPlus.consolePrint(genDiagram2D[i][j])
            SystemPlus.consolePrint("\n")
        rlt += '\n'
        rlt += '\n'
        return rlt