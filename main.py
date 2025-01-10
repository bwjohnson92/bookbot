def read_file(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    return len(text.split())

def count_characters(text):
    lowered_text = text.lower()
    letter_map = {}
    for letter in lowered_text:
        if not letter.isalpha():
            continue
        if letter not in letter_map:
            letter_map[letter] = 0
        letter_map[letter] = letter_map[letter] + 1
    return letter_map

def sort_on(dict):
    return dict["num"]

def sort_map(map):
    map.sort(reverse=True, key=sort_on)
    return map

def dict_to_list_dict(map):
    list = []
    for k,v in map.items():
        list.append({"name":k,"num":v})
    sort_map(list)
    return list


def print_report(path, word_count, letter_map):
    sorted_dict = dict_to_list_dict(letter_map)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")
    for i in sorted_dict:
        char = i["name"]
        num = i["num"]
        print(f"The '{char}' character was found {num} times")
    print(f"--- End report ---")

def book_report(file_name):
    book = read_file(file_name)
    word_count = count_words(book)
    character_counts = count_characters(book)
    print_report(file_name, word_count, character_counts)



def main():
    book_report("books/frankenstein.txt")

main()

