def is_palindrome(phrase):
    stripped_phrase_list = [letter.lower() for letter in phrase if letter.isalpha()]
    stripped_phrase = "".join(stripped_phrase_list)
    return stripped_phrase == "".join(reversed(stripped_phrase))

if __name__ == "__main__":
    phrase = input("Enter a phrase: ")
    print(is_palindrome(phrase))
