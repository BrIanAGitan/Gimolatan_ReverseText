def reverse_text(text):
    return text[::-1]


def has_numbers(text):
    return any(char.isdigit() for char in text)


while True:
    user_input = input("Enter a string: ")

    if has_numbers(user_input):
        print("Error Reported! Enter text only.")
    else:
        reversed_text = reverse_text(user_input)
        print(f"Output: {reversed_text}")
        break
