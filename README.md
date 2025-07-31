<div align="center">
  <h2 align="center">CyberTemp API Client</h2>
  <p align="center">
    A Python client for interacting with the CyberTemp temporary email service API.
    <br />
    <br />
    <a href="https://cybertemp.xyz">🌐 Website</a>
    ·
    <a href="#-changelog">📜 ChangeLog</a>
    ·
    <a href="https://github.com/sexfrance/cybertemp-wrapper/issues">⚠️ Report Bug</a>
  </p>
</div>

---

### ⚙️ Installation

```bash
pip install cybertemp
```

### 🚀 Quick Start

```python
from cybertemp import CyberTemp


# Initialize (API key required)
client = CyberTemp(api_key="your_api_key_here", debug=True)


# Get available domains
domains = client.get_domains()

# Check mailbox with retry settings (optional parameters: max_retries, delay_between_retries)
emails = client.get_email_content("test@cybertemp.xyz", max_retries=3, delay_between_retries=2.0)
```


**API key is now required for all requests.**
You can purchase an API key here: [CyberTemp Pricing](https://cybertemp.xyz/pricing)

### 📚 API Reference


#### Initialization
```python
client = CyberTemp(
    api_key="your_api_key_here",  # Required: API key for all features
    debug=True                     # Optional: Enable debug logging
)
```

#### Available Methods


1. **Get Email Content**
```python
emails = client.get_email_content("test@cybertemp.xyz", max_retries=3, delay_between_retries=2.0)  # Optional: max_retries, delay_between_retries
```


2. **Get Email by ID**
```python
email = client.get_email_content_by_id("email_id_here")
```


3. **Get Available Domains**
```python
domains = client.get_domains()
```


4. **Search Email by Subject**
```python
mail_id = client.get_mail_by_subject(
    email="test@cybertemp.xyz",
    subject_contains="Verification",
    max_attempts=5,                # Optional
    delay_between_retries=1.5       # Optional
)
```


5. **Extract URL from Email**
```python
url = client.extract_url_from_message(
    email="test@cybertemp.xyz",
    subject_contains="Verification",
    url_pattern=r'https://[^\s<>"']+',
    max_attempts=5,                # Optional
    delay_between_retries=1.5       # Optional
)
```


6. **Check API Balance**
```python
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