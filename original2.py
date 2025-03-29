import random 
h = float
quizList = ["ヒント❶：赤い食べ物"+"\n"
           +"ヒント❷：丸い果物"+"\n"
           +"ヒント❸：最初に「り」がつく"+"\n"
           +"\n"
           +"この食べ物何でしょう"+"\n"+
           "選択肢1：いちご"+"\n"
           +"選択肢2：トマト"+"\n"
           +"選択肢3：りんご"+"\n"
           +">",
'''
ヒント❶:鳥
ヒント❷：黒い
ヒント❸：「カーカー」と鳴く
この生き物何でしょう
選択肢1：ハト
選択肢2：カラス
選択肢3：すずめ
>'''
]

choiced = random.randint(0,1)
#print("choiced is ",choiced)
h = int(input(quizList[choiced]))

if h.isdigit():
    printh = int(input(quizList[choiced]))

else:
    print("数値じゃないよ")
#print("h is '",h,"'")

if choiced == 0:
    if h == 3:
        print("正解！")
        print("おめでとう！")
    else:
        print("残念")
        print("正解は❸　の「りんご」でした")


if choiced == 1:
    if h == 2:
        print("正解！")
        print("おめでとう！")
    else:
        print("残念")
        print("正解は❷　の「カラス」でした")