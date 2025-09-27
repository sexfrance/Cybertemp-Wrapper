<div align="center">
  <h2>CyberTemp API Client</h2>
  <p>
    A Python client for interacting with the CyberTemp temporary email service API.
    <br />
    <br />
    <a href="https://www.cybertemp.xyz">🌐 Website</a>
    ·
    <a href="#-changelog">📜 ChangeLog</a>
    ·
    <a href="https://github.com/sexfrance/cybertemp-wrapper/issues">⚠️ Report Bug</a>
  </p>
</div>

---

#### Available Methods

1. **Get Email Content**

```py
emails = client.get_email_content("test@cybertemp.xyz", max_retries=3, delay_between_retries=2.0)
```

1. **Get Email by ID**

```py
email = client.get_email_content_by_id("test@cybertemp.xyz", "email_id_here")
```

1. **Get Available Domains**

```py
domains = client.get_domains()
```

1. **Search Email by Subject**

```py
mail_id = client.get_mail_by_subject(
    email="test@cybertemp.xyz",
    subject_contains="Verification",
    max_attempts=5,
    delay_between_retries=1.5
)
```

1. **Extract URL from Email**

```py
url = client.extract_url_from_message(
    email="test@cybertemp.xyz",
    subject_contains="Verification",
    url_pattern=r'https://[^\s<>"']+',
    max_attempts=5,
    delay_between_retries=1.5
)
```

1. **Get Plan Info**

```py
plan = client.get_plan()
```

1. **Delete Email**

```py
success = client.delete_email("email_id_here")
```

1. **Delete Inbox**

```py
success = client.delete_inbox("test@cybertemp.xyz")
```

1. **List User Inboxes**

```py
inboxes = client.list_user_inboxes()
```

1. **Delete User Inbox**

```py
success = client.delete_user_inbox("test@cybertemp.xyz")
```

1. **Get Private Emails (Bearer Token)**

```py
private_emails = client.get_private_emails(bearer_token="your_bearer_token", email="test@cybertemp.xyz")
```
```

1. **Get Available Domains**

```py
domains = client.get_domains()
```

4. **Search Email by Subject**

```py
mail_id = client.get_mail_by_subject(
    email="test@cybertemp.xyz",
    subject_contains="Verification",
    max_attempts=5,                # Optional
    delay_between_retries=1.5       # Optional
)
```

5. **Extract URL from Email**

```py
url = client.extract_url_from_message(
    email="test@cybertemp.xyz",
    subject_contains="Verification",
    url_pattern=r"""https://[^\s<>"']+""",
    max_attempts=5,                # Optional
    delay_between_retries=1.5       # Optional
)
```

6. **Check API Balance**

```py
balance = client.get_balance()
```

### 💳 Pricing & Plans

CyberTemp offers several subscription plans:

- **Free Tier**: No API key required, 2-second delay, 10 req/sec
- **Eco Plan**: €1.99/month, no delay, 20 req/sec
- **Core Plan**: €2.99/month, no delay, 50 req/sec
- **Elite Plan**: €4.99/month, no delay, unlimited requests

All paid plans require an API key. See [CyberTemp Pricing](https://cybertemp.xyz/pricing) for details and to purchase a key.

### ⚠️ Rate Limits

- All requests require an API key (except Free tier)
- Free tier: 2-second delay between requests, 10 req/sec
- Paid tiers: No delay, higher rate limits

### 📜 ChangeLog

```diff
v1.0.1 ⋮ 2025-03-05
+ Added configurable retry and delay options for email checking functions
+ Indicated optional parameters in documentation

v1.0.0 ⋮ 2025-02-14
! Initial release
```

<p align="center">
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg"/>
  <img src="https://img.shields.io/badge/license-MIT-green.svg"/>
  <img src="https://img.shields.io/badge/version-1.0.1-orange.svg"/>
</p>
