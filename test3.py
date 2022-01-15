# how to get a bunch of URLs from bitly 
from pyshorteners import Shortener
from bitshortener import BitShortener

# get the token from https://bitly.is/accesstoken
access_token = "1ef1315a2efebd7557de137f776602276d833cb9"  
# link = input("Enter the short link to get more info:")
client = BitShortener(api_key=access_token)

urlist = []
# urlist.extend(["https://j.mp/pythonYes", "https://j.mp/listThis", "http://j.mp/junk"])
for link in urlist: 
  try:
    # get more info here--> https://bit.ly/shorteners-info
    print(f"Original Link: {client.bitly.expand(link)}\n"  
          f"Short Link: {link}\n"
          f"Total number of clicks = {client.bitly.total_clicks(link)}")
  except Exception as e:
  # except BadAPIResponseException as e:
    print("Bad URL!", e)


# how to get a bunch of URLs from bitly 

# Step 1 - get groupid 
userinfo = client.user_info()
groupid = userinfo.get('default_group_guid')
print("groupid", groupid)

# Step 2 - get links by group
#import pprint
linkinfo = client.get_links()
print(len(linkinfo["links"]))

for bitlink in linkinfo["links"][:5]: 
  try:
    print(f'{bitlink["title"][:30]}', end=" -> ")
  except: 
    print("<No title>", end=" ->")
  print(f'{bitlink["long_url"][:35]}, {bitlink["link"]}') #, bitlink["custom_bitlinks"])
