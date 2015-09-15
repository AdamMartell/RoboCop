from Parts import *
from Controller import Controller

powerSupply = PowerSupply()
legs = Legs()
arms = Arms()
vision = Vision()
speech = Speech()
stats = Stats()
leftArm = LeftArm()
rightArm = RightArm()
controller = Controller()
controller.roboCopController(powerSupply)