import requests
import sys

def check_args_len(arg):
    if arg< 3:
        print("Error: missing arguments.")
        print("Usage: python file.py <limit> <common|official>")
        sys.exit(1)

def check_is_negative(arg):
    if arg < 0:
        print("Error: the argument should be positive.")
        sys.exit(1)

def check_type_name(arg):
    if arg != "common" and arg != "official":
        print("Error: the third argument must be either 'common' or 'official'.")
        sys.exit(1)

def check_requisition_status(response):
    if response.status_code != 200:
        print("Request failed.")
        print("Status: ", response.status_code)
        print("Response: ", response.text)
        sys.exit(1)

def print_data(countries_sorted, limit, type_name):
    index = 0
    while index < limit:
        item = countries_sorted[index]
        name = item["name"][type_name]
        pop = item["population"]
        print(f"[{index + 1}] {name}: {pop:,}")
        index += 1 

check_args_len(len(sys.argv))
check_is_negative(int(sys.argv[1]))
check_type_name(sys.argv[2])

url = 'https://restcountries.com/v3.1/all?fields=name,population'
response = requests.get(url)
check_requisition_status(response)

countries = response.json()
countries_sorted = sorted(countries, key=lambda c: c["population"], reverse=True)

print_data(countries_sorted, int(sys.argv[1]), sys.argv[2])