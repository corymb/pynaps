# -*- coding: utf-8 -*-
from collections import Counter

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

entries = parse_naps()

# Helper functions:
is_positive = lambda(tip): True if tip['spread'][0] == '+' else False
get_integer = lambda(tip): tip['spread'][1:]

# Nap functions:
get_top_x = lambda x: entries[:x]
get_most_tipped = Counter([entry['naps'] for entry in entries])
get_positive_tippers = filter(lambda(tip): tip if is_positive(tip) else None,
        entries)
