"""
# Object Oriented Programming
"""

class Player(object):
	job = 'Pemain sepak bola'

	def __init__(self, name, age):
		self.name = name
		self.age = age

	@property
	def infoPlayer(self):
		return self.name + ' berumur ' + self.age

	@infoPlayer.setter
	def infoPlayer(self, data):
		name, age = data.split(' ')
		self.name = name
		self.age  = age

player = Player('Maradona', '30')
player.infoPlayer = 'Paul 100'
print(player.infoPlayer)
