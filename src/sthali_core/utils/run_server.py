import os
import fastapi


def run(config, app_spec, app) -> type[fastapi.FastAPI]:
    app_specification_file_path = os.getenv("APP_SPECIFICATION_FILE_PATH") or "volume/app_specification_sample.json"
    config = config(app_specification_file_path)
    app_specification_dict = config.app_specification

    client = app(app_spec(**app_specification_dict))
    return client.app
