def process_square(x, y):
    quick_print("Processing square at")
    # if can_harvest():
    harvest()
    # till()
    plant(Entities.Bush)
    quick_print("Square processed.")


print("Starting farming bot...")

while True:
    quick_print("Farming...")

    FARM_DIMENSIONS = (get_world_size(), get_world_size())
    quick_print("Farm dimensions", FARM_DIMENSIONS)

    for row in range(FARM_DIMENSIONS[0]):
        move(East)
        for column in range(FARM_DIMENSIONS[1]):
            move(North)
            process_square(row, column)
