from collections import Counter


def unique(lst):
    return len(lst) == len(set(lst))


def anagram(x, y):
    return Counter(x) == Counter(y)


def compact(lst):
    return list(filter(None, lst))


def vowel(string):
    return [each for each in string if each in 'aeiou']


def decapitalize(string):
    return string[:1].lower() + string[1:]


def duplicate(lst):
    return len(lst) != len(set(lst))
