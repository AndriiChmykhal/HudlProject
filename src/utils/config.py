import os
from dotenv import load_dotenv

load_dotenv()

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