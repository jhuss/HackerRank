if __name__ == '__main__':
    input_val = input().strip()

    if input_val.isdigit():
        n = int(input_val)

        if 1 <= n <= 100:
            if n % 2 == 0 and (n > 20 or n in range(2, 6)):
                print('Not Weird')
            else:
                print('Weird')
