from pyshorteners import Shortener

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
    pass

    def user_info(self, **kwargs):
        """return or update info about a user"""
        return "ashok"

