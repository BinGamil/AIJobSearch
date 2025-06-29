"""Main entry point for the AI Job Search application."""

from pathlib import Path
from selenium import webdriver

from . import config
from .job_search import search_jobs
from .resume_utils import ResumeProcessor
from .email_utils import send_email
from .application_bot import apply_to_job


def run():
    # Initialize Selenium driver (example uses Chrome)
    driver = webdriver.Chrome()
    # User must log in manually or you can automate login here

    keywords = input("Job keywords: ")
    location = input("Location: ")

    job_postings = search_jobs(driver, keywords, location)
    processor = ResumeProcessor(api_key="YOUR_OPENAI_API_KEY", base_resume_path=config.BASE_RESUME_PATH)

    for job in job_postings:
        resume_out = Path(f"resume_{job.company}_{job.title}.txt")
        processor.generate_custom_resume(job.description, resume_out)
        cover_letter_out = Path(f"cover_{job.company}_{job.title}.txt")
        processor.generate_cover_letter(job.description, cover_letter_out)

        body = f"Prepared application for {job.title} at {job.company}. Review attached files and reply 'Good to send' to submit."
        send_email(
            config.SMTP_SERVER,
            config.SMTP_PORT,
            config.EMAIL_USERNAME,
            config.EMAIL_PASSWORD,
            config.NOTIFY_EMAIL,
            subject=f"Application ready: {job.title} at {job.company}",
            body=body,
            attachments=[str(resume_out), str(cover_letter_out)],
        )

        # Wait for user's manual confirmation outside of this script
        confirm = input(f"Send application for {job.title} at {job.company}? (y/N): ")
        if confirm.lower().startswith("y"):
            apply_to_job(driver, job.url, name=config.EMAIL_USERNAME, phone="000-000-0000",
                         resume_path=resume_out, cover_letter_path=cover_letter_out)

    driver.quit()


if __name__ == "__main__":
    run()
