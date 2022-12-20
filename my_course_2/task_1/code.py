word, n, lst = input(), int(input()), []

for _ in range(n):
    lst.append(input())

str_vov = list('а, у, о, ы, и, э, я, ю, ё, е'.replace(', ', ''))

indexes = []

for i in range(len(word)):
    if word[i] in str_vov:
        indexes.append(i)

result = []

for w in lst:
    indexes_checking = []
    for letter_index in range(len(w)):
        if len(list(filter(lambda x: x in str_vov, word))) == len(list(filter(lambda y: y in str_vov, w))):
            if w[letter_index] in str_vov and letter_index in indexes:
                indexes_checking.append(letter_index)
    if set(indexes) == set(indexes_checking):
        result.append(w)

print(*[i for i in lst if i in result], sep='\n')