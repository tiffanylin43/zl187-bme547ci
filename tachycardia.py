# receive input
def receive_input():
    string = input("Enter the string for testing:")
    return string


# check if there is "tachycardic" in the string input
def is_tachycardic(A):
    a = A.lower()
    n = len(a)
    m = 0
    for i in range(n):
        answer = a.startswith("tachycardic", i, n)
        if answer == 1:
            print(bool(1))
            m = 1
    if m == 0:
        print(bool(0))
    return bool(m)


# main code
def main_code():
    A = receive_input()
    is_tachycardic(A)


if __name__ == "__main__":
    main_code()
