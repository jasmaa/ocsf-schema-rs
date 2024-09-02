from pathlib import Path
import logging
import sys
import bs4
import requests

BASE_URL = "https://schema.ocsf.io"
VERSION = "1.3.0"
OUTPUT_DIR = "./data"


def download_all_schemas():
    for type in ["objects", "classes"]:
        logging.info("Finding table...")
        res = requests.get(f"{BASE_URL}/{VERSION}/{type}")
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        table = soup.find("table", class_="table")
        rows = table.find("tbody").find_all("tr")
        logging.info(f"Found {len(rows)} rows.")
        for row in rows:
            cells = row.find_all("td")
            a = cells[1].find("a")
            text = "_".join(a.text.split("/"))
            logging.info(f"Processing {text}...")
            p = f"{BASE_URL}/schema/{VERSION}/{type}/{text}"
            res = requests.get(p)
            output_path = Path(OUTPUT_DIR).joinpath(
                Path(f"{type}/{text}.json"))
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w") as f:
                f.write(res.text)
            logging.info(f"Wrote to {output_path}.")


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    download_all_schemas()
    logging.info("Done!")
