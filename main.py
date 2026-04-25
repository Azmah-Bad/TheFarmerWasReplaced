while True:
	clear()

	FARM_DIMENSIONS = (3, 3)

	for row in range(FARM_DIMENSIONS[0]):
		move(East)
		for column in range(FARM_DIMENSIONS[1]):
			move(North)
			if can_harvest():
				harvest()
				# till()
				plant(Entities.Bush)