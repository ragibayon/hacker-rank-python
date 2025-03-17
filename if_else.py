if __name__ == '__main__':
    n = int(input().strip())


    def check_even(num: int):
        return num % 2 == 0


    if not check_even(n):
        print("Weird")
    else:
        if 2 <= n <= 5:
            print('Not Weird')
        elif 6 <= n <= 20:
            print('Weird')
        elif n >= 20:
            print('Not Weird')
