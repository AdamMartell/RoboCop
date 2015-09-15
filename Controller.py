from Parts import *

class Controller:
	def roboCopController(self, powerSupply):
		while True:
			try:
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
						powerSupply.charge(10)
					elif key == 105:
						stats.displayBodyCount()
					elif key ==107:
						print "RoboCop needs to recharge...Please press <F or G> to recharge"
					elif key ==108:
						print "RoboCop needs to recharge...Please press <F or G> to recharge"
				else:
					key = ord(getch())
					if key == 27:
						break
					elif key == 113:
						legs.run(powerSupply)
					elif key == 119:
						legs.walk(powerSupply)
					elif key == 104:
						legs.roundHouse(powerSupply, stats)
					elif key == 112:
						arms.punch(powerSupply)
					elif key == 115:
						arms.shoot(powerSupply)
					elif key == 99:
						arms.handcuff(powerSupply)
					elif key == 100:
						powerSupply.displayPowerRemaining()
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
						powerSupply.charge(10)
					elif key == 105:
						stats.displayBodyCount()
					elif key ==107:
						leftArm.shoot(powerSupply)
					elif key ==108:
						rightArm.shoot(powerSupply)
					
			except Exception:
				print "An error has occurred.  Please try discharging some power and trying again.  If this does not help please contact your local RoboCop distributor"
			
powerSupply = PowerSupply()
rightArm = RightArm()
legs = Legs()
arms = Arms()
vision = Vision()
speech = Speech()
stats = Stats()
leftArm = LeftArm()
controller = Controller()