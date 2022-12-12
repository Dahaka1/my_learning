with open('goats.txt') as file_in:
    text = list(map(lambda x: str(x).rstrip(), file_in.readlines()))
    colours = text[text.index('COLOURS') + 1:text.index('GOATS')]
    goats = text[text.index('GOATS') + 1:]
    with open('answer.txt', 'w') as file_out:
        print(*filter(lambda x: goats.count(x) > len(goats) * 0.07, colours), sep='\n', file=file_out)