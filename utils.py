import settings
import requests
import json

from requests_aws4auth import AWS4Auth

auth = None
if settings.PROD:
    auth = AWS4Auth(
      settings.ACCESS_ID,
      settings.ACCESS_SECRET,
      'us-east-2', 'es'
    )


def save_in_db(author, data):
    """Saves string data in db"""
    url = f"{settings.ES_URL}/{author.id}/_doc"
    requests.post(url, json={
      "text": data
    }, auth=auth)


def search_in_db(author, data):
    """Searches db for words in given query"""
    url = f"{settings.ES_URL}/{author.id}/_search"
    words = map(lambda x: f"*{x}*", filter(lambda x: len(x) > 0, data.split()))
    query = " OR ".join(words)
    res = requests.post(url, 
      json.dumps({
        "query": {
          "query_string": {
            "query": query
          }
        }
      }),
      headers = {"Content-type": "application/json", "Accept": "text/plain"},
      auth = auth
    )
    if res.status_code==200:
        return map(lambda x: x['_source']['text'], res.json()['hits']['hits'])

    return []
