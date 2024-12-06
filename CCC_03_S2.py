def syllable_getter(word):
    vowels = "aeiou"
    for i in range(len(word) - 1, -1, -1):
        if word[i].lower() in vowels:
            return word[i:].lower()
    return word.lower()

def rhymes(verse):
    syllables = []
    for line in verse:
        words = line.split()
        last_word = words[-1]
        syllable = syllable_getter(last_word)
        syllables.append(syllable)

    if syllables[0] == syllables[1] == syllables[2] == syllables[3]:
        return "perfect"
    elif syllables[0] == syllables[1] and syllables[2] == syllables[3]:
        return "even"
    elif syllables[0] == syllables[2] and syllables[1] == syllables[3]:
        return "cross"
    elif syllables[0] == syllables[3] and syllables[1] == syllables[2]:
        return "shell"
    else:
        return "free"

num_verses = int(input())
verses = []

for i in range(num_verses):
    verse = []
    for j in range(4):
        line = input()
        verse.append(line)
    verses.append(verse)

for verse in verses:
    print(rhymes(verse))
