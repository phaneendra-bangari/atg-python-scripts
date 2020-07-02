#Printing the track name and release data from iTunes API with search "the beatles" and the limiting the search to 200.
import requests
import json

#iTunes API Documentation location.
iTunes_base_url = "https://itunes.apple.com/search"

#GET REQUESTS using requests package.
r_get=requests.get(iTunes_base_url,params={"term":"the beatles" ,"limit":"200"})

#Converting the response to JSON Object.
returned_data=r_get.json()

#Using a loop to access only the necessary fields.
for trackName in returned_data["results"]:
    print(f'{trackName["trackName"]}\t{trackName["releaseDate"]}')

'''
More Stuff
print(returned_data.keys())
print(json.dumps(returned_data["results"][0]["trackName"],indent=4))
print(json.dumps(returned_data,indent=4))
'''