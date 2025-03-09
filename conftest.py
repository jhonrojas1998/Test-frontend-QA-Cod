import pytest
import shutil
import os
from playwright.sync_api import BrowserContext

@pytest.fixture(scope="function")
def context(browser) -> BrowserContext:
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},  # Pantalla completa
        storage_state=None,  # Evita almacenar cookies/sesión (modo incógnito)
        record_video_dir="videos/",
    )
    return context

@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session):
    """Borra la carpeta allure-results solo si NO se ejecuta desde el Explorador de Pruebas de Playwright en VS Code."""
    if "VSCODE_PID" not in os.environ:  # Detecta si es desde VS Code
        results_dir = "allure-results"
        if os.path.exists(results_dir):
            shutil.rmtree(results_dir)
        os.makedirs(results_dir)
        
 # Borrar videos si existe
    videos_dir = "videos"
    if os.path.exists(videos_dir):
        shutil.rmtree(videos_dir)
    os.makedirs(videos_dir)