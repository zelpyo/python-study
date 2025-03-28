import random
def omikuji():
    kuji = ['大吉','中吉','小吉','凶','半吉','末吉','大凶','大大吉']
    return random.choice(kuji)
kekka = omikuji()
print("結果は",kekka,"です")