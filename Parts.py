import random
from msvcrt import getch
class PowerSupply:
	def __init__ (self, power = 100):
		self.power = power
	def displayPowerRemaining (self):
		print "Power remaining: ", self.power
	def charge(self, amount, power = 1000):
		if self.power < power:
			self.power = self.power + amount
			print "RoboCop charged +", amount
		else:
			raise Exception()
	def deplete(self, amount = 0):
		self.power = self.power - amount
		
		
class Stats:
	def __init__(self):
		self.bodyCount = 0
	def addBody(self, numOfBodies):
		self.bodyCount += numOfBodies
	def displayBodyCount(self):
		print "RoboCop has un-instanciated ", self.bodyCount, "criminals"
		
		
		
class Legs:
	def run(self, powerSupply):
		powerSupply.deplete(2)
		print "*RoboCop Runs*"
	def walk(self, powerSupply):
		powerSupply.deplete(1)
		print "*RoboCop Walks*"
	def roundHouse(self, powerSupply, stats):
		powerSupply.power = powerSupply.power - 5
		numOfHits = random.randrange(1, 5)
		stats.addBody(numOfHits)
		criminalRoundHouse = "*RoboCop roundhouses " + str(numOfHits) + " criminals* *Smack!!!!!*"
		if numOfHits == 1:
			print criminalRoundHouse[:31] + criminalRoundHouse[32:]
		else:
			print criminalRoundHouse
class Arms(object):
	def punch(self, powerSupply):
		powerSupply.deplete(4)
		print "*RoboCop punches the criminal*  *POWWW*"
	def shoot(self, powerSupply):
		powerSupply.deplete(3)
		hitChance = random.random()
		if (hitChance > .20):
			print "*RoboCop Shoots the criminal* *BANG*"
		else:
			print "Miss"
	def handcuff(self, powerSupply):
		powerSupply.deplete(2)
		print "*RoboCop handcuffs the criminal* Justice!!!"
		
class RightArm(Arms):
	def shoot(self,powerSupply):
		super (RightArm, self).shoot(powerSupply)
		hitChance = random.random()
		if (hitChance > .70):
			print "Right Arm bonus shot. Sweet!"
			
class LeftArm(Arms):
	def shoot(self, powerSupply):
		super (LeftArm, self).shoot(powerSupply)
		bonusRoundChance = random.random()
		if (bonusRoundChance > .2) and (powerSupply.power > 3):
			self.shoot(powerSupply)

class Vision:
	def identifyCriminal(self, powerSupply):
		powerSupply.deplete(1)
		print "*Identifying criminal*"
	def targetCriminal(self, powerSupply):
		powerSupply.deplete(1)
		targetChance = random.random()
		if (targetChance > .25):
			print "*Criminal targeted.*"
		else:
			print "*Unable to target. Try again*"
		
class Speech:
	def yellHalt (self,powerSupply):
		powerSupply.deplete(1)
		print "*RoboCop yells 'HALT!'"
	def readRights (self, powerSupply):
		powerSupply.deplete(5)
		print "*RoboCop reads to suspect their rights with intense enthusiasm*"
	def mutterNoises (self, powerSupply):
		powerSupply.charge(2)
		print "*RoboCop shakes violently while muttering robot noises, giving +2 charge to his battery power"
	def sayMessage(self,message):
		if (message > 0):
			print message.upper()