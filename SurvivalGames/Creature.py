from ThirdParty import SystemPlus
from ThirdParty import RandomEx

attribute_count = 8
attribute_rank_count = 6

def createFromGen(gen, config):
    rlt = Creature()
    rlt.isAlive = True
    # * Create ship attributes from gens
    # # A gens varies from 0 to 99
    rlt.energy = gen[0]
    rlt.attack = gen[1]
    rlt.reproduction = gen[2]
    rlt.speed = gen[3]
    rlt.size = gen[4]
    rlt.aggressive = gen[5]
    rlt.energy_gain = gen[6]
    rlt.energy_capacity = gen[7]
    # * Save the gen and config.
    rlt.gen = gen
    Creature.config = config
    # * Create a name of the ship according to its gen
    # # Each name letter represents a gen approximate value
    # # A name letter varies from A to F
    rlt.name = ""
    for g in gen:
        rlt.name += generateNameChar( g )
    return rlt


def encounter( config, a, b):
    # ? Check whether the ship A and B are still alive
    if a.isAlive == False or b.isAlive == False:
        return 0
    aWin = 0
    # ? Check how the encounter will happened
    if a.aggressive >= config.chance_of_aggressive_limit_0_100_a and \
                    b.aggressive >= config.chance_of_aggressive_limit_0_100_b:
        # ? Check winner
        aWin = 1 if a.attack > b.attack * config.scale_log_e_of_1_100_attack_success else -1
        # * Both units lost energy
        b.energy -= a.attack * config.scale_demi_of_01_2_energy_drain_a
        a.energy -= b.attack * config.scale_demi_of_01_2_energy_drain_b
    elif a.aggressive > config.chance_of_aggressive_limit_0_100_a:
        aWin = 1
    elif b.aggressive > config.chance_of_aggressive_limit_0_100_b:
        aWin = -1
    # ? Check the winner
    if aWin == 1:
        # * Winner gains energy
        if b.energy > 0:
            a.energy += b.energy * config.scale_demi_of_01_1_energy_gain
        b.isAlive = False
        # [] Show the battle in the console
        SystemPlus.consolePrintL("Encounter: " + a.name + " > " + b.name + " +" + str(b.energy if b.energy > 0 else 0))
    elif aWin == -1:
        # * Winner gains energy
        if a.energy > 0:
            b.energy += a.energy * config.scale_demi_of_01_1_energy_gain
        a.isAlive = False
        # [] Show the battle in the console
        SystemPlus.consolePrintL("Encounter: " + a.name + " > " + b.name + " +" + str(a.energy if a.energy > 0 else 0))
    return aWin


def reproduce(config, a, b):
    # ? Check whether the ship A and B are still alive
    if a.isAlive == False or b.isAlive == False:
        return None
    # ? Check whether both ship want to reproduce
    boolA = RandomEx.r.randomInt(0, 100) * config.scale_demi_of_01_1_reproduce_intent_a < a.reproduction
    boolB = RandomEx.r.randomInt(0, 100) * config.scale_demi_of_01_1_reproduce_intent_b < b.reproduction
    if a or b:
        return None
    # * Create a new ship by gen mixing
    gen = [ 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, len(a.gen) ):
        if RandomEx.r.randomInt(0, 100) > 49 * config.scale_demi_of_01_1_chance_gen_of_a:
            gen[i] = a.gen[i]
        else:
            gen[i] = b.gen[i]
        i += 1
    rlt = createFromGen(gen, config)
    # rlt.energy = a.reproduction + b.reproduction;
    a.energy -= rlt.energy * 0.5 * config.scale_demi_of_01_1_percentage_genergy_cost_b
    b.energy -= rlt.energy * 0.5 * config.scale_demi_of_01_1_percentage_genergy_cost_b
    SystemPlus.consolePrintL("Reproduce: " + a.name + " + " + b.name + " = " + rlt.name)
    return rlt


def wandering(config, a):
    # Console.Write( a.name + ": " + a.energy + ", " );
    a.energy += a.energy_gain * config.scale_log_e_of_1_100_wandering_gain
    return 0


def timePass(config, a):
    # ? Check whether the ship will lost some energy
    if RandomEx.r.randomInt(0, 100) > config.chance_of_0_100_pass_lost:
        a.energy -= 1
    return 0


def generateNameChar(gen):
    if gen > 90:
        return 'A'
    if gen > 80:
        return 'B'
    if gen > 60:
        return 'C'
    if gen > 40:
        return 'D'
    if gen > 20:
        return 'E'
    return 'F'


class Creature(object):

    def __init__(self):
        # * Ship attributes ( it's magic... )
        self.energy = 0
        self.attack = 0
        self.reproduction = 0
        self.speed = 0
        self.size = 0
        self.aggressive = 0
        self.energy_gain = 0
        self.energy_capacity = 0
        # * Ship's core testing features: gens, names, and is-alive
        self.gen = []
        self.isAlive = False
        # # A B C D E F by gen, 100-90, 90-80, 80-60, 60-40, 40-20, 20-0
        self.name = ""