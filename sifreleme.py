from AES import aes
import ezhashlib as ehl
from PIL import Image
from datetime import datetime
from stegano import lsb

def newImage(height,width,newRED,newGREEN,newBLUE):
    newData=[]
    for i in range(0, int(height*(width/2))):
        newData.append((newRED[i],newGREEN[i],newBLUE[i]))
    return newData

def renk_sifreleme(RGB, kullanici):
    list = []
    x = kullanici
    for i in range(0, len(RGB),2):
            # t=(ilkpixel+ikincipixel*x)mod255
            t= (RGB[i] if RGB[i]>0 else 1)+((RGB[i+1]if RGB[i+1]>0 else 1)*x)
            list.append(t%255)
    return list

def resim_bolme(imageName):
    im = Image.open(imageName)
    width = im.size[0]
    height = im.size[1]
    pix = im.load()
    RED = []
    GREEN=[]
    BLUE=[]
    for a in range(0, height):
        for b in range(0, width):
            RED.append(pix[b,a][0])
            GREEN.append(pix[b,a][1])
            BLUE.append(pix[b,a][2])

    for v in range(1, 5):
        newRED = renk_sifreleme(RGB=RED, kullanici=v)
        newGREEN = renk_sifreleme(RGB=GREEN, kullanici=v)
        newBLUE = renk_sifreleme(RGB=BLUE, kullanici=v)
        newData = newImage(height, width, newRED, newGREEN, newBLUE)
        newim = Image.new("RGB", (int(width / 2), int(height)))
        newim.putdata(data=newData)
        newim.save(str(v) + ".png")

def aesSifreleme(imageName,v):
    RGB=[]
    newDATA=[]
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
        if len(RGB)%16!=0:
            for a in range(0,len(RGB)):
                RGB.append((0,0,0))
        for i in range(0,16):
            tRED.append(RGB[index + i][0])
            tGREEN.append(RGB[index + i][1])
            tBLUE.append(RGB[index + i][2])

        tRED = AES.encrypt(tRED)
        tGREEN = AES.encrypt(tGREEN)
        tBLUE = AES.encrypt(tBLUE)
        for k in range(0,16):
             newDATA.append((tRED[k],tGREEN[k],tBLUE[k]))

    newim = Image.new("RGB", (int(width), int(height)))
    newim.putdata(data=newDATA)
    newim.save(str(v) + '.png')

def basla(imageName):
    baslangic = datetime.now()
    secret = lsb.hide(imageName, message)
    secret.save("secret.png")

    resim_bolme('secret.png')

    for v in range(1, 5):
        aesSifreleme(str(v)+'.png',v)
    print(' RGB şifreleme bitti --- şifreleme Süresi : ', (datetime.now() - baslangic))

imageName=input('şifrelenecek resimin adı : ')
key = input('şifre : ')
message = input('gizlenecek mesaj : ')
masterKEY = ehl.sha256(key)
print('256 bit şifre :', masterKEY)
print('şifrenin anahtara dönüştürülmüş hali: ', int(masterKEY, 16))
AES = aes(int(masterKEY, 16))
basla(imageName)
