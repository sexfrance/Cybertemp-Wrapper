"""
Test script for the delete_inbox fix
This demonstrates that delete_inbox now correctly calls delete_user_inbox
"""

from cybertemp import CyberTemp

# Example usage - replace with your actual API key
# api_key = "your_api_key_here"
# cybertemp = CyberTemp(api_key)

# The delete_inbox method now correctly uses the /api/user/inboxes endpoint
# email_address = "test@example.com"
# result = cybertemp.delete_inbox(email_address)

# This is equivalent to:
# result = cybertemp.delete_user_inbox(email_address)

print("delete_inbox() now correctly calls delete_user_inbox() internally")
print("The endpoint used is: DELETE /api/user/inboxes")
print("With JSON body: {\"inbox_address\": \"<email_address>\"}")
