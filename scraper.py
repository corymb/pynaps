# -*- coding: utf-8 -*-
from collections import Counter

import requests
from bs4 import BeautifulSoup

DEBUG = True

if DEBUG:
    input_source = 'test_nap.html1'
    with open(input_source, 'r') as page:
        data = page.read()
else:
    data = requests.get("https://www.racingpost.com/news/tips_home.sd").content


def parse_naps(data=data):
    soup = BeautifulSoup(data)
    table = soup.find('div', {'id': 'tipsTableOutput'})
    rows = table.find_all('tr')
    clean_rows = [[col.get_text().strip() for col in row.find_all(
        "td")] for row in rows if row]
    return [dict(zip(['name', 'time', 'crs', 'tipster', 'spread'],
        e)) for e in clean_rows if len(e) == 5]

entries = parse_naps()

# Helper functions:
is_positive = lambda(tip): True if tip['spread'][0] == '+' else False
get_integer = lambda(tip): tip['spread'][1:]

# Nap functions:
get_top_x = lambda x: entries[:x]
get_most_tipped = Counter([entry['name'] for entry in entries])
get_most_tipped_spread = lambda: [float(entry['spread']) for entry in entries]

aggregate_spreads = lambda x: sum([float(y['spread'])
    for y in entries if y['name'] == x])

hottest_tips = ['%s @ %s' % (x, aggregate_spreads(x))
        for x, y in get_most_tipped.items()
        if y > 1 if aggregate_spreads(x) > 0]
get_positive_tippers = filter(lambda(tip): tip if is_positive(tip) else None,
                entries)

for tip in hottest_tips:
    print tip
