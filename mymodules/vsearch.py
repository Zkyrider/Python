﻿def search4vowels(phrase:str) -> set:
    '''Возвращает гласныеб найденные в указанной фразе.'''
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase:str, letters:str) -> set:
    '''Возвращает множество букв из letters, найденных
     в указанной фразе'''
    return set(letters).intersection(set(phrase))