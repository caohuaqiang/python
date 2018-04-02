
def ABC():
    n = 4
    A = ''
    for i in range(1, n+1):
        b = 'box'+str(i)+','
        A = A +b
        print(A)


def ABC_1(n: int=1) -> str:
    # n = 1
    A = ''
    for i in range(1, n + 1):
        if i == n:
            b = 'box_' + str(i)
        else:
            b = 'box_'+str(i)+','
        A += b
        # print(A)
    return A


def ABC_2():
    n = 5
    A = ''
    data = {'box1': 0,
            'box2': 1,
            'box3': 1,
            'box4': 1,
            'box5': 0}
    for k, v in data.items():
        if v == 1:
            # print(k)
            A += k + ','
    print(A)
    B = A[:-1]
    print(B)




if __name__ == '__main__':
    ABC_2()

