import os
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent


def getenv():
    environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
    return environ.Env(
        DEBUG=(bool, False),

    )
