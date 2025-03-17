def print_function(num: int):
    if not 1 <= num <= 150:
        return
    output_str = ""
    for i in range(num):
        output_str += str(i + 1)
    print(output_str)


if __name__ == "__main__":
    n = int(input())
    print_function(n)
