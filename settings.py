PROD = False

if not PROD:
  ES_URL = "http://localhost:9200"
else:
  ES_URL = "https://search-discordbot-zk7q5t7pg6dw2dutpwkni7gpxy.us-east-2.es.amazonaws.com"