from curses.ascii import isdigit

sentence ="The quick brown fox jumped over a lazy dog"
#builtin functionality
#functions
print(sentence)
print(sentence.upper()) #calling a function
print(sentence.lower())
print(sentence.title())
print(sentence.count("dog"))



sentence= "99"
if sentence.isspace()or sentence.isdigit() or sentence.isnumeric():
    print("Invalid Name")
else:
    print("Valid Name")