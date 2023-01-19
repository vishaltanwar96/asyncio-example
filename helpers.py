from bs4 import BeautifulSoup


def html_to_quotes(html: str) -> list[dict[str, str]]:
    json_data = []
    soup = BeautifulSoup(html, "html.parser")
    quotes = soup.find_all(class_="quote")
    for quote_html in quotes:
        spans = quote_html.find_all_next("span")
        quote, author = spans[0].text, spans[1].small.text
        json_data.append({"author": author, "quote": quote})
    return json_data
