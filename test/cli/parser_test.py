from cli.parser import split_commands, parse_command


def test_input_parser():
    value = "FLFFFRFLB"
    expected = [w for w in "FLFFFRFLB"]
    assert expected == split_commands(value)


def test_parse_command():
    directions = ["NORTH", "EAST", "SOUTH", "WEST"]

    current_position = (x, y, direction) = (4, 2, "EAST")

    # Move forward on current heading
    command = "F"
    expected_position = (x + 1, y, "EAST")
    assert expected_position == parse_command(current_position, command)

    # Move backward on current heading
    command = "B"
    expected_position = (x - 1, y, "EAST")
    assert expected_position == parse_command(current_position, command)

    # Rotate left by 90 degrees
    command = "L"
    expected_position = (x, y, "NORTH")
    assert expected_position == parse_command(current_position, command)

    # Rotate left by 90 degrees
    command = "R"
    expected_position = (x, y, "SOUTH")
    assert expected_position == parse_command(current_position, command)
