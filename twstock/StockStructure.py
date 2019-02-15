from collections import namedtuple

class Quotes():
	QUOTETUPLE = namedtuple('Quotes', ['date', 'open', 'high', 'low','close','change',
                                		'increse','transaction','amount','pe_ratio'])
	quotes = []

	def __init__(self):
		pass

	def add(self,data):
		self.quotes.append(self.QUOTETUPLE(*data))

	def __iter__(self):
		return iter(self.quotes)

	@property
	def open(self):
		return [q.open for q in self.quotes]

	@property
	def high(self):
		return [q.high for q in self.quotes]

	@property
	def low(self):
		return [q.low for q in self.quotes]

	@property
	def close(self):
		return [q.close for q in self.quotes]

	@property
	def change(self):
		return [q.change for q in self.quotes]

	@property
	def increse(self):
		return [q.increase for q in self.quotes]

	@property
	def transaction(self):
		return [q.transaction for q in self.quotes]

	@property
	def amount(self):
		return [q.amount for q in self.quotes]

	@property
	def pe_ratio(self):
		return [q.pe_ratio for q in self.quotes]

