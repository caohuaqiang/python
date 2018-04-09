import os
from pprint import pprint
os.chdir('F:\python\webapp')

from datetime import datetime


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open(file='buzzers.csv', mode='r') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
    # pprint(flights)



    flights3 = {convert2ampm(k): v.title()
                for k, v in flights.items()
                }
    pprint(flights3)

    dests = set(flights3.values())  # 唯一目的地
    print('唯一目的地： ', dests)


    # for dest in dests:
    #     print(dest, '->', [k
    #                        for k, v in flights3.items()
    #                        if v == dest])

    # B = {}
    #
    # for dest in dests:
    #     C = []
    #     for k, v in flights3.items():
    #         if v == dest:
    #             C.append(k)
    #             B[v] = C
    #
    # pprint(B)

    # when = {}
    # for dest in dests:
        # print(dest, '->', [k for k, v in flights3.items() if v == dest])
    #     when[dest] = [k for k,v in flights3.items() if v == dest]

    c = {dest: [k for k, v in flights3.items() if v == dest]
         for dest in dests
        }
    print(c)

