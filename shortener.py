from pyshorteners import Shortener
# get the token from https://bitly.is/accesstoken
access_token = "1ef1315a2efebd7557de137f776602276d833cb9"
long_url = input("Enter the long link:")
client = Shortener(api_key=access_token)
print(client.bitly.short(long_url))
