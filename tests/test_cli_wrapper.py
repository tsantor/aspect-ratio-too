import importlib

from aspect_ratio_too import cli_wrapper


def test_wrapper_shows_install_hint_for_missing_cli_deps(monkeypatch, capsys):
    def _raise_missing(_name):
        message = "No module named 'click'"
        raise ModuleNotFoundError(message, name="click")

    monkeypatch.setattr(importlib, "import_module", _raise_missing)

    exit_code = cli_wrapper.main([])
    captured = capsys.readouterr()

    assert exit_code == 1
    assert "aspect-ratio-too[cli]" in captured.err


def test_wrapper_delegates_to_cli_module(monkeypatch):
    class _CliModule:
        @staticmethod
        def main(args):
            assert args == ["ratio", "1920", "1080"]
            return 0

    monkeypatch.setattr(importlib, "import_module", lambda _name: _CliModule)

    assert cli_wrapper.main(["ratio", "1920", "1080"]) == 0
