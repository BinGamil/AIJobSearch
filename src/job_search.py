from dataclasses import dataclass
from typing import List
from urllib.parse import quote_plus

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This module provides utilities to search LinkedIn for jobs.
# It uses Selenium for browser automation. Users must provide
# their own LinkedIn credentials and ensure this usage complies
# with LinkedIn's Terms of Service.

@dataclass
class JobPosting:
    title: str
    company: str
    url: str
    description: str


def search_jobs(driver, keywords: str, location: str) -> List[JobPosting]:
    """Search LinkedIn for jobs using the provided Selenium driver.

    The driver must already be authenticated. The function navigates to
    LinkedIn's job search page, collects the listings on the first page,
    and extracts each job's title, company, URL and full description.
    """
    jobs: List[JobPosting] = []

    query = (
        "https://www.linkedin.com/jobs/search/?keywords="
        f"{quote_plus(keywords)}&location={quote_plus(location)}"
    )
    driver.get(query)

    wait = WebDriverWait(driver, 10)
    result_items = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "ul.jobs-search__results-list li")
        )
    )

    for item in result_items:
        try:
            link = item.find_element(By.CSS_SELECTOR, "a.job-card-list__title")
            title = link.text.strip()
            url = link.get_attribute("href")
            company_el = item.find_element(By.CSS_SELECTOR, "a.job-card-container__company-name")
            company = company_el.text.strip()

            driver.get(url)
            desc_el = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.description")
                )
            )
            description = desc_el.text.strip()
            jobs.append(JobPosting(title=title, company=company, url=url, description=description))
            driver.back()
        except Exception:
            continue

    return jobs
