from click.testing import CliRunner

from aspect_ratio_too.cli import cli


def test_ratio():
    result = CliRunner().invoke(cli, ["ratio", "1920", "1080"])
    assert result.exit_code == 0
    assert result.output.strip() == "1.7777777777777777"


def test_ratio_str():
    result = CliRunner().invoke(cli, ["ratio-str", "1920", "1080"])
    assert result.exit_code == 0
    assert result.output.strip() == "16:9"


def test_width_to_height():
    result = CliRunner().invoke(cli, ["width-to-height", "16", "9", "1920"])
    assert result.exit_code == 0
    assert result.output.strip() == "1080"


def test_height_to_width():
    result = CliRunner().invoke(cli, ["height-to-width", "16", "9", "1080"])
    assert result.exit_code == 0
    assert result.output.strip() == "1920"


def test_width_to_dimensions():
    result = CliRunner().invoke(cli, ["width-to-dimensions", "16", "9", "1920"])
    assert result.exit_code == 0
    assert result.output.strip() == "1920x1080"


def test_height_to_dimensions():
    result = CliRunner().invoke(cli, ["height-to-dimensions", "16", "9", "1080"])
    assert result.exit_code == 0
    assert result.output.strip() == "1920x1080"
