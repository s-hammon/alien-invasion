class GameStats:
	"""Track statistics for Alien Invasions."""

	def __init__(self, ai_game):
		"""Initialize statistics."""
		self.settings = ai_game.settings
		self.reset_stats()

		# Start Alien Invasion in an inactive state.
		self.game_active = True

		# Reads high score from a file.
		with open('high_score.txt') as file_object:
			read_high_score = file_object.read()
		self.high_score = int(read_high_score.rstrip())

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1

	def save_high_score(self):
		"""Saves high score to a file."""
		with open('high_score.txt', 'w') as file_object:
			file_object.write(str(self.high_score))