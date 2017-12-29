import sys

if __name__ == '__main__':
    val01 = input().strip()
    val02 = input().strip()

    if val01.isdigit() and val02.isdigit():
        n01 = int(val01)
        n02 = int(val02)

        for i in map(lambda x: 1 <= x <= 10**10, [n01, n02]):
            if not i:
                sys.exit()

        print('{}'.format(n01 + n02))
        print('{}'.format(n01 - n02))
        print('{}'.format(n01 * n02))
