def main():
    text = get_text("./books/frankenstein.txt")
    word_count = get_word_count(text)
    character_counts = get_character_counts(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    for character_count in character_counts:
        print(f"The `{(character_count['character'])}` character was found {(character_count['count'])} times")
    print("--- End report ---")

def get_text(filename):
    with open("./books/frankenstein.txt") as f:
        text = f.read()
        return text

def get_word_count(text):
    count = len(text.split())
    return count

def get_character_counts(text):
    counts = {}
    for character in text:
        if character.isalpha():
            lowerCharacter = character.lower()
            if lowerCharacter in counts:
                counts[lowerCharacter] += 1
            else:
                counts[lowerCharacter] = 1
    sorted_counts = sort_character_counts(counts)
    return sorted_counts

def sort_character_counts(character_counts):
    sorted_counts = []
    for character_count in character_counts:
        count = character_counts[character_count]
        sorted_counts.append({ "character": character_count, "count": count })
    sorted_counts.sort(reverse=True, key=sort_character_counts_on)
    return sorted_counts


def sort_character_counts_on(character_counts):
    return character_counts["count"]


main()