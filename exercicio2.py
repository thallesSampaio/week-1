import json
import requests
import sys


UID = "YOUR UID"
SECRET = "YOUR SECRET KEY"

BASE_URL = "https://api.intra.42.fr"

def check_arguments(argc):
    if argc == 1:
        print("Missing arguments.")
        sys.exit(1)

def validate_arguments(argc, argv):
    if argc == 2:
        if argv != "formated" and argv != "json":
            print("Error: the second argument must be either 'formated' or 'json'.")
            sys.exit(1)

def check_requisition_status(response):
    if response.status_code != 200:
        print("Request failed.")
        print("Status: ", response.status_code)
        print("Response: ", response.text)
        sys.exit(1)

def get_token(UID, SECRET, BASE_URL):
    token_url = f"{BASE_URL}/oauth/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": UID,
        "client_secret": SECRET
    }
    token_response = requests.post(token_url, data=data)
    token_response.raise_for_status()
    return token_response.json()["access_token"]

seen = set()
def print_data(response, seen):
    for item in response:
        if item["user"]["location"] == None:
            continue
        
        name = item["user"]["login"]
        location = item["user"]["location"]

        if name in seen:
            continue
        
        seen.add(name)
        print(f"Login: [{name}] Location: [{location}]")


check_arguments(len(sys.argv))
validate_arguments(len(sys.argv), sys.argv[1])

headers = {
    "Authorization": f"Bearer {get_token(UID, SECRET, BASE_URL)}"
}

response = requests.get(f"{BASE_URL}/v2/campus/28/locations?filter[active]=true&filter[primary]=true", headers=headers)
check_requisition_status(response)

if sys.argv[1] == "json":
    data_to_format = response.json()
    formated_data = json.dumps(data_to_format, indent=4)
    print(formated_data)
elif sys.argv[1] == "formated":
    data = response.json()
    print_data(data, seen)
    print("Total number of students:", len(seen))
