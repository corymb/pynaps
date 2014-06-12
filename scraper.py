# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


input_source = 'test_nap.html'
with open(input_source, 'r') as page:
    data = page.read()


def parse_naps(data=data):
    soup = BeautifulSoup(data)
    table = soup.find("div", {"id": "tipsTableOutput"})
    rows = table.find_all("tr")
    clean_rows = [[col.get_text().strip() for col in row.find_all(
        "td")] for row in rows if row]
    return [dict(zip(["naps", "time", "crs", "tipster", "spread"],
        e)) for e in clean_rows if len(e) == 5]

naps = parse_naps()

# Nap functions:
get_top_x = lambda x: naps[:x]
