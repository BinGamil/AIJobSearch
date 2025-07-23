"""Configuration constants for the AI Job Search application."""

from pathlib import Path

# Provide your LinkedIn credentials and email settings here. In practice, you
# may want to load these from environment variables or a secure vault.

LINKEDIN_USERNAME = "your_email@example.com"
LINKEDIN_PASSWORD = "your_password"

SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 465
EMAIL_USERNAME = "your_email@example.com"
EMAIL_PASSWORD = "email_password"
NOTIFY_EMAIL = "notify@example.com"

# Path to your base resume file
BASE_RESUME_PATH = Path("resume.txt")
