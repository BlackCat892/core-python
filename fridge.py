"""Demonstrate raiding a refrigirator."""

from contextlib import closing


class RefrigiratorRaider:
	"""Raid a fridge."""

	def open(self):
		print("Open fridge door.")

	def take(self,food):
		print("Finding {food}...")
		if food == 'deep fried pizza':
			raise RuntimeError("Health warning!")
		print(f"Taking {food}")

	def close(self):
		print("Close the fridge door.")

	def raid(self,food):
		with closing(RefrigiratorRaider()) as r:
			pass
		r.open()
		r.take(food)
