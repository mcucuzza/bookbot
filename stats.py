def words_in_text(text):
    return len(text.split())

def count_letters(text):
    counts = {}

    for word in text.split():
        for letter in word:
            letter = letter.lower()
            if (letter in counts):
                counts[letter] += 1
            else:
                counts[letter] = 1

    return counts

def sort_count(dict):
    return dict["count"]

def sort_frequencies(dict):
    freqs = []
    for key in dict.keys():
        freqs.append({"letter": key, "count": dict[key]})

    freqs.sort(reverse=True, key=sort_count)

    return freqs