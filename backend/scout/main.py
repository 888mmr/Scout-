from fastapi import FastAPI

from scout.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name)

    @app.get("/")
    def root() -> dict[str, str]:
        return {"name": settings.app_name}

    return app


app = create_app()
