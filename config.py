from pydantic_settings import BaseSettings
from pydantic import EmailStr

class Settings(BaseSettings):
    app_name: str = "Book API"
    debug: bool = True
    admin_email: EmailStr = "admin@example.com"

    model_config = {
        "extra": "forbid",
        "env_file": ".env",
        "frozen": True
    }

_settings_instance: Settings | None = None

def get_settings() -> Settings:
    global _settings_instance
    if _settings_instance is None:
        _settings_instance = Settings()
    return _settings_instance