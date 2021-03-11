from click.testing import CliRunner
from rover import ignite

def test_rover():
    runner = CliRunner()
    result = runner.invoke(ignite, input="y\nexit")
    assert result.exit_code == 0
    