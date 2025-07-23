"""Utilities for sending notification emails."""

import smtplib
from pathlib import Path
from email.message import EmailMessage
from typing import List


def send_email(smtp_server: str, smtp_port: int, username: str, password: str,
               to_address: str, subject: str, body: str, attachments: List[str] = None) -> None:
    msg = EmailMessage()
    msg["From"] = username
    msg["To"] = to_address
    msg["Subject"] = subject
    msg.set_content(body)

    attachments = attachments or []
    for path in attachments:
        with open(path, "rb") as f:
            data = f.read()
            msg.add_attachment(data, maintype="application", subtype="octet-stream", filename=Path(path).name)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(username, password)
        server.send_message(msg)
