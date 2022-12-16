def likes(names):
    if not names:
        return 'Никто не оценил данную запись'
    elif len(names) == 1:
        return names[0] + 'оценил(а) данную запись'
    elif len(names) == 2