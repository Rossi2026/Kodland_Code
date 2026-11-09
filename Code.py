meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor\n",
            "STALKEAR": "Investigar a vida de alguém online\n",
            }
val = 1
while val < 5:
    word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas):\n ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("A palavra não está no dicionário. Tente novamente.\n ")
    val +=1
