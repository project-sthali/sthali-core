"""{...}."""

import os

import fastapi
import uvicorn

from .base import App, AppSpecification, Config


def run(config: type[Config], app_spec: type[AppSpecification], app: type[App]) -> fastapi.FastAPI:
    app_specification_file_path = os.getenv("APP_SPECIFICATION_FILE_PATH") or "volume/app_specification_sample.json"
    client_config = config(app_specification_file_path)
    client_app = app(app_spec(**client_config.app_specification))
    return client_app.app


def main(app: fastapi.FastAPI, port: int = 8000):
    uvicorn.run(app, host="0.0.0.0", port=port)
