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
    def user_info(self, **kwargs):
        # return "ashok"
        """return or update info about a user
        Args:
        Returns:
            user information
        """
        #clicks_url = f"{self.api_url}/bitlinks/{url}/clicks"
        user_url = f"{self.bitly.api_url}/user"
        print(f'user_url: {user_url}')
        headers = {"Authorization": f"Bearer {self.bitly.api_key}"}
        response = self.bitly._get(user_url, headers=headers)
        if not response.ok:
            raise BadAPIResponseException(response.content)

        try:
            data = response.json()
        except json.decoder.JSONDecodeError:
            raise BadAPIResponseException("API response could not be decoded")

        return data

    def get_links(self, **kwargs):
        """get links for a default groupid and user
        Args:
           userinfo and groupid
        Returns:
            paginated bitlinks 
        """
        groupid = self.user_info()["default_group_guid"]
        bitlinks_url = f"{self.bitly.api_url}/groups/{groupid}/bitlinks"
        headers = {"Authorization": f"Bearer {self.bitly.api_key}"}

        params = (
            ('size', '50'),
            ('page', '1'),
            #('keyword', 'python'),
            ('query', "python"),
            # ('created_before', '1501027200'),
            # ('created_after', '1501027200'),
            # ('modified_after', '1501027200'),
            ('archived', 'both'),
            ('deeplinks', 'both'),
            ('domain_deeplinks', 'both'),
            # ('campaign_guid', 'Ca1bcd2EFGh'),
            # ('channel_guid', 'Ha1bc2DefGh'),
            ('custom_bitlink', 'both'),
            ('tags[0]', 'bitly'),
            ('tags[1]', 'api'),
            # ('launchpad_ids[0]', 'M1234567890'),
            # ('encoding_login[0]', 'chauncey'),
        )

        # response = requests.get(bitlinks_url, headers=headers, params=params)
        print(f'bitlink_url: {bitlinks_url}')
        response = self.bitly._get(bitlinks_url, headers=headers, params=params)
        if not response.ok:
            raise BadAPIResponseException(response.content)

        try:
            data = response.json()
        except json.decoder.JSONDecodeError:
            raise BadAPIResponseException("API response could not be decoded")

        return data