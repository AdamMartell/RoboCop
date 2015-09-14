
class PowerSupply:
	def __init__ (self):
		self.power = 100
	def power_Remaining (self):
		print "Power remaining: ", self.power
		
class Legs:
	def run(self, powerSupply):
		powerSupply.power = powerSupply.power - 2
		print "*RoboCop Runs*"
	def walk(self, powerSupply):
		powerSupply.power = powerSupply.power - 1
		print "*RoboCop Walks*"
	def roundHouse(self, powerSupply):
		powerSupply.power = powerSupply.power - 5
		print "*RoboCop roundhouses a bitch* *Smack!!!!!*"
		
class Arms:
	
powerSupply = PowerSupply()
legs = Legs()
powerSupply.power_Remaining()
legs.run(powerSupply)
powerSupply.power_Remaining()
legs.walk(powerSupply)
powerSupply.power_Remaining()
legs.roundHouse(powerSupply)
powerSupply.power_Remaining()