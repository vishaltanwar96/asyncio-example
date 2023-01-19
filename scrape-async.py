import asyncio
import json
import time

import aiofiles
import httpx

from constants import URL
from helpers import html_to_quotes


async def scrape_async() -> None:
    timer_start = time.time()
    async with httpx.AsyncClient() as client:
        await asyncio.gather(
            *[scrape_page_and_save_to_file(client, page_no) for page_no in range(1, 11)]
        )
    timer_end = time.time()
    print(
        f"[ASYNC-VERSION]Scraping Quotes and Inserting them in a file took {timer_end - timer_start} seconds"
    )


async def scrape_page_and_save_to_file(
    client: httpx.AsyncClient, page_number: int
) -> None:
    url = f"{URL}{page_number}/"
    print(f"Sending request to URL: {url}")
    response = await client.get(url)
    print(f"Scraping response for URL: {url}")
    json_data = html_to_quotes(response.text)
    print(f"Saving response for URL: {url}")
    async with aiofiles.open(f"quotes-async-{page_number}.json", "w") as f:
        await f.write(json.dumps(json_data))


if __name__ == "__main__":
    asyncio.run(scrape_async())
