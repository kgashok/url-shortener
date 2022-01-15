from pyshorteners import Shortener
import json 

class BitShortener(Shortener):
    """Bit.ly shortener Extended Implementation
    Args:
        api_key (str): bit.ly API key
    Example:
        >>> import pyshorteners
        >>> s = pyshorteners.Shortener(api_key='YOUR_KEY')
        >>> s.bitly.short('http://www.google.com')
        'http://bit.ly/TEST'
        >>> s.bitly.expand('https://bit.ly/TEST')
        'http://www.google.com'
        >>> s.bitly.total_clicks('https://bit.ly/TEST')
        10
    """
    api_url = "https://api-ssl.bit.ly/v4"

    def user_info(self, **kwargs):
        """return or update info about a user"""
        # return "ashok"
        """Total clicks implementation for Bit.ly
        Args:
        Returns:
            user information
        """
        #clicks_url = f"{self.api_url}/bitlinks/{url}/clicks"
        user_url = f"{self.api_url}/user"
        headers = {"Authorization": f"Bearer {self.bitly.api_key}"}
        response = self.bitly._get(user_url, headers=headers)
        if not response.ok:
            raise BadAPIResponseException(response.content)

        try:
            data = response.json()
        except json.decoder.JSONDecodeError:
            raise BadAPIResponseException("API response could not be decoded")

        return data
