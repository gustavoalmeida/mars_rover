def parse_command(current_position, command):
    directions = ["NORTH", "EAST", "SOUTH", "WEST"]

    (x, y, direction) = current_position

    current_direction_idx = directions.index(direction)
    # Move forward on current heading
    if command == "F":
        if direction == "NORTH":
            y = y + 1
        if direction == "EAST":
            x = x + 1
        if direction == "SOUTH":
            y = y - 1
        if direction == "WEST":
            x = x - 1
    # Move backward on current heading
    if command == "B":
        if direction == "NORTH":
            y = y - 1
        if direction == "EAST":
            x = x - 1
        if direction == "SOUTH":
            y = y + 1
        if direction == "WEST":
            x = x + 1
    # Rotate left by 90 degrees
    if command == "L":
        if current_direction_idx > 0:
            next_direction_idx = current_direction_idx - 1
        else:
            next_direction_idx = len(directions) - 1
        direction = directions[next_direction_idx]
    # Rotate right by 90 degrees
    if command == "R":
        if current_direction_idx < len(directions) - 1:
            next_direction_idx = current_direction_idx + 1
        else:
            next_direction_idx = 0
        direction = directions[next_direction_idx]

    current_position = (x, y, direction)

    return current_position


def split_commands(commands):
    return [command for command in commands]
