from pathlib import Path
import logging
import bs4
import requests

BASE_URL = "https://schema.ocsf.io"
VERSION = "1.3.0"


def download_all_object_schemas():
    res = requests.get(f"{BASE_URL}/{VERSION}/objects")
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    table = soup.find("table", class_="table")
    rows = table.find("tbody").find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        a = cells[1].find("a")
        text = "_".join(a.text.split("/"))
        p = f"{BASE_URL}/schema/{VERSION}/objects/{text}"
        res = requests.get(p)
        filep = Path(f"./data/objects/{text}.json")
        filep.parent.mkdir(parents=True, exist_ok=True)
        with open(filep, "w") as f:
            f.write(res.text)


def download_all_class_schemas():
    res = requests.get(f"{BASE_URL}/{VERSION}/classes")
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    table = soup.find("table", class_="table")
    rows = table.find("tbody").find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        a = cells[1].find("a")
        text = "_".join(a.text.split("/"))
        p = f"{BASE_URL}/schema/{VERSION}/classes/{text}"
        res = requests.get(p)
        filep = Path(f"./data/classes/{text}.json")
        filep.parent.mkdir(parents=True, exist_ok=True)
        with open(filep, "w") as f:
            f.write(res.text)


download_all_object_schemas()
download_all_class_schemas()
