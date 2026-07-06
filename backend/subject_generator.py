import random


def generate_subject(company):
    subjects = [
        "Application for Software Engineer Opportunities",
        "Final Year CSE Student | Resume Attached",
        "Seeking Entry-Level Software Engineer Role",
        "AI & Data Analytics Fresher | Resume Attached",
        f"Interested in Opportunities at {company}",
        f"Application for Technology Roles at {company}",
        f"Resume for Software Engineer Position - {company}"
    ]

    return random.choice(subjects)
