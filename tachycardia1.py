# receive input
def receive_input():
    string = input("Enter the string for testing:")
    return string


# check if there is "tachycardic" in the string input
# tolerate 1 to 2 missing/misspelled letters
def is_tachycardic(A):
    a = A.lower()
    n = len(a)
    m = 0
    target = "tachycardic"
    k = len(target)
    same_letter = 0
    new_str = []
    for i in range(n):
        answer = a.startswith("t", i, n)
        if answer == bool(1):
            for j in range(k):
                if i + j <= n-1:
                    new_str.append(a[i+j])
            for x in new_str:
                if x in target:
                    same_letter = same_letter + 1
                if same_letter >= k-2:
                    m = 1
    if m == 0:
        print(bool(0))
    if m == 1:
        print(bool(1))
    return bool(m)


# main code
def main_code():
    A = receive_input()
    is_tachycardic(A)


if __name__ == "__main__":
    main_code()
