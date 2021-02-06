#son kiritiladi shu sonni raqamlarini so`z bilan yozing!
'''son = input('Son kiriting: ')
raqam = {
    "0": "nol",
    "1": "bir",
    "2": "ikki",
    "3": "uch",
    "4": "to`rt",
    "5": "besh",
    "6": "olti",
    "7": "yetti",
    "8": "sakkiz",
    "9": "to`qqiz"
}
for i in son:
    print(raqam.get(i),end=' ')
'''

#Funksiya yozish
def salomlashish():
    print("Assalomu aleykum")

salomlashish()

#funksiyaga parametr kiritish
def inson1(ism):
    print(f"Assalomu aleykum, {ism}")

inson1("Anvar")

def inson2(ism,familiya):
    print(f"Assalomu aleykum, {ism} {familiya} !")

inson2("Anvar","Sobirov")
