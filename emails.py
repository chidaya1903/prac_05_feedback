"""
Emails
Estimate: 20 minutes
Actual:   __ minutes
"""

def main():
    email_to_name: dict[str, str] = {}

    email = input("Email: ").strip()
    while email:
        default_name = extract_name_from_email(email)
        answer = input(f"Is your name {default_name}? (Y/n) ").strip()
        if answer and answer[0].lower() != "y":
            default_name = input("Name: ").strip().title()
        email_to_name[email] = default_name
        email = input("Email: ").strip()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email: str) -> str:
    """Return a title-cased best-guess name from an email like 'first.last@host'."""
    local = email.split("@", 1)[0]
    parts = [p for p in local.replace(".", " ").replace("_", " ").split() if p]
    return " ".join(parts).title() if parts else "User"


if __name__ == "__main__":
    main()
