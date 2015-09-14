
class Robot:
	def __init__(self):
		
	class PowerSupply:
		def usePower(self, amountUsed):
			self.power = self.power - amountUsed
		
		def powerRemaining(self):
			print self.power
		
	class Legs(PowerSupply):
		def run(self):
			self.usePower(2)
		def walk(self):
			self.usePower(1)
			
	class Arms:
		def shoot(self):
		
		def punch(self):
		
		def write(self):
		
		def handcuff(self):
		
	class Processor:
		def decisionMaking(self):
		
		def crimeNotCrime (self):
		
		
	class Vision:
		def target(self):
		
		def IdentifyCriminal(self):
		
		
	class Speech:
		def mirandaRights(self):
	
roboCop = PowerSupply()
roboLegs = Legs()
roboCop.powerRemaining()
roboCop.usePower(3)
roboCop.powerRemaining()		
roboCop.usePower(5)
roboCop.powerRemaining()
roboLegs.run()
roboCop.powerRemaining()