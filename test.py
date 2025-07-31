
from cybertemp import CyberTemp

def main():
    # Initialize client (API key required)
    client = CyberTemp(api_key="your_api_key_here", debug=True)

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
        email_content = client.get_email_content_by_id(test_email, email_id)
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
        url_pattern=r'https://[^\s<>\"]+',
        max_attempts=5,
        delay_between_retries=1.5
    )
    if url:
        print(f"Extracted URL: {url}")

    # 6. Get plan info
    print("\n=== Getting Plan Info ===")
    plan = client.get_plan()
    if plan:
        print(f"Plan info: {plan}")

    # 7. Delete email (if any email exists)
    if emails and len(emails) > 0:
        email_id = emails[0]['id']
        print(f"\n=== Deleting Email ID: {email_id} ===")
        deleted = client.delete_email(email_id)
        print(f"Delete email result: {deleted}")

    # 8. Delete inbox
    print(f"\n=== Deleting Inbox: {test_email} ===")
    deleted_inbox = client.delete_inbox(test_email)
    print(f"Delete inbox result: {deleted_inbox}")

    # 9. List user inboxes
    print("\n=== Listing User Inboxes ===")
    inboxes = client.list_user_inboxes()
    print(f"User inboxes: {inboxes}")

    # 10. Delete user inbox
    print(f"\n=== Deleting User Inbox: {test_email} ===")
    deleted_user_inbox = client.delete_user_inbox(test_email)
    print(f"Delete user inbox result: {deleted_user_inbox}")

    # 11. Get private emails (requires bearer token)
    # print("\n=== Getting Private Emails (Bearer Token) ===")
    # private_emails = client.get_private_emails(bearer_token="your_bearer_token", email=test_email)
    # print(f"Private emails: {private_emails}")

if __name__ == "__main__":
    main()
