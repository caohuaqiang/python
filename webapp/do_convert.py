from datetime import datetime
from pprint import pprint


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v


pprint(flights)
print()

fts = {convert2ampm(k): v.title()
       for k, v in flights.items()
       }
pprint(fts)
print()

dests = set(fts.values())
A = {dest: [k
            for k, v in fts.items()
            if v == dest]
     for dest in dests}
print(A)
