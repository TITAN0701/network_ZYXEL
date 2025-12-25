from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    base_url: str = os.environ.get("BASE_URL", "https://the-internet.herokuapp.com")
    headless: bool = os.environ.get("HEADLESS", "1") != "0"
    slowmo_ms: int = int(os.environ.get("SLOWMO_MS", "0"))
    login_username: str = os.environ.get("LOGIN_USERNAME", "tomsmith")
    login_password: str = os.environ.get("LOGIN_PASSWORD", "SuperSecretPassword!")
    invalid_username: str = os.environ.get("LOGIN_INVALID_USERNAME", "wrong")
    invalid_password: str = os.environ.get("LOGIN_INVALID_PASSWORD", "wrong")
    login_error_message: str = os.environ.get(
        "LOGIN_ERROR_MESSAGE",
        "Your username is invalid!",
    )


settings = Settings()
