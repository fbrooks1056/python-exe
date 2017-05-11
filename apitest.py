import requests

response = requests.get("http://hclapi-dev.us-east-2.elasticbeanstalk.com/organization/5")

print(response.text)