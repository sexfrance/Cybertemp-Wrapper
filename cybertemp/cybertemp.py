import requests
import time
import re

from functools import wraps
from typing import Optional, List, Dict, Union, Callable
from logmagix import Logger

class CyberTemp:
    def __init__(self, api_key: str, debug: bool = True) -> None:
        if not api_key:
            raise ValueError("API key is required. Get one at https://cybertemp.xyz/pricing")
        self.__debug = debug
        self.__log = Logger()
        self.__session = requests.Session()
        self.__session.headers = {"X-API-KEY": api_key.strip()}

    def __debug_log(self, func_or_message: Union[Callable, str], *args, **kwargs) -> Callable:
        if callable(func_or_message):
            @wraps(func_or_message)
            def wrapper(*args, **kwargs):
                result = func_or_message(*args, **kwargs)
                if self.__debug:
                    self.__log.debug(f"{func_or_message.__name__} returned: {result}")
                return result
            return wrapper
        else:
            if self.__debug:
                self.__log.debug(f"Debug: {func_or_message}")

    def get_mailbox(self, email: str, max_retries: int = 5, delay_between_retries: float = 2.0) -> Optional[List[Dict]]:

        self.__debug_log(f"Checking mailbox for {email}")
        for attempt in range(max_retries):
            try:
                response = self.__session.get(f'https://api.cybertemp.xyz/getMail?email={email}')
                if response.ok:
                    return response.json()
                else:
                    self.__log.failure(f"Failed to check mailbox: {response.text}, {response.status_code}")
                    break
            except Exception as error:
                self.__log.failure(f"Error checking mailbox: {str(error)}")
                if attempt < max_retries - 1:
                    time.sleep(delay_between_retries * (attempt + 1))
                    continue
                break
        return None

    def get_mail_by_subject(self, email: str, subject_contains: str, max_attempts: int = 10, delay_between_retries: float = 1.5) -> Optional[str]:
        attempt = 0
        self.__debug_log(f"Getting message with subject containing '{subject_contains}' for {email}")
        while attempt < max_attempts:
            messages = self.get_mailbox(email, max_retries=1, delay_between_retries=delay_between_retries)
            if messages:
                for message in messages:
                    if subject_contains in message.get("subject", ""):
                        self.__debug_log(message)
                        return message.get("id")
            attempt += 1
            time.sleep(delay_between_retries)
        self.__debug_log(f"No matching message found after {attempt} attempts")
        return None

    def get_message_content(self, email: str, message_id: str) -> Optional[Dict]:
        self.__debug_log(f"Fetching message {message_id} for {email}")
        messages = self.get_mailbox(email, max_retries=1)
        if messages:
            for message in messages:
                if message.get("id") == message_id:
                    return {
                        "text": message.get("text", ""),
                        "html": message.get("html", ""),
                        "subject": message.get("subject", "")
                    }
        return None

    def extract_url_from_message(self, email: str, subject_contains: str, url_pattern: str, max_attempts: int = 10, delay_between_retries: float = 1.5) -> Optional[str]:
        self.__debug_log(f"Extracting URL for {email}")
        mail_id = self.get_mail_by_subject(email, subject_contains, max_attempts, delay_between_retries)
        if mail_id:
            message = self.get_message_content(email, mail_id)
            if message and message.get("html"):
                url_match = re.search(url_pattern, message["html"])
                if url_match:
                    return url_match.group(0)
        return None

    def get_email_content(self, email: str, max_retries: int = 5, delay_between_retries: float = 2.0) -> Optional[List[Dict]]:
        self.__debug_log(f"Getting emails for {email}")
        return self.get_mailbox(email, max_retries, delay_between_retries)

    def get_email_content_by_id(self, email: str, email_id: str) -> Optional[Dict]:
        """
        Fetch a single email by ID from the mailbox list (deprecated: /api/email/{id}).
        """
        self.__debug_log(f"Getting email with id {email_id} for {email}")
        messages = self.get_mailbox(email, max_retries=1)
        if messages:
            for message in messages:
                if message.get("id") == email_id:
                    return message
        return None

    def get_domains(self, type: str = None) -> Optional[List[str]]:
        """
        GET /api/getDomains - Fetch all available email domains.
        """
        self.__debug_log("Getting domains")
        try:
            response = self.__session.get(f"https://api.cybertemp.xyz/getDomains?type={type}")
            if response.ok:
                return response.json()
            else:
                self.__log.failure(f"Failed to get domains: {response.text}, {response.status_code}")
        except Exception as error:
            self.__log.failure(f"Error getting domains: {str(error)}")
        return None

    def get_plan(self) -> Optional[Dict]:
       
        self.__debug_log("Getting plan info")
        try:
            response = self.__session.get("https://api.cybertemp.xyz/getPlan")
            if response.ok:
                return response.json()
            else:
                self.__log.failure(f"Failed to get plan info: {response.text}, {response.status_code}")
        except Exception as error:
            self.__log.failure(f"Error getting plan info: {str(error)}")
        return None
    
    def get_health(self) -> dict:
        """
        GET /health - Check CyberTemp API health status.
        Returns a dict with status or error/reason.
        """
        self.__debug_log("Checking API health status")
        try:
            response = self.__session.get("https://www.cybertemp.xyz/health")
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 500:
                return response.json()
            else:
                self.__log.failure(f"Unexpected health status: {response.text}, {response.status_code}")
                return {"error": "Unexpected response", "reason": response.text}
        except Exception as error:
            self.__log.failure(f"Error checking health: {str(error)}")
            return {"error": "API unavailable", "reason": str(error)}

    
    def delete_email(self, email_id: str) -> bool:
        """
        DELETE /api/email/{emailId} - Deletes a specific email by its ID.
        Returns True if deleted, False otherwise.
        """
        self.__debug_log(f"Deleting email with id {email_id}")
        try:
            response = self.__session.delete(f"https://api.cybertemp.xyz/email/{email_id}")
            if response.ok:
                return True
            else:
                self.__log.failure(f"Failed to delete email: {response.text}, {response.status_code}")
        except Exception as error:
            self.__log.failure(f"Error deleting email: {str(error)}")
        return False

    def delete_inbox(self, email_address: str) -> bool:
        """
        DELETE /api/inbox/{emailAddress} - Deletes an entire inbox and all its emails.
        Returns True if deleted, False otherwise.
        """
        self.__debug_log(f"Deleting inbox {email_address}")
        try:
            response = self.__session.delete(f"https://api.cybertemp.xyz/inbox/{email_address}")
            if response.ok:
                return True
            else:
                self.__log.failure(f"Failed to delete inbox: {response.text}, {response.status_code}")
        except Exception as error:
            self.__log.failure(f"Error deleting inbox: {str(error)}")
        return False

    def list_user_inboxes(self) -> Optional[Dict]:
        """
        GET /api/user/inboxes - Returns a list of all inboxes created by the authenticated user.
        """
        self.__debug_log("Listing user inboxes")
        try:
            response = self.__session.get("https://api.cybertemp.xyz/user/inboxes")
            if response.ok:
                return response.json()
            else:
                self.__log.failure(f"Failed to list user inboxes: {response.text}, {response.status_code}")
        except Exception as error:
            self.__log.failure(f"Error listing user inboxes: {str(error)}")
        return None

    def delete_user_inbox(self, inbox_address: str) -> bool:
        """
        DELETE /api/user/inboxes - Deletes a user inbox and all its emails. Requires JSON body: {"inbox_address": ...}
        Returns True if deleted, False otherwise.
        """
        self.__debug_log(f"Deleting user inbox {inbox_address}")
        try:
            response = self.__session.delete(
                "https://api.cybertemp.xyz/user/inboxes",
                json={"inbox_address": inbox_address},
                headers={"Content-Type": "application/json", **self.__session.headers}
            )
            if response.ok:
                return True
            else:
                self.__log.failure(f"Failed to delete user inbox: {response.text}, {response.status_code}")
        except Exception as error:
            self.__log.failure(f"Error deleting user inbox: {str(error)}")
        return False

    def get_private_emails(self, bearer_token: str, email: str) -> Optional[List[Dict]]:
        """
        GET /api/private/emails - Fetch emails for a private address using a Bearer token.
        """
        self.__debug_log(f"Getting private emails for {email}")
        try:
            headers = {"Authorization": f"Bearer {bearer_token}"}
            response = self.__session.get(f"https://api.cybertemp.xyz/private/emails?email={email}", headers=headers)
            if response.ok:
                return response.json()
            else:
                self.__log.failure(f"Failed to get private emails: {response.text}, {response.status_code}")
        except Exception as error:
            self.__log.failure(f"Error getting private emails: {str(error)}")
        return None
    
