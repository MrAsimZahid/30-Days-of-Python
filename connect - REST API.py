#Using REST API to query different data and practicing how different REST APIs work 

import requests
import pprint
import pandas as pd

api_key = "e4d081c6d7fad9cdb86b48beed4e36ff"
api_version = 3
# HTTP requests
"""
GET ->  grab data
POST -> add/update data

PATCH
PUT
DELETE
"""
#wha'ts our endpoint (or a url)?

#what is the http method that we need?

"""
ENDPOINT
GET
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=e4d081c6d7fad9cdb86b48beed4e36ff
"""

movie_id = 500
api_base_url =  f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "the matrix"

endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
r = requests.get(endpoint) #, data={"api_key": api_key})
#pprint.pprint(r.json())
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:

  #      print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result['id']
            #print(result['title'], _id)
            movie_ids.add(_id)
#        print(list(movie_ids))

 #   print(r.text)
 #   pprint.pprint(r.json())
output = 'movies.csv'
movie_data = []

for movie_id in movie_ids:
    api_base_url =  f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)

df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index=False)