def has_all_vowels(word):
    required = {"a", "e", "i", "o", "u"}
    word = word.lower()
    for vowel in "aeiou":
        if vowel not in word:
            return False
    
    else:
        return True


print(has_all_vowels("education"))