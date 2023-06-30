sesli_harfler = 'aeıioöuü'
sayaç = 0

kelime = input('bir kelime giriniz: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır(sayaç):
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç

mesaj = '{} kelimesinde {} sesli harf vardır.'
print(mesaj.format(kelime, artır(sayaç)))