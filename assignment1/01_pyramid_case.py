# EX 1.1- basic python: Pyramid case
# Implement a function that get a string input and outputs the same word, only each odd char is lower
# case and each even letter is upper case
# You can assume that the input is a valid string which contains only english letters.


def pyramid_case(in_word):
    # TODO: return the pyramid case word.
    out_word = ""
    ch = ""
    for i in range(len(in_word)):
        if i%2==0:
            ch = in_word[i].lower()
        else:
            ch = in_word[i].upper()
        out_word += ch
    return out_word 

def pyramid_case_one_liner(in_word):
    # TODO: return the pyramid case word in one line of code inside the function.
    return ''.join(in_word[i].lower() if i%2==0 else in_word[i].upper() for i in range(len(in_word)))
    # DO NOT USE ";" IN YOUR CODE.


# test functions here
input_words = ["hello", "world", "", "I", "am", "LEARNING", "Python"]

print("==== pyramid_case() results:")
for word in input_words:
    print(pyramid_case(word))

print("\n==== pyramid_case_one_liner() results:")
for word in input_words:
    print(pyramid_case_one_liner(word))
