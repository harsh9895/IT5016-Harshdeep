def reverse_string(s):
    reverse_string = ""
    for char in s:
        reverse_string = char + reverse_string
    return reverse_string


def main():
    original_string = input("Enter a string:")
    reversed_string = reverse_string(original_string)
    print(f"Original: {original_string}")
    print(f"Reversed: {reversed_string}")

main()