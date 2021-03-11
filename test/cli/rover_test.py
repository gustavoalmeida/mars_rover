from cli.rover import Rover


def test_initial_position():
    initial_position = (4, 2, "EAST")
    rover = Rover(initial_position)
    assert rover.position == (4, 2, "EAST")


def test_move_rover_forward():
    initial_position = (4, 2, "EAST")
    rover = Rover(initial_position)
    rover.move("F")
    assert rover.position == (5, 2, "EAST")


def test_move_rover_backward():
    initial_position = (4, 2, "EAST")
    rover = Rover(initial_position)
    rover.move("B")
    assert rover.position == (3, 2, "EAST")


def test_rotate_rover_left():
    initial_position = (4, 2, "EAST")
    rover = Rover(initial_position)
    rover.move("L")
    assert rover.position == (4, 2, "NORTH")


def test_rotate_rover_right():
    initial_position = (4, 2, "EAST")
    rover = Rover(initial_position)
    rover.move("R")
    assert rover.position == (4, 2, "SOUTH")


def test_rover_goto():
    initial_position = (4, 2, "EAST")
    rover = Rover(initial_position)
    rover.goto("FLFFFRFLB")
    assert rover.position == (6, 4, "NORTH")
