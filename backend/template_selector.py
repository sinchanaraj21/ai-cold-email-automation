ENTERPRISE_COMPANIES = [
    "Microsoft",
    "Google",
    "Amazon",
    "Intel",
    "SAP",
    "Cisco",
    "Oracle",
    "IBM",
    "Dell",
    "Adobe",
    "NVIDIA",
    "Qualcomm",
]

STARTUP_KEYWORDS = [
    "Labs",
    "AI",
    "Technologies",
    "Tech",
    "Systems",
]


def get_company_type(company):

    company = company.lower()

    for enterprise in ENTERPRISE_COMPANIES:
        if enterprise.lower() in company:
            return "enterprise"

    for keyword in STARTUP_KEYWORDS:
        if keyword.lower() in company:
            return "startup"

    return "general"