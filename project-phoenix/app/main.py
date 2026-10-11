"""FastAPI entry point for Project Phoenix."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = FastAPI(title="Project Phoenix")


@app.get("/api/health")
def health() -> dict[str, str]:
    """Return the local service health state."""
    return {"status": "ok"}


frontend_directory = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/", StaticFiles(directory=frontend_directory, html=True), name="frontend")
