""" Написать программу, которая просит ввести номер карточки и после успешного введения номера,
маскирует все символы кроме последних четырех. Нужно добавить проверку на введенный номер.
(не должно быть букв и количество цифр должно = 16)"""
def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]
print(card_hide("8754456321113213"))

def card_1_number (card_1):
    if card_1 in (16, 18, 19): return "true"
    else: return "error"
print(card_1_number(int(input("Ввести количество цифр карты:"))))