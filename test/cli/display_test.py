from click.testing import CliRunner
from rover import ignite

import pytest


def test_using_current_position():
    runner = CliRunner()
    result = runner.invoke(ignite, input='y\nFLFFFRFLB\nexit')
    with open("./test/data/current_position.txt", "r") as myfile:
        expected = myfile.read()
    assert result.output == expected

def test_with_new_initial_position():
    runner = CliRunner()
    result = runner.invoke(ignite, input='n\n4\n3\nEAST\nn\n4\n2\nEAST\ny\nFLFFFRFLB\nexit')
    with open("./test/data/new_initial_position.txt", "r") as myfile:
        expected = myfile.read()
    assert result.output == expected
    