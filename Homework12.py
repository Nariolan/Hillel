import requests
import csv


def get_random_quote(range_value):
    url = "http://api.forismatic.com/api/1.0/"
    quotes_list = []
    for number in range(range_value):
        params = {"method": "getQuote",
                  "format": "json",
                  "key": number,
                  "lang": "ru",
                  }
        responce = requests.get(url, params=params)
        data = {"quoteAuthor": "Марк Аврелий", "quoteText": "Брать без ослепления, расставаться с легкостью."}

        if responce.json()["quoteAuthor"] == " " and responce.json()["quoteText"] in data["quoteText"]:
            pass
        else:
            data = responce.json()

        print(data["quoteAuthor"], ">>>>>>>>", data["quoteText"])
        quotes_list.append([data["quoteAuthor"], data["quoteText"]])
    return quotes_list


def write_csv(my_list):
    with open("12.csv", "w") as csv_file:
        csv_file.columns = ["Цитата", "Автор"]
        writer = csv.writer(csv_file, delimiter=",")

        writer.writerow(("Цитата   ", "Автор"))

        for line in my_list:
            writer.writerow(line)


write_csv(get_random_quote(5))
