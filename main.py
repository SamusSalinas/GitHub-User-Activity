import sys
import urllib.request
import json

if len(sys.argv) > 1 and sys.argv[1]:
    username = sys.argv[1]
    url = f"https://api.github.com/users/{username}/events"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    for event in data:
        print(f"- {event['type']} en {event['repo']['name']}")
else:
    print("Please provide a valid GitHub username as a command line argument.")