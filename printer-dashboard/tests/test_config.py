import json
import pytest
from pathlib import Path
from config import load_config


def test_load_config_raises_on_invalid_json(tmp_path):
    config_file = tmp_path / "printers.json"
    config_file.write_text("not valid json {{{")

    with pytest.raises(ValueError, match="printers.json"):
        load_config(str(config_file))


def test_load_config_raises_on_wrong_format(tmp_path):
    config_file = tmp_path / "printers.json"
    config_file.write_text(json.dumps({"not": "a list"}))

    with pytest.raises(ValueError, match="printers.json"):
        load_config(str(config_file))


def test_load_config_raises_on_missing_file(tmp_path):
    with pytest.raises(FileNotFoundError, match="printers.json"):
        load_config(str(tmp_path / "printers.json"))


def test_load_config_returns_list_of_printers(tmp_path):
    config_file = tmp_path / "printers.json"
    config_file.write_text(json.dumps([
        {"label": "Printer A", "ip": "192.168.1.10"},
        {"label": "Printer B", "ip": "192.168.1.11"},
    ]))

    result = load_config(str(config_file))

    assert result == [
        {"label": "Printer A", "ip": "192.168.1.10"},
        {"label": "Printer B", "ip": "192.168.1.11"},
    ]
