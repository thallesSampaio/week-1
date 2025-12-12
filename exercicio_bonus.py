import sys
import csv
import requests
import exercicio1

def export_to_csv(countries_sorted, limit, type_name, filename="dados_api.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["rank", "name", "population"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for index in range(limit):
            item = countries_sorted[index]
            name = item["name"][type_name]
            pop = item["population"]

            writer.writerow({
                "rank": index + 1,
                "name": name,
                "population": pop
            })

    print(f"CSV saved as: {filename}")

exercicio1.check_args_len(len(sys.argv))
exercicio1.check_is_negative(int(sys.argv[1]))
exercicio1.check_type_name(sys.argv[2])

url = 'https://restcountries.com/v3.1/all?fields=name,population'
response = requests.get(url)
exercicio1.check_requisition_status(response)

countries = response.json()
countries_sorted = sorted(countries, key=lambda c: c["population"], reverse=True)



export_to_csv(countries_sorted, int(sys.argv[1]), sys.argv[2], filename="dados_api.csv")