
import math
from ThirdParty import RandomEx

def generate(_seed):
    config = AutoConfig()
    config.seed = _seed
    r = RandomEx.RandomEx(config.seed)
    config.chance_of_0_19_event = r.randomInt(0, 19)
    config.chance_of_0_19_encounter = r.randomInt(0, 19)
    config.chance_of_aggressive_limit_0_100_a = r.randomInt(0, 100)
    config.chance_of_aggressive_limit_0_100_b = r.randomInt(0, 100)
    config.scale_log_e_of_1_100_attack_success = math.log(r.randomInt(1, 100))
    config.scale_demi_of_01_2_energy_drain_a = r.randomFloat(0.1, 2)
    config.scale_demi_of_01_2_energy_drain_b = r.randomFloat(0.1, 2)
    config.scale_demi_of_01_1_energy_gain = r.randomFloat(0.1, 1)
    config.scale_demi_of_01_1_reproduce_intent_a = r.randomFloat(0.1, 1)
    config.scale_demi_of_01_1_reproduce_intent_b = r.randomFloat(0.1, 1)
    config.scale_demi_of_01_1_chance_gen_of_a = r.randomFloat(0.1, 1)
    config.scale_demi_of_01_1_percentage_genergy_cost_a = r.randomFloat(0.1, 1)
    config.scale_demi_of_01_1_percentage_genergy_cost_b = 1 - config.scale_demi_of_01_1_percentage_genergy_cost_a
    config.scale_log_e_of_1_100_wandering_gain = math.log(r.randomInt(1, 100))
    config.chance_of_0_100_pass_lost = r.randomInt(0, 100)
    return config

class AutoConfig:

    def __init__(self):
        # * Pre-set parameters for random-config-testing
        self.seed = 0
        self.chance_of_0_19_event = 0
        self.chance_of_0_19_encounter = 0
        self.chance_of_aggressive_limit_0_100_a = 0
        self.chance_of_aggressive_limit_0_100_b = 0
        self.scale_log_e_of_1_100_attack_success = 0
        self.scale_demi_of_01_2_energy_drain_a = 0
        self.scale_demi_of_01_2_energy_drain_b = 0
        self.scale_demi_of_01_1_energy_gain = 0
        self.scale_demi_of_01_1_reproduce_intent_a = 0
        self.scale_demi_of_01_1_reproduce_intent_b = 0
        self.scale_demi_of_01_1_chance_gen_of_a = 0
        self.scale_demi_of_01_1_percentage_genergy_cost_a = 0
        self.scale_demi_of_01_1_percentage_genergy_cost_b = 0
        self.scale_log_e_of_1_100_wandering_gain = 0
        self.chance_of_0_100_pass_lost = 0

    def toString(self):
        rlt = "Config: " + str(self.seed) + "\n"
        rlt += "chance_of_0_19_event:                          %.0f\n" % self.chance_of_0_19_event
        rlt += "chance_of_aggressive_limit_0_100_a:            %.0f\n" % self.chance_of_aggressive_limit_0_100_a
        rlt += "chance_of_aggressive_limit_0_100_b:            %.0f\n" % self.chance_of_aggressive_limit_0_100_b
        rlt += "scale_log_e_of_1_100_attack_success:           %.2f\n" % self.scale_log_e_of_1_100_attack_success
        rlt += "scale_demi_of_01_2_energy_drain_a:             %.2f\n" % self.scale_demi_of_01_2_energy_drain_a
        rlt += "scale_demi_of_01_2_energy_drain_b:             %.2f\n" % self.scale_demi_of_01_2_energy_drain_b
        rlt += "scale_demi_of_01_1_energy_gain:                %.2f\n" % self.scale_demi_of_01_1_energy_gain
        rlt += "scale_demi_of_01_1_reproduce_intent_a:         %.2f\n" % self.scale_demi_of_01_1_reproduce_intent_a
        rlt += "scale_demi_of_01_1_reproduce_intent_b:         %.2f\n" % self.scale_demi_of_01_1_reproduce_intent_b
        rlt += "scale_demi_of_01_1_chance_gen_of_a:            %.2f\n" % self.scale_demi_of_01_1_chance_gen_of_a
        rlt += "scale_demi_of_01_1_percentage_genergy_cost_a:  %.2f\n" %\
            self.scale_demi_of_01_1_percentage_genergy_cost_a
        rlt += "scale_demi_of_01_1_percentage_genergy_cost_b:  %.2f\n" %\
            self.scale_demi_of_01_1_percentage_genergy_cost_b
        rlt += "scale_log_e_of_0_100_wandering_gain:           %.2f\n" % self.scale_log_e_of_1_100_wandering_gain
        rlt += "chance_of_0_100_pass_lost:                     %.0f\n" % self.chance_of_0_100_pass_lost
        rlt += "\n"
        return rlt