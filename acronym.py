from itertools import permutations

def acronym(input):
    words = input.split(" ")
    letters = []
    output = []
    for w in words:
        letters.append(w[0].upper())
    perm = permutations(letters)
    for letter_list in perm:
        temp = ""
        for letter in letter_list:
            temp += letter
        output.append(temp)
    return output
