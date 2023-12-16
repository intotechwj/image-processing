import cv2
import cvzone
from cvzone.ColorModule import ColorFinder

# video dosyası
yakala = cv2.VideoCapture('video/sample2.mp4')

# kameradan görüntü
#yakala = cv2.VideoCapture(0)

# renk yakalama
renkBul = ColorFinder(False)

# sample penaltı 200
#hsvVals = {'hmin': 0, 'smin': 0, 'vmin': 136, 'hmax': 179, 'smax': 77, 'vmax': 255}

# sample1 futbol 50
# hsvVals = {'hmin': 44, 'smin': 33, 'vmin': 214, 'hmax': 77, 'smax': 90, 'vmax': 255}

# sample2 basket 2200
hsvVals = {'hmin': 4, 'smin': 71, 'vmin': 112, 'hmax': 10, 'smax': 255, 'vmax': 255}

# sample3 kamera 500
#hsvVals= {'hmin': 104, 'smin': 90, 'vmin': 84, 'hmax': 140, 'smax': 255, 'vmax': 255}
# sample4 kamera 400
# hsvVals = {'hmin': 96, 'smin': 107, 'vmin': 130, 'hmax': 152, 'smax': 255, 'vmax': 255}

# -------------------------------------------------------------------------------------

# pozisyon
posList = []

while True:

    # dosya
    ok, img = yakala.read()
    #img = cv2.imread("sample5.jpg")

    # renk ayarı
    imgRenk, maske = renkBul.update(img, hsvVals)

    # top lokasyonu
    imgKontur, Kontur = cvzone.findContours(img, maske, minArea=2000)

    # kamerada top lokasyon takibi
    if Kontur:
        posList.append(Kontur[0]['center'])

    for i, pozisyon in enumerate(posList):
        cv2.circle(imgKontur, pozisyon, 5, (0, 255, 0), cv2.FILLED)
        cv2.line(imgKontur, pozisyon, posList[i - 1], (0, 0, 255), 2)

    # görüntüleme
    imgRenk = cv2.resize(imgKontur, (0, 0), None, 1.7, 1.7)
    # cv2.imshow("image", img)
    cv2.imshow("imageRenk", imgKontur)
    cv2.waitKey(50)
