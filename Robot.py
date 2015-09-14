import random
from msvcrt import getch
class PowerSupply:
	def __init__ (self):
		self.power = 100
	def power_Remaining (self):
		print "Power remaining: ", self.power
	def charge(self):
		powerSupply.power = powerSupply.power + 10
		print "RoboCop charged +10"
		
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
			print "*RoboCop misses. -20 power*"
			powerSupply.power = powerSupply.power - 20
	def handcuff(self, powerSupply):
		powerSupply.power = powerSupply.power - 2
		print "*RoboCop handcuffs the criminal* Justice!!!"
		
class Vision:
	def identifyCriminal(self, powerSupply):
		powerSupply.power = powerSupply.power - 1
		print "*Identifying criminal*"
	def targetCriminal(self, powerSupply):
		powerSupply.power = powerSupply.power - 1
		targetChance = random.random()
		if (targetChance > .25):
			print "*Criminal targeted.*"
		else:
			print "*Unable to target. Try again*"
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
		
class Test:
	def testLegs(self,Legs):
		powerSupply.power_Remaining()
		legs.run(powerSupply)
		powerSupply.power_Remaining()
		legs.walk(powerSupply)
		powerSupply.power_Remaining()
		legs.roundHouse(powerSupply)
		powerSupply.power_Remaining()
	def testArms(self,Arms):
		powerSupply.power_Remaining()
		arms.punch(powerSupply)
		powerSupply.power_Remaining()
		arms.shoot(powerSupply)
		powerSupply.power_Remaining()
		arms.handcuff(powerSupply)
		powerSupply.power_Remaining()
	def testVision(self,Vision):
		powerSupply.power_Remaining()
		vision.identifyCriminal(powerSupply)
		powerSupply.power_Remaining()
		vision.targetCriminal(powerSupply)
	def testSpeech(self,Speech):
		powerSupply.power_Remaining()
		speech.yellHalt(powerSupply)
		powerSupply.power_Remaining()
		speech.readRights(powerSupply)
		powerSupply.power_Remaining()
		speech.mutterNoises(powerSupply)
		powerSupply.power_Remaining()
		
class Controller:
	def roboCopController(self, powerSupply):
		while True:
			if powerSupply.power < 0:
				print "RoboCop needs to recharge...Please press <F or G> to recharge"
				key = ord(getch())
				if key == 27:
					break
				elif key == 113:
					print "RoboCop needs to recharge...Please press <F or G> to recharge"
				elif key == 119:
					print "RoboCop needs to recharge...Please press <F or G> to recharge"
				elif key == 104:
					print "RoboCop needs to recharge...Please press <F or G> to recharge"
				elif key == 112:
					print "RoboCop needs to recharge...Please press <F or G> to recharge"
				elif key == 115:
					print "RoboCop needs to recharge...Please press <F or G> to recharge"
				elif key == 99:
					print "RoboCop needs to recharge...Please press <F or G> to recharge"
				elif key == 100:
					print "RoboCop needs to recharge...Please press <F or G> to recharge"
				elif key == 97:
					print "RoboCop needs to recharge...Please press <F or G> to recharge"
				elif key == 116:
					print "RoboCop needs to recharge...Please press <F or G> to recharge"
				elif key == 98:
					print "RoboCop needs to recharge...Please press <F or G> to recharge"
				elif key == 101:
					print "RoboCop needs to recharge...Please press <F or G> to recharge"
				elif key == 102:
					speech.mutterNoises(powerSupply)
				elif key == 103:
					powerSupply.charge()
			else:
				key = ord(getch())
				if key == 27:
					break
				elif key == 113:
					legs.run(powerSupply)
				elif key == 119:
					legs.walk(powerSupply)
				elif key == 104:
					legs.roundHouse(powerSupply)
				elif key == 112:
					arms.punch(powerSupply)
				elif key == 115:
					arms.shoot(powerSupply)
				elif key == 99:
					arms.handcuff(powerSupply)
				elif key == 100:
					powerSupply.power_Remaining()
				elif key == 97:
					vision.identifyCriminal(powerSupply)
				elif key == 116:
					vision.targetCriminal(powerSupply)
				elif key == 98:
					speech.yellHalt(powerSupply)
				elif key == 101:
					speech.readRights(powerSupply)
				elif key == 102:
					speech.mutterNoises(powerSupply)
				elif key == 103:
					powerSupply.charge()
	
	
powerSupply = PowerSupply()
legs = Legs()
arms = Arms()
vision = Vision()
speech = Speech()
test = Test()
controller = Controller()
controller.roboCopController(powerSupply)



