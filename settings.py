import os

PROD = True

ACCESS_ID = os.environ.get("AWS_ACCESS_ID")
ACCESS_SECRET = os.environ.get("AWS_ACCESS_SECRET")

if not PROD:
  ES_URL = "http://localhost:9200"
else:
  ES_URL = "https://search-discord-jcizn4xvaamzdcxm6xyydnltvy.us-east-2.es.amazonaws.com"