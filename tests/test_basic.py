from flask import Flask
from flask.testing import FlaskClient, FlaskCliRunner
import pytest
from api import create_app
from werkzeug.wrappers.response import Response


@pytest.fixture()
def app() -> Flask:
    app = create_app(testing=True)
    yield app

@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()

@pytest.fixture()
def runner(app: Flask) -> FlaskCliRunner:
    return app.test_cli_runner()

def test_app_config(app: Flask):
    assert app.config["TESTING"] == True

def test_request_example(client: FlaskClient):
    response : Response = client.get("/")
    assert response.json == {"hello": "world"}
