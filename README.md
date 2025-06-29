# AIJobSearch

This project demonstrates a proof-of-concept automation pipeline for job applications on LinkedIn. It includes:

1. **Job search** using Selenium to scrape LinkedIn results.
2. **Resume tailoring** and **cover letter generation** using the OpenAI API.
3. **Email notifications** so you can review applications before submission.
4. Skeleton code for automated form filling on LinkedIn job pages.

> **Warning**: Automating interactions with LinkedIn may violate their Terms of Service. Use this code responsibly and only for personal/educational purposes.

## Running

1. Install dependencies such as `selenium` and `openai`.
2. Populate `src/config.py` with your credentials and SMTP details.
3. Prepare your base resume in `resume.txt`.
4. Run `python -m src.main` and follow the prompts.

The script will prepare a customized resume and cover letter for each job found and email them to you for review before attempting to submit the application.
