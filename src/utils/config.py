import os
from dotenv import load_dotenv

load_dotenv()

REQUIRED_ENV_VARS = ["VALID_EMAIL", "VALID_PASSWORD"]

missing_vars = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]

if missing_vars:
    raise EnvironmentError(
        f"Missing required environment variables: {', '.join(missing_vars)}.\n"
        "Please create a .env file in the root directory and add valid credentials for login:\n"
        'VALID_EMAIL="your_email@example.com"\n'
        'VALID_PASSWORD="your_password"'
    )

valid_email = os.getenv("VALID_EMAIL")
valid_password = os.getenv("VALID_PASSWORD")
invalid_email = "@com"
invalid_password = "1"
wrong_email = "test+123@test.com"
wrong_password = "Qwert123!"

base_url = "https://www.hudl.com"
privacy_policy_url = "https://www.hudl.com/privacy"
terms_of_service_url = "https://www.hudl.com/terms"

screen_resolution = {"width": 1920, "height": 1080}
