import requests
import json
from collections import Counter
import argparse

def get_activity(username):
    if username is None:
        print("Provide a Github Username ")
        return
    url=f'https://api.github.com/users/{username}/events'
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        events = response.json()
        event_types=[event['type'] for event in events]
        type_counts=Counter(event_types)
        print("-----------------------------------------------------------")
        print(f'{'Github UserActivity Report of User : '}{username}')
        print("------------------------------------------------------------")
        print(f'{'Event Type':<10} | {'Number of Events':<15}')
        for event_type,count in type_counts.items():
            print(f'{event_type:<20}{count:2}')
    else:
        print("Error connect to git hub please check the username and internet connection")

parser = argparse.ArgumentParser(description="Github User activity report")
parser.add_argument('--username',help="Provide the github username")

args = parser.parse_args()

get_activity(args.username)


