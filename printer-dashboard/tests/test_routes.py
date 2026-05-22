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


def test_ok_printer_shown_with_toner_percentage(client):
    response = client.get("/")
    body = response.data.decode()
    assert "Recepção" in body
    assert "72%" in body


def test_inaccessible_printer_shown_with_inacessivel_label(client):
    response = client.get("/")
    body = response.data.decode()
    assert "Depósito" in body
    assert "Inacessível" in body


def test_inaccessible_printer_toner_cell_has_distinct_style(client):
    response = client.get("/")
    body = response.data.decode()
    assert 'style=' in body
    inacessivel_pos = body.index("Inacessível")
    style_pos = body.rindex('style=', 0, inacessivel_pos)
    assert style_pos > 0


def test_inaccessible_printer_appears_after_accessible_printers(client):
    response = client.get("/")
    body = response.data.decode()
    pos_accessible = body.index("Sala de Reunião")
    pos_inaccessible = body.index("Depósito")
    assert pos_accessible < pos_inaccessible


def test_dashboard_shows_all_printers_when_all_accessible(tmp_path):
    data = [{"label": "Recepção", "ip": "192.168.1.11"}]  # ok only
    f = tmp_path / "printers.json"
    f.write_text(json.dumps(data))

    app = create_app(str(f))
    app.config["TESTING"] = True
    with app.test_client() as c:
        response = c.get("/")
        body = response.data.decode()
        assert "Recepção" in body
        assert "72%" in body
        assert "Inacessível" not in body
