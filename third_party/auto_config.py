

class DynamicConfig(object):
	def __init__(self):
		# * Pre-set parameters for random-config-testing
		self._seed = 0
		self._chance_of_0_19_event = 0
		self._chance_of_0_19_encounter = 0
		self._chance_of_aggressive_limit_0_100_a = 0
		self._chance_of_aggressive_limit_0_100_b = 0
		self._scale_log_e_of_1_100_attack_success = 0
		self._scale_demi_of_01_2_energy_drain_a = 0
		self._scale_demi_of_01_2_energy_drain_b = 0
		self._scale_demi_of_01_1_energy_gain = 0
		self._scale_demi_of_01_1_reproduce_intent_a = 0
		self._scale_demi_of_01_1_reproduce_intent_b = 0
		self._scale_demi_of_01_1_chance_gen_of_a = 0
		self._scale_demi_of_01_1_percentage_genergy_cost_a = 0
		self._scale_demi_of_01_1_percentage_genergy_cost_b = 0
		self._scale_log_e_of_0_100_wandering_gain = 0
		self._chance_of_0_100_pass_lost = 0

	def ToString(self):
		rlt = "Config:\t\t" + self._seed + "\n"
		rlt += "chance_of_0_19_event:\t\t" + self._chance_of_0_19_event + "\n"
		rlt += "chance_of_aggressive_limit_0_100_a:\t\t" + self._chance_of_aggressive_limit_0_100_a + "\n"
		rlt += "chance_of_aggressive_limit_0_100_b:\t\t" + self._chance_of_aggressive_limit_0_100_b + "\n"
		rlt += "scale_log_e_of_1_100_attack_success:\t\t" + self._scale_log_e_of_1_100_attack_success + "\n"
		rlt += "scale_demi_of_01_2_energy_drain_a:\t\t" + self._scale_demi_of_01_2_energy_drain_a + "\n"
		rlt += "scale_demi_of_01_2_energy_drain_b:\t\t" + self._scale_demi_of_01_2_energy_drain_b + "\n"
		rlt += "scale_demi_of_01_1_energy_gain:\t\t" + self._scale_demi_of_01_1_energy_gain + "\n"
		rlt += "scale_demi_of_01_1_reproduce_intent_a:\t\t" + self._scale_demi_of_01_1_reproduce_intent_a + "\n"
		rlt += "scale_demi_of_01_1_reproduce_intent_b:\t\t" + self._scale_demi_of_01_1_reproduce_intent_b + "\n"
		rlt += "scale_demi_of_01_1_chance_gen_of_a:\t\t" + self._scale_demi_of_01_1_chance_gen_of_a + "\n"
		rlt += "scale_demi_of_01_1_percentage_genergy_cost_a:\t\t" + self._scale_demi_of_01_1_percentage_genergy_cost_a + "\n"
		rlt += "scale_demi_of_01_1_percentage_genergy_cost_b:\t\t" + self._scale_demi_of_01_1_percentage_genergy_cost_b + "\n"
		rlt += "scale_log_e_of_0_100_wandering_gain:\t\t" + self._scale_log_e_of_0_100_wandering_gain + "\n"
		rlt += "chance_of_0_100_pass_lost:\t\t" + self._chance_of_0_100_pass_lost + "\n"
		rlt += "\n"
		return rlt

	def generate(_seed):
		config = DynamicConfig()
		config.seed = _seed
		r = Random(config.seed)
		config.chance_of_0_19_event = r.Next(20)
		config.chance_of_0_19_encounter = r.Next(20)
		config.chance_of_aggressive_limit_0_100_a = r.Next(101)
		config.chance_of_aggressive_limit_0_100_b = r.Next(101)
		config.scale_log_e_of_1_100_attack_success = Math.Log(r.Next(100)) + 1
		config.scale_demi_of_01_2_energy_drain_a = (r.Next(201)) / 100.0f
		config.scale_demi_of_01_2_energy_drain_a = (r.Next(201)) / 100.0f
		config.scale_demi_of_01_1_energy_gain = (r.Next(101)) / 100.0f
		config.scale_demi_of_01_1_reproduce_intent_a = (r.Next(101)) / 100.0f
		config.scale_demi_of_01_1_reproduce_intent_b = (r.Next(101)) / 100.0f
		config.scale_demi_of_01_1_chance_gen_of_a = (r.Next(101)) / 100.0f
		config.scale_demi_of_01_1_percentage_genergy_cost_a = (r.Next(101)) / 100.0f
		config.scale_demi_of_01_1_percentage_genergy_cost_b = 1 - config.scale_demi_of_01_1_percentage_genergy_cost_a
		config.scale_log_e_of_0_100_wandering_gain = Math.Log(r.Next(101))
		config.chance_of_0_100_pass_lost = r.Next(101)
		return config

	generate = staticmethod(generate)