"""
CP1404/CP5632 Practical
Word occurrences Program
"""

"""
Word Occurrences
Estimate: 60 minutes
Actual:   64 minutes
"""

text = "this is a collection of words of nice words this is a fun thing it is"
words = (text.split())
TEXT_TO_COUNT = {}
print("Text:", text)

string = input(">>> ")
for word in words:
    if word in TEXT_TO_COUNT:
        TEXT_TO_COUNT[word] += 1
    else:
        TEXT_TO_COUNT[word] = 1

width = max(len(word) for word in TEXT_TO_COUNT)

for word, count in sorted(TEXT_TO_COUNT.items()):
    print(f"{word:{width}} : {count}")




