"""Settings module"""
import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
	envvar_prefix="ECOBE",
	preload=[os.path.join(HERE, "default.toml")],
	settings_files=["settings.toml", ".secrets.toml"],
	environments=["development", "production", "testing"],
	env_switcher="ECOBE_ENV",
	load_dotenv=False,
)
