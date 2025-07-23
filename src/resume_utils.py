"""Utilities for modifying resumes and generating cover letters."""

from pathlib import Path
from typing import Optional

import openai


class ResumeProcessor:
    def __init__(self, api_key: str, base_resume_path: Path):
        """Initialize with an OpenAI API key and path to the base resume."""
        openai.api_key = api_key
        self.base_resume_path = base_resume_path

    def _load_resume_text(self) -> str:
        return self.base_resume_path.read_text()

    def generate_custom_resume(self, job_description: str, output_path: Path) -> None:
        """Use OpenAI to tailor the resume for the job description."""
        prompt = (
            "Given the following resume, rewrite it so that it highlights \
            skills and experience relevant to this job description:\n\n"
            f"Resume:\n{self._load_resume_text()}\n\n"
            f"Job description:\n{job_description}\n"
            "Rewrite the resume accordingly."
        )
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
        )
        output_path.write_text(response["choices"][0]["text"].strip())

    def generate_cover_letter(self, job_description: str, output_path: Path, user_info: Optional[str] = None) -> None:
        """Generate a cover letter based on resume and job description."""
        prompt = (
            "Write a professional cover letter for the following job description."
            " Use the candidate information below if provided.\n\n"
            f"Candidate info:\n{user_info or 'N/A'}\n\n"
            f"Job description:\n{job_description}\n"
        )
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=800,
        )
        output_path.write_text(response["choices"][0]["text"].strip())
