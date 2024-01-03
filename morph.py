import pymorphy3
morph = pymorphy3.MorphAnalyzer(lang='ru')


def decline_noun_by_number(number, word):
    parsed_word = morph.parse(word)[0]
    plural_form = parsed_word.make_agree_with_number(number).word
    return f"{number} {plural_form}"