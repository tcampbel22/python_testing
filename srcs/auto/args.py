class Args:
	def __init__(self, num):
		self.num = num

	@staticmethod
	def count_nums(*args, **kwargs):
		print(args)
		for key, value in kwargs.items():
			print(f"{key}, {value}")

	def __repr__(self):
		return f"(num={self.num})"

	def __str__(self):
		return f"(The number for this class is {self.num})"

	def __eq__(self, other):
		if isinstance(other, Args):
			return self.num == other.num
		return False

	@staticmethod
	def is_div_two(num: int) -> bool:
		return num % 2 == 0

if __name__ == "__main__":
	b = Args(10)
	c = Args(11)
	Args.count_nums(1, 2, 7, 4, 5, a=10, g=99)
	print(repr(b))
	print(c == b)
	print(str(b))
