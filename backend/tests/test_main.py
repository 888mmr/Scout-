def test_app_smoke(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg://scout:test@localhost:5432/scout")
    from fastapi.testclient import TestClient

    from scout.main import app

    with TestClient(app) as client:
        response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"name": "SCOUT"}
