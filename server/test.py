from pprint import pprint

import requests

pprint(requests.get("http://127.0.0.1:5000/app/api/v1.0/questions/").text)