import re
import os

def extract_emails(input_file: str, output_file: str) -> None:
    if not os.path.exists(input_file):
        print(f"[ERROR] File '{input_file}' not found.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"[INFO] File read: '{input_file}'")

    email_pattern = r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'
    found_emails  = re.findall(email_pattern, content)
    unique_emails = list(dict.fromkeys(found_emails))

    if not unique_emails:
        print("[INFO] No email addresses found.")
        return

    print(f"[INFO] {len(unique_emails)} unique email(s) found:")
    for email in unique_emails:
        print(f"       • {email}")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Total emails found: {len(unique_emails)}\n")
        f.write("=" * 40 + "\n")
        for email in unique_emails:
            f.write(email + "\n")

    print(f"\n[SUCCESS] Emails saved to: '{output_file}'")


if __name__ == "__main__":
    sample_input = "sample_input.txt"
    sample_text  = """
    Hello this is a test file.
    Contact: ali@gmail.com or sara.khan@yahoo.com
    Office email: info@company.org
    Invalid emails: notanemail, @missing.com
    Duplicate: ali@gmail.com
    Support: help@support.net
    Pakistan: admin@website.com.pk
    """

    with open(sample_input, "w", encoding="utf-8") as f:
        f.write(sample_text)
    print(f"[DEMO] Sample input file created: '{sample_input}'\n")

    extract_emails(
        input_file  = sample_input,
        output_file = "extracted_emails.txt"
    )
