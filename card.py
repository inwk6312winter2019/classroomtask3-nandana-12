class card():
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
	
	def __init__(self,suit = 2,rank = 0):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return f"The rank is {card.rank_names[self.rank]} and the suit is {card.suit_names[self.suit]}"

	def __lt__(self,other):
		return self.rank < other.rank

	def __gt__(self,other):
		return self.rank>other.rank

	def __et__(self,other):
		return self.rank==other.rank

ace_spade = card(3,1)
queen_hearts = card(2,12)
print(ace_spade)
print(queen_heart)

