import os
from jinja2 import Environment, FileSystemLoader

from ai_email_generator import generate_ai_email

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_dir = os.path.join(BASE_DIR, "templates")

env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template("cold_email.html")


def generate_email(hr):

    prompt = f"""
Do NOT start with "Hi", "Hello", or "Dear".
Do NOT greet the recruiter.
The greeting is already provided.
Start immediately with the first paragraph.
Do NOT include "Best regards" or a signature.
You are writing a cold outreach email ON BEHALF OF the candidate.

The candidate is sending this email to a recruiter.

Candidate Information:

Name: Sinchana Raj G

Education:
Final-year Computer Science Engineering student

Experience:
Software Engineering Intern at Bharat Electronics Limited (BEL)

Projects:
- CARDEON (Spring Boot, React, FastAPI, XGBoost)
- AI and Data Analytics projects

Skills:
Python, Java, SQL, Spring Boot, React, Machine Learning, Docker, REST APIs, Power BI

Portfolio:
https://sinchananalyst.netlify.app

Recruiter Information:

Name: {hr["Full Name"]}
Company: {hr["Company Name"]}
Role: {hr["Title"]}

Instructions:

- Write the EMAIL FROM Sinchana TO the recruiter.
- Do NOT write as the recruiter.
- Do NOT compliment Sinchana.
- Do NOT say "I reviewed your portfolio."
- Do NOT include "Hi" or "Best regards".
- Mention the company naturally.
- Mention BEL internship
- Keep it between 130 and 170 words.
- Sound confident, genuine, and professional.
- Every email should be different.
- Return ONLY HTML paragraphs using <p>...</p>.
"""

    ai_email = generate_ai_email(prompt)

    return template.render(
        first_name=hr["First Name"],
        ai_email=ai_email,
        portfolio="https://sinchananalyst.netlify.app",
        sender_email="sinchanarajg21@gmail.com",
    )