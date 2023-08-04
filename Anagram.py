def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    
    char_freq1 = {}
    char_freq2 = {}
    for char in str1:
        char_freq1[char] = char_freq1.get(char, 0) + 1
    for char in str2:
        char_freq2[char] = char_freq2.get(char, 0) + 1
    return char_freq1 == char_freq2


if __name__ == "__main__":
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")
    if are_anagrams(word1, word2):
        print(f"{word1} and {word2} are anagrams.")
    else:
        print(f"{word1} and {word2} are not anagrams.")
