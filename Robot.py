
class PowerSupply:
	def __init__ (self):
		self.power = 100
	def power_drain (self):
		print self.power
		
class Legs:
	def run(self, powerSupply):
		powerSupply.power = powerSupply.power - 2
	
powerSupply = PowerSupply()
legs = Legs()
powerSupply.power_drain()
legs.run(powerSupply)
powerSupply.power_drain()
