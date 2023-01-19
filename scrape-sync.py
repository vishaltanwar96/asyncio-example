import json
import time

import requests

from constants import URL
from helpers import html_to_quotes


def scrape_sync() -> None:
    timer_start = time.time()
    for page_number in range(1, 11):
        scrape_pg_and_save_to_file(page_number)
    timer_end = time.time()
    print(
        f"[SYNC-VERSION]Scraping Quotes"
        f" and Inserting them in a "
        f"file took {timer_end - timer_start} seconds"
    )


def scrape_pg_and_save_to_file(page_number: int) -> None:
    url = f"{URL}{page_number}/"
    print(f"Sending request to URL: {url}")
    response = requests.get(url)
    print(f"Scraping response for URL: {url}")
    json_data = html_to_quotes(response.text)
    print(f"Saving response for URL: {url}")
    with open(f"quotes-sync-{page_number}.json", "w") as f:
        json.dump(json_data, f)


if __name__ == "__main__":
    scrape_sync()
