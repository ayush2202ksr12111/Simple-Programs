# python program to capitialize first character of a string

def first_cap(word):
# first we are going to determine the length of a word
    word_len= len(word)
    # then we are fetch the string first character and captialize it
    f_c = word[0].capitalize()
    # we are going to create an empty with only first capital  character in a new string 
    n_w=f_c
    # now we are going to add every other character in new string using for loop and then retutning new string
    for i in range(1, word_len):
        n_w+=word[i]
    return n_w
    

print(first_cap("ram"))
    
