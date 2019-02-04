class card():
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
	
	def __init__(self,suit = 2,rank = 0):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return f"The rank is {card.rank_names[self.rank]} and the suit is {card.suit_names[self.suit]}"

ace_spade = card(3,1)
print(ace_spade)