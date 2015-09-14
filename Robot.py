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
		
class Speech:
	def yellHalt (self,powerSupply):
		powerSupply.power = powerSupply.power - 1
		print "*RoboCop yells 'HALT!'"
	def readRights (self, powerSupply):
		powerSupply.power = powerSupply.power - 5
		print "*RoboCop reads to suspect their rights with intense enthusiasm*"
	def mutterNoises (self, powerSupply):
		powerSupply.power = powerSupply.power + 2
		print "*RoboCop shakes violently while muttering robot noises, giving +2 charge to his battery power"
		
	

	
	
powerSupply = PowerSupply()
legs = Legs()
arms = Arms()
vision = Vision()

#legs:
powerSupply.power_Remaining()
legs.run(powerSupply)
powerSupply.power_Remaining()
legs.walk(powerSupply)
powerSupply.power_Remaining()
legs.roundHouse(powerSupply)
powerSupply.power_Remaining()

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

#speech:
speech = Speech()
speech.yellHalt(powerSupply)
powerSupply.power_Remaining()
speech.readRights(powerSupply)
powerSupply.power_Remaining()
speech.mutterNoises(powerSupply)
powerSupply.power_Remaining()

#Vision
vision.identifyCriminal(powerSupply)
powerSupply.power_Remaining()
vision.targetCriminal(powerSupply)
powerSupply.power_Remaining()