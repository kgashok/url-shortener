from pyshorteners import Shortener
import json
import requests


class BitShortener(Shortener):
    """Bit.ly Shortener Extended Implementation
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

    def _patch(self, url, data=None, json=None, params=None, headers=None):
        """Wrap a PATCH request with a url check.
        Args:
            url (str): URL shortener address.
        Keyword Args:
            data (dict, str): Form-encoded data, `Requests POST Data`_.
            headers (dict): HTTP headers to add, `Requests Custom Headers`_.
            json (dict): Python object to JSON encode for data, `Requests
                POST Data`_.
            params (dict): URL parameters, `Requests Parameters`_.
        .. _Requests Custom Headers: http://requests.kennethreitz.org/en/master/user/quickstart/#custom-headers
        .. _Requests Parameters: http://requests.kennethreitz.org/en/master/user/quickstart/#passing-parameters-in-urls
        .. _Requests POST Data: http://requests.kennethreitz.org/en/master/user/quickstart/#more-complicated-post-requests
        Returns:
            requests.Response: HTTP response.
        """
        url = self.bitly.clean_url(url)

        response = requests.patch(
            url,
            data=data,
            json=json,
            # params=params,
            headers=headers,
            timeout=self.bitly.timeout,
            verify=self.bitly.verify,
            proxies=self.bitly.proxies,
            # cert=self.bitly.cert,
        )
        return response

    def update_link(self, **kwargs):
        headers = {
            "Authorization": f"Bearer {self.bitly.api_key}",
            "Content-Type": "application/json"
        }

        id = "/bit.ly/3GB8YMP"

        response = self.bitly._get(
            'https://api-ssl.bitly.com/v4/bitlinks' + id,
            headers=headers)

        print(response, response.content)
        data = response.content
        print("type", type(data))
        data = response.json()
        print("type after", type(data))
        del data["deeplinks"]
        print(type(data['tags']), type(data['tags']))
        print(data['tags'])

        # updating the tags with another additional tag
        # Does it accept duplicates?
        # It doesn't - that's cool!
        data['tags'].append('test')

        response = self._patch(
            'https://api-ssl.bitly.com/v4/bitlinks' + id,
            json=data,
            headers=headers)
        print("--After update")
        print(response, response.content)

    def user_info(self, **kwargs):
        # return "ashok"
        """return or update info about a user by
        calling the appropriate bitlyAPI endpoint.
        Documented at https://dev.bitly.com/api-reference#getUser

        Args:
        Returns:
            user information, including default_group_id
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
        as Documented at https://dev.bitly.com/api-reference#getBitlinksByGroup

        Args:
           userinfo and groupid
        Returns:
            paginated bitlinks
        """
        groupid = self.user_info()["default_group_guid"]
        bitlinks_url = f"{self.bitly.api_url}/groups/{groupid}/bitlinks"
        headers = {"Authorization": f"Bearer {self.bitly.api_key}"}

        params = (
            ('size', '100'),
            ('page', '1'),
            #('keyword', 'learningToTeach'),
            #('query', "python"),
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
        response = self.bitly._get(
            bitlinks_url, headers=headers, params=params)
        if not response.ok:
            raise BadAPIResponseException(response.content)

        try:
            data = response.json()
        except json.decoder.JSONDecodeError:
            raise BadAPIResponseException("API response could not be decoded")

        return data
