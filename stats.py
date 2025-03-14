def word_count(text):
    num_words = len(text.split())
    return num_words
    
def character_count(text):
    char_count = {}
    for character in text:
        character = character.lower()
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    return char_count

def sort_character_counts(char_count):
    sorted_char_list = [{'character': char, 'count': count} for char, count in char_count.items()]
    sorted_char_list.sort(key=lambda x: x['count'], reverse=True)
    return sorted_char_list