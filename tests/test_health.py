from app.main import healthcheck


def test_healthcheck():
    assert healthcheck() == {"status": "ok", "service": "whitestones"}
