from pprint import pprint
from datetime import datetime


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


# with open(file='buzzers.csv') as data:
#     data.readline()
#     first = {}
#     for line in data:
#         k, v = line.strip().split(',')
#         first[k] = v
#
#
# pprint(first)
#
# dests = set(first.values())
# print(dests)
#
# second = {}
# for dest in dests:
#     a = []
#     for time, destinataion in first.items():
#         if destinataion == dest:
#             a.append(convert2ampm(time))
#         second[dest.title()] = a
#
# pprint(second)

with open(file='buzzers.csv', mode='r') as data:
    flights = {}
    data.readline()
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint(flights)

dests = set(flights.values())
print('唯一目的地：', dests)

# A = [v
#      for k, v in flights.items()
#      if k == dest]

B = {dest.title(): [convert2ampm(k)
                    for k, v in flights.items()
                    if v == dest]
     for dest in dests}

pprint(B)


