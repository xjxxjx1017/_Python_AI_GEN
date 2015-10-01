

class Universe(object):
	def __init__(self):
		# * A randomly generated config file that can be tracked
		self._seed = 0
		self._rlt_endYear = 0
		self._rlt_shipCount = 0

	def run(self, _seed):
		self._seed = _seed
		shipList = List[FogShip]()
		self._config = DynamicConfig.generate(self._seed)
		# * Initialize limits
		timeCount = 1000
		shipCount = 1000
		shipMax = 10000
		scaleSize = 100
		currentYear = 0
		# * Generate ships
		i = 0
		while i < shipCount:
			newShip = FogShip.createFromGen(Array[Single]((RandomEx.r.Next(scaleSize), RandomEx.r.Next(scaleSize), RandomEx.r.Next(scaleSize), RandomEx.r.Next(scaleSize), RandomEx.r.Next(scaleSize), RandomEx.r.Next(scaleSize), RandomEx.r.Next(scaleSize), RandomEx.r.Next(scaleSize))), self._config)
			shipList.Add(newShip)
			i += 1
		# * Run simulation
		i = 0
		while i < timeCount:
			# {} Loop through ships
			enumerator = shipList.GetEnumerator()
			while enumerator.MoveNext():
				ship = enumerator.Current
				# ? Check whether the unit is still alive
				if ship.isAlive == False:
					continue
				# * Chance for an event!
				dice20 = RandomEx.r.Next(20) + 1
				# ? Chance for event or wandering
				if dice20 >= self._config.chance_of_0_19_event:
					# * Get a random ship B
					B = shipList[RandomEx.r.Next(shipList.Count)]
					# ? Chance for encounter or reproduce
					if RandomEx.r.Next(20) > self._config.chance_of_0_19_encounter: # 50%
						FogShip.encounter(ship, B)
					else:
						FogShip.reproduce(ship, B)
				else:
					FogShip.wandering(ship)
				# * Time pass!
				FogShip.timePass(ship)
			# * Remove dead ships
			shipList.RemoveAll()
			# [] Debug outputs
			Console.Clear()
			Console.WriteLine(i + "|" + shipList.Count)
			Console.WriteLine(i + "|" + shipList.Count)
			Console.WriteLine(i + "|" + shipList.Count)
			currentYear = i
			# [] Time to stop debuging
			if shipList.Count < 10 or shipList.Count > shipMax:
				break
			i += 1
		# * A list of ships that still remain on the battle field.
		self._rlt_remainList = Dictionary[str, List]()
		# [] Time to stop debuging
		Console.Clear()
		Console.WriteLine("")
		Console.WriteLine("")
		Console.WriteLine("")
		Console.WriteLine("")
		Console.WriteLine("")
		# * Set up the result set
		# {} Loop through remained shiped
		enumerator = shipList.GetEnumerator()
		while enumerator.MoveNext():
			ship = enumerator.Current
			# [] Output remained ship's name and energy.
			Console.Write(ship.name + "|" + ship.energy + ", ")
			# ? Check if it's the same type of ship. 
			if self._rlt_remainList.ContainsKey(ship.name):
				# * Add them together, if it is.
				self._rlt_remainList[ship.name].Add(ship)
			else:
				# * Create a new list if it's not
				newList = List[FogShip]()
				newList.Add(ship)
				self._rlt_remainList.Add(ship.name, newList)
		# * Set up general result information
		self._rlt_endYear = currentYear
		self._rlt_shipCount = shipList.Count
		# [] Print the end year and total ship count
		Console.WriteLine("")
		Console.WriteLine("")
		Console.WriteLine("Year: " + self._rlt_endYear)
		Console.WriteLine("Alive: " + self._rlt_shipCount)
		# [] Print general ship types and counts.
		enumerator = rlt_remainList.GetEnumerator()
		while enumerator.MoveNext():
			pair = enumerator.Current
			Console.Write(pair.Key + "|" + pair.Value.Count + ", ")

	def ToStringLimit(self, limit):
		rlt = ""
		# [] Print the end year and total ship count
		rlt += "Year: " + self._rlt_endYear + '\n'
		rlt += "Alive: " + self._rlt_shipCount + '\n'
		# [] Print general ship types and counts.
		count = 0
		enumerator = rlt_remainList.GetEnumerator()
		while enumerator.MoveNext():
			pair = enumerator.Current
			rlt += pair.Key + "|" + pair.Value.Count + ", "
			count += 1
			if count > limit:
				break
		# [] Create a ship gen summary
		# # 1D: gen category, 2D: gen rank
		mark = List[Char]('A', 'B', 'C', 'D', 'E', 'F')
		genDiagram2D = Array.CreateInstance(int, FogShip.attribute_count, FogShip.attribute_rank_count)
		enumerator = rlt_remainList.GetEnumerator()
		while enumerator.MoveNext():
			pair = enumerator.Current
			enumerator = pair.Value.GetEnumerator()
			while enumerator.MoveNext():
				ship = enumerator.Current
				# * Get the ship gen summary
				i = 0
				while i < ship.gen.Length:
					# * Find the rank and the sequence
					value = ship.gen[i]
					gen = FogShip.generateNameChar(value)
					rank = mark.IndexOf(gen)
					# * Add the count
					genDiagram2D[i][rank] += 1
					i += 1
		# [] Print the ship gen summary
		Console.Write("Ship attribute summary: \n")
		Console.Write("+\tA\tB\tC\tD\tE\tF\n")
		i = 0
		while i < FogShip.attribute_count:
			Console.Write("" + i + ": ")
			j = 0
			while j < FogShip.attribute_rank_count:
				Console.Write("\t")
				if genDiagram2D[i][j] != 0:
					Console.Write(genDiagram2D[i][j])
				j += 1
			Console.Write("\n")
			i += 1
		rlt += '\n'
		rlt += '\n'
		return rlt