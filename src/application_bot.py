"""Automation for filling out job applications on LinkedIn."""

from pathlib import Path
from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver


def apply_to_job(driver: WebDriver, job_url: str, name: str, phone: str,
                 resume_path: Path, cover_letter_path: Optional[Path] = None) -> None:
    """Navigate to the given job URL and attempt to submit an application.

    The caller must ensure that the driver is logged in to LinkedIn and
    has already navigated to the job page. This function only sketches
    out the automation steps. Additional handling is required for
    LinkedIn's dynamic forms and CAPTCHA.
    """
    driver.get(job_url)
    # TODO: implement the steps using Selenium to click "Apply", fill in
    # fields, upload files, etc.
    # This typically involves locating HTML elements with driver.find_element
    # and sending keys/clicking as appropriate.
    pass
