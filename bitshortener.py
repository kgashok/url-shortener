from pyshorteners import Shortener
import json
import requests

class BitShortener(Shortener):
    """Bit.ly Shortener Extended Implementation using a requests Session for efficiency.
    
    Args:
        api_key (str): bit.ly API key.
    """
    
    def __init__(self, api_key):
        super().__init__(api_key=api_key)
        self.session = requests.Session()  # Create a Session object.
        self.session.headers.update({"Authorization": f"Bearer {api_key}",
                                     "Content-Type": "application/json"})  # Set default headers.

    def _patch(self, url, json=None):
        """Send a PATCH request.
        
        Args:
            url (str): Endpoint URL (will be concatenated with base URL).
            json (dict, optional): JSON data to send in the request.
            
        Returns:
            requests.Response: The response object.
        """
        url = self.clean_url(url)  # Assuming clean_url method exists and cleans the URL.
        return self.session.patch(url, json=json)  # Use session's patch method.

    def update_link(self, bitlink_id, updates):
        """Update a bitlink with new data.
        
        Args:
            bitlink_id (str): The unique identifier of the bitlink.
            updates (dict): The updates to apply to the bitlink.
        """
        url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink_id}"
        response = self._patch(url, json=updates)
        if response.ok:
            print("Update successful:", response.json())
        else:
            print("Update failed:", response.text)

    def get_links(self, group_id):
        """Retrieve bitlinks for a specified group.
        
        Args:
            group_id (str): The unique identifier of the group.
            
        Returns:
            list: A list of bitlinks.
        """
        url = f"https://api-ssl.bitly.com/v4/groups/{group_id}/bitlinks"
        response = self.session.get(url)
        if response.ok:
            return response.json()['links']
        else:
            print("Failed to retrieve links:", response.text)
            return []

    def user_info(self):
        """Retrieve information about the user.
        
        Returns:
            dict: User information.
        """
        url = "https://api-ssl.bitly.com/v4/user"
        response = self.session.get(url)
        if response.ok:
            return response.json()
        else:
            print("Failed to retrieve user info:", response.text)
            return {}

    @staticmethod
    def clean_url(url):
        """Placeholder method for cleaning URLs if necessary."""
        # Implement any necessary URL cleaning here.
        return url
