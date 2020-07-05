from AES import aes
import ezhashlib as ehl
from PIL import Image
from datetime import datetime
from stegano import lsb
from sympy.abc import x
from sympy import *

def renkBirlestirme(height,width,newRED,newGREEN,newBLUE):
    newData=[]
    for i in range(0, (height*(width*2))):
        newData.append((newRED[i],newGREEN[i],newBLUE[i]))
    return newData

def modlama(bolunen,bolum):
    if int(bolunen)==0:
        return 255
    elif type(bolunen/bolum)==Integer:
        if int(bolunen/bolum) == 255:
            return 255
        else:
            return (bolunen/bolum)%255
    else:
        return modlama(bolunen+255,bolum)

def cozme(RGB,RGB2,k1,k2):
    list = []
    for i in range(0,len(RGB)):

                Denklem = (expand((RGB[i]) * (x - k2)) - expand((RGB2[i]) * (x - k1)))
                Denklem = Denklem.as_coefficients_dict()
                list.append(modlama(Denklem[1], (k1 - k2)))
                list.append(modlama(Denklem[x], (k1 - k2)))

    return list

def birlestirme(k1,k2):
    im = Image.open(str(k1) + '.png')
    im2 = Image.open(str(k2) + '.png')

    width = im.size[0]
    height = im.size[1]

    pix = im.load()
    pix2 = im2.load()

    RED1 = []
    GREEN1 = []
    BLUE1 = []
    RED2 = []
    GREEN2 = []
    BLUE2 = []

    for a in range(0, height):
        for b in range(0, width):
            RED1.append(pix[b, a][0])
            GREEN1.append(pix[b, a][1])
            BLUE1.append(pix[b, a][2])
            RED2.append(pix2[b, a][0])
            GREEN2.append(pix2[b, a][1])
            BLUE2.append(pix2[b, a][2])

    newRED = cozme(RGB=RED1, RGB2=RED2,k1=k1,k2=k2)
    newGREEN = cozme(RGB=GREEN1, RGB2=GREEN2, k1=k1, k2=k2)
    newBLUE = cozme(RGB=BLUE1, RGB2=BLUE2, k1=k1, k2=k2)
    newim = Image.new("RGB", (int(width * 2), int(height)))
    newRGB = renkBirlestirme(height,width,newRED,newGREEN,newBLUE)
    newim.putdata(data=newRGB)
    newim.save("ÇözülmüşResimRGB.png")

def aesCozme(imageName):
    newDATA = []
    RGB = []
    im = Image.open(imageName)
    width = im.size[0]
    height = im.size[1]
    pix = im.load()

    for a in range(0, height):
        for b in range(0, width):
            RGB.append(pix[b,a])

    for index in range(0,len(RGB),16):
        tRED=[]
        tGREEN = []
        tBLUE = []
        for i in range(0,16):
            tRED.append(RGB[index + i][0])
            tGREEN.append(RGB[index + i][1])
            tBLUE.append(RGB[index + i][2])

        tRED = cipher.decrypt(tRED)
        tGREEN = cipher.decrypt(tGREEN)
        tBLUE = cipher.decrypt(tBLUE)
        for k in range(0,16):
             newDATA.append((tRED[k],tGREEN[k],tBLUE[k]))

    newim = Image.new("RGB", (int(width), int(height)))
    newim.putdata(data=newDATA)
    newim.save(imageName)

def basla(k1,k2):
    baslangic = datetime.now()
    aesCozme(str(k1)+'.png')
    aesCozme(str(k2)+'.png')
    birlestirme(k1,k2)
    clear_message = lsb.reveal('ÇözülmüşResimRGB.png')
    print('resime gizlenmiş olan veri : ', clear_message)
    print('RGB çözme bitti --- çözme Süresi : ', (datetime.now() - baslangic))

k1 = int(input('seçilecek 1. resim : '))
k2 = int(input('seçilecek 2. resim : '))
key = input('şifre : ')
masterKEY=ehl.sha256(key)
print('256 bit şifre :' ,masterKEY)
print('şifrenin anahtara dönüştürülmüş hali: ',int(masterKEY,16))
cipher = aes(int(masterKEY,16))

basla(k1,k2)

