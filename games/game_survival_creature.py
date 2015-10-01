

class FogShip(object):
	def __init__(self):
		self._attribute_count = 8
		self._attribute_rank_count = 6

	# * Ship attributes ( it's magic... )
	# * Ship's core testing features: gens, names, and is-alive # A B C D E F by gen, 100-90, 90-80, 80-60, 60-40, 40-20, 20-0
	# * Configuration for ships
	def createFromGen(gen, config):
		rlt = FogShip()
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
		FogShip.config = config
		# * Create a name of the ship according to its gen
		# # Each name letter represents a gen approximate value
		# # A name letter varies from A to F
		rlt.name = ""
		enumerator = gen.GetEnumerator()
		while enumerator.MoveNext():
			g = enumerator.Current
			rlt.name += 
		return rlt

	createFromGen = staticmethod(createFromGen)

	def encounter(a, b):
		# ? Check whether the ship A and B are still alive
		if a.isAlive == False or b.isAlive == False:
			return 0
		aWin = 0
		# ? Check how the encounter will happened
		if a.aggressive >= self._config.chance_of_aggressive_limit_0_100_a and b.aggressive >= self._config.chance_of_aggressive_limit_0_100_b:
			# ? Check winner
			aWin = 1 if a.attack > b.attack * self._config.scale_log_e_of_1_100_attack_success else -1
			# * Both units lost energy
			b.energy -= 
			a.energy -= 
		elif a.aggressive > self._config.chance_of_aggressive_limit_0_100_a:
			aWin = 1
		elif b.aggressive > self._config.chance_of_aggressive_limit_0_100_b:
			aWin = -1
		# ? Check the winner
		if aWin == 1:
			# * Winner gains energy
			a.energy += 
			b.isAlive = False
			# [] Show the battle in the console
			Console.WriteLine("Encounter: " + a.name + " > " + b.name + " +" + (b.energy if b.energy > 0 else 0))
		elif aWin == -1:
			# * Winner gains energy
			b.energy += 
			a.isAlive = False
			# [] Show the battle in the console
			Console.WriteLine("Encounter: " + a.name + " > " + b.name + " +" + (a.energy if a.energy > 0 else 0))
		return aWin

	encounter = staticmethod(encounter)

	def reproduce(a, b):
		# ? Check whether the ship A and B are still alive
		if a.isAlive == False or b.isAlive == False:
			return None
		# ? Check whether both ship want to reproduce
		if RandomEx.r.Next(100) * self._config.scale_demi_of_01_1_reproduce_intent_a < a.reproduction or RandomEx.r.Next(100) * self._config.scale_demi_of_01_1_reproduce_intent_a < b.reproduction:
			return None
		# * Create a new ship by gen mixing
		gen = 
		i = 0
		while i < a.gen.Length:
			self._gen[i] = a.gen[i] if RandomEx.r.Next(100) > 49 * self._config.scale_demi_of_01_1_chance_gen_of_a else b.gen[i]
			i += 1
		rlt = FogShip.createFromGen(self._gen, self._config)
		# rlt.energy = a.reproduction + b.reproduction;
		a.energy -= 
		b.energy -= 
		Console.WriteLine("Reproduce: " + a.name + " + " + b.name + " = " + rlt.name)
		return rlt

	reproduce = staticmethod(reproduce)

	def wandering(a):
		# Console.Write( a.name + ": " + a.energy + ", " );
		a.energy += 
		return 0

	wandering = staticmethod(wandering)

	def timePass(a):
		# ? Check whether the ship will lost some energy
		if RandomEx.r.Next(100) > self._config.chance_of_0_100_pass_lost:
			a.energy -= 
		return 0

	timePass = staticmethod(timePass)

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

	generateNameChar = staticmethod(generateNameChar)