def sort_string(phrase):
    phrase_list = phrase.split(" ")
    sorted_phrase_list = sorted(phrase_list, key=lambda x: x.lower())
    return " ".join(sorted_phrase_list)

if __name__ == "__main__":
    phrase = input("Enter a string: ")
    print(sort_string(phrase))
