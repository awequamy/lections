string = input('enter any sentence')
reversed_string = string.split()
reversed_words = list(reversed(reversed_string))
print(" ".join(reversed_words))



# or



def ReverseSentence():
    string = input('enter any sentence')
    reversed_string = string.split()
    reversed_words = list(reversed(reversed_string))
    print(" ".join(reversed_words))

ReverseSentence()