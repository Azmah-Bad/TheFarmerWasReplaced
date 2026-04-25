while True:
	clear()
	for row in range(3):
		move(East)
		for column in range(3):
			move(North)
			if can_harvest():
				harvest()
				# till()
				plant(Entities.Bush)