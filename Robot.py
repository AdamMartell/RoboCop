import random
class PowerSupply:
	def __init__ (self):
		self.power = 100
	def power_Remaining (self):
		print "Power remaining: ", self.power
	def charge(self):
		powerSupply.power = powerSupply.power + 10
		
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
	def punch(self, powerSupply):
		powerSupply.power = powerSupply.power - 4
		print "*RoboCop punches the criminal*  *POWWW*"
	def shoot(self, powerSupply):
		powerSupply.power = powerSupply.power - 3
		hitChance = random.random()
		if (hitChance > .20):
			print "*RoboCop Shoots the criminal* *BANG*"
		else:
			print "Miss"
	def handcuff(self, powerSupply):
		powerSupply.power = powerSupply.power - 2
		print "*RoboCop handcuffs the criminal* Justice!!!"
		
class Vision:
	def identifyCriminal(self, powerSupply):
		powerSupply.power = powerSupply.power - 1
		print "*Identifying criminal*"
	def targetCriminal(self, powerSupply):
		powerSupply.power = powerSupply.power - 1
		print "*Targeting criminal*"
		
	

	
	
powerSupply = PowerSupply()
legs = Legs()
arms = Arms()
vision = Vision()

#Arms
arms.shoot(powerSupply)
arms.shoot(powerSupply)
arms.shoot(powerSupply)
arms.shoot(powerSupply)
arms.shoot(powerSupply)
arms.shoot(powerSupply)
arms.shoot(powerSupply)
arms.shoot(powerSupply)
arms.shoot(powerSupply)
arms.shoot(powerSupply)
arms.shoot(powerSupply)
powerSupply.power_Remaining()

#Vision
vision.identifyCriminal(powerSupply)
powerSupply.power_Remaining()
vision.targetCriminal(powerSupply)
powerSupply.power_Remaining()