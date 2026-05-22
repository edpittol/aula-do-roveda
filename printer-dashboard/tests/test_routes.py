import json
import pytest
from app import create_app


@pytest.fixture
def printers_json(tmp_path):
    data = [
        {"label": "Sala de Reunião", "ip": "192.168.1.10"},  # critical (5%)
        {"label": "Recepção",        "ip": "192.168.1.11"},  # ok (72%)
        {"label": "Depósito",        "ip": "192.168.1.99"},  # inaccessible (None)
    ]
    f = tmp_path / "printers.json"
    f.write_text(json.dumps(data))
    return str(f)


@pytest.fixture
def client(printers_json):
    app = create_app(printers_json)
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_critical_printer_appears_in_response(client):
    response = client.get("/")
    assert response.status_code == 200
    body = response.data.decode()
    assert "Sala de Reunião" in body
    assert "5%" in body


def test_ok_printer_not_listed_as_critical(client):
    response = client.get("/")
    body = response.data.decode()
    assert "Recepção" not in body


def test_inaccessible_printer_omitted(client):
    response = client.get("/")
    body = response.data.decode()
    assert "Depósito" not in body


def test_all_ok_message_when_no_criticals(tmp_path):
    data = [{"label": "Recepção", "ip": "192.168.1.11"}]  # ok only
    f = tmp_path / "printers.json"
    f.write_text(json.dumps(data))

    app = create_app(str(f))
    app.config["TESTING"] = True
    with app.test_client() as c:
        response = c.get("/")
        body = response.data.decode()
        assert "Todas as impressoras estão OK" in body
