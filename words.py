def print_upper_words(words, must_start_with):
    allowed = str(must_start_with)
    for word in words: 
        if(word[0] in allowed): 
            print(word.upper())

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})