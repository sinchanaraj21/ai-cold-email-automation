def generate_intro(company, hr_title):

    title = str(hr_title).lower()

    if "talent" in title:
        return (
            f"I recently came across {company} and would appreciate being considered "
            "for any current or upcoming Software Engineer opportunities."
        )

    elif "recruit" in title:
        return (
            f"I'm reaching out to express my interest in entry-level Software Engineer "
            f"roles at {company}."
        )

    elif "hrbp" in title:
        return (
            f"I would be grateful if you could consider my profile for suitable "
            f"engineering opportunities within {company}."
        )

    elif "manager" in title:
        return (
            f"I admire the work being done at {company} and would appreciate the "
            "opportunity to contribute as a Software Engineer."
        )

    else:
        return (
            f"I recently came across {company} while exploring innovative technology "
            "companies and wanted to introduce myself."
        )