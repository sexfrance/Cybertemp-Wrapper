from cybertemp import CyberTemp

def main():
    # Initialize client (with or without API key)
    client = CyberTemp(debug=True)  # Free tier
    # client = CyberTemp(api_key="your_api_key_here")  # Premium tier

    # 1. Get available domains
    print("\n=== Available Domains ===")
    domains = client.get_domains()
    if domains:
        print(f"Available domains: {domains}")

    # 2. Check emails in a mailbox
    test_email = "test@cybertemp.xyz"
    print(f"\n=== Checking Mailbox: {test_email} ===")
    emails = client.get_email_content(test_email, max_retries=3, delay_between_retries=2.0)
    if emails:
        for email in emails:
            print(f"ID: {email['id']}")
            print(f"From: {email['from']}")
            print(f"Subject: {email['subject']}")
            print(f"Date: {email['date']}")
            print(f"Text Content:: {email['text']}...")
            print(f"Html Content:: {email['html']}...")
            print("---")

    # 3. Get specific email by ID
    if emails and len(emails) > 0:
        email_id = emails[0]['id']
        print(f"\n=== Getting Email Content for ID: {email_id} ===")
        email_content = client.get_email_content_by_id(email_id)
        if email_content:
            print(f"Subject: {email_content['subject']}")
            print(f"Text Content:: {email_content['text']}...")
            print(f"Html Content:: {email_content['html']}...")

    # 4. Search for email with specific subject
    print("\n=== Searching for Verification Email ===")
    mail_id = client.get_mail_by_subject(
        email=test_email,
        subject_contains="Verification",
        max_attempts=5,
        delay_between_retries=1.5
    )
    if mail_id:
        print(f"Found verification email with ID: {mail_id}")

    # 5. Extract URL from email
    print("\n=== Extracting URL from Email ===")
    url = client.extract_url_from_message(
        email=test_email,
        subject_contains="Verification",
        url_pattern=r'https://[^\s<>"]+',
        max_attempts=5,
        delay_between_retries=1.5
    )
    if url:
        print(f"Extracted URL: {url}")

    # 6. Check API balance (premium only)
    if hasattr(client, 'api_key') and client.api_key:
        print("\n=== Checking API Balance ===")
        balance = client.get_balance()
        if balance:
            print(f"Remaining credits: {balance['balance']}")

if __name__ == "__main__":
    main()
