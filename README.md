# AI Cold Email Automation

An AI-powered cold email automation platform that streamlines personalized outreach by combining generative AI, campaign management, and automated email delivery. The application enables users to generate customized cold emails, create optimized subject lines, manage recipient data, and send emails securely through the Gmail API.

---

## Overview

AI Cold Email Automation is designed to simplify large-scale personalized outreach while maintaining high-quality communication. The platform leverages Google's Gemini model to generate tailored email content based on recipient information and integrates with Gmail for secure delivery.

The application also provides campaign tracking, recipient management, and an interactive Streamlit dashboard for monitoring outreach activities.

---

## Features

* AI-powered personalized email generation using Google Gemini
* Automatic subject line generation
* Gmail API integration for secure email delivery
* Dynamic recipient personalization
* Excel-based recipient import
* HTML email templates
* Campaign tracking with SQLite
* Streamlit dashboard for campaign management
* Logging and monitoring
* Modular backend architecture

---

## Technology Stack

| Category             | Technologies      |
| -------------------- | ----------------- |
| Programming Language | Python            |
| AI                   | Google Gemini API |
| Frontend             | Streamlit         |
| Backend              | Python            |
| Email Service        | Gmail API         |
| Database             | SQLite            |
| Data Processing      | Pandas            |
| Templates            | HTML              |
| Configuration        | python-dotenv     |

---

## System Architecture

```text
                 Excel Dataset
                       │
                       ▼
            Recipient Processing
                       │
                       ▼
          Personalization Engine
                       │
                       ▼
         Google Gemini AI Service
                       │
                       ▼
      Subject & Email Generation
                       │
                       ▼
          HTML Email Rendering
                       │
                       ▼
             Gmail API Service
                       │
                       ▼
               Email Delivery
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
   SQLite Database              Application Logs
```

---

## Project Structure

```text
ai-cold-email-automation/
│
├── backend/
│   ├── campaign.py
│   ├── ai_email_generator.py
│   ├── subject_generator.py
│   ├── gmail_service.py
│   ├── personalization.py
│   ├── email_generator.py
│   ├── database.py
│   ├── sender.py
│   ├── logger.py
│   └── config.py
│
├── frontend/
│   ├── app.py
│   ├── components/
│   ├── pages/
│   ├── assets/
│   └── db.py
│
├── templates/
│   └── cold_email.html
│
├── uploads/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .env.example
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/sinchanaraj21/ai-cold-email-automation.git
cd ai-cold-email-automation
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root and configure the required environment variables.

Example:

```env
PROJECT_NAME=AI Cold Email Automation
SENDER_NAME=Your Name
PORTFOLIO=https://yourportfolio.com
```

Store Gmail OAuth credentials inside the `credentials/` directory.

```
credentials/
├── client_secret.json
└── token.json
```

These files should never be committed to version control.

---

## Running the Application

Start an email campaign:

```bash
python backend/campaign.py
```

Launch the Streamlit dashboard:

```bash
streamlit run frontend/app.py
```

---

## Workflow

1. Import recipient information from an Excel spreadsheet.
2. Process and personalize recipient data.
3. Generate customized email content using Google Gemini.
4. Generate optimized subject lines.
5. Apply the HTML email template.
6. Deliver emails through the Gmail API.
7. Store campaign records in SQLite.
8. Monitor campaign activity through the Streamlit dashboard.

---

## Security

Sensitive files are excluded from version control.

Ignored resources include:

* `.env`
* `credentials/`
* `campaign.db`
* `logs/`
* `venv/`
* `__pycache__/`

---

## Future Enhancements

* Email scheduling
* Campaign analytics dashboard
* Multi-threaded email delivery
* Open and click tracking
* Support for multiple email providers
* PostgreSQL integration
* Docker deployment
* REST API
* AI-based follow-up email generation

---

## Author

**Sinchana Raj G**

Computer Science Engineering Student

Portfolio: https://sinchananalyst.netlify.app

LinkedIn: https://www.linkedin.com/in/sinchanaraj292004/

---

## License

This project is licensed under the MIT License.
