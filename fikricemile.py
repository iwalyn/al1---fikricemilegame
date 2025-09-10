import random
import time

karaktercan = 120
fikrican = 200
cemilecan = 200
bosshasarr = random.randint(20, 100)


#karakter ismi
#yol seçimi
#karşılama
#kaçma olasılığı
#savaş

karakterismi = str(input("KARAKTERİNE İSİM VER:     "))
yolseçimi = int(input("CHOOSE YOUR WAY: 1(KARANLIK ORMAN), 2(TERKEDİLMİŞ KALE)"))
if yolseçimi == 1:
    print("SİSLİ VE ÜRPERTİCİ ORMANDA İLERLERKEN KARŞINA BİR ANDA FİKRİ İSMİNDE ANTİK BİR CANAVAR ÇIKIYOR.")
    time.sleep(3)
    print("SENİ GÖREBİLİR VEYA GÖRMEYEBİLİR DİKKAT ET.")
    time.sleep(3)
    print(".")
    time.sleep(3)
    print(".")
    time.sleep(3)
    print(".")
    olasılık = random.randint(1,2)
    if olasılık == 1:
        print("FİKRİ SENİ GÖRDÜ ÇABUK SAVAŞ POZİSYONU AL!!!")
        while karaktercan > 0 and fikrican > 0:
            aksiyonsor = int(input("SAVAŞ TEKNİĞİ... 1(TEKME) 2(YUMRUK) 3(FİYUFİT)"))
            if aksiyonsor == 1:
                hasarr = 40
            elif aksiyonsor == 2:
                hasarr = 50
            elif aksiyonsor == 3:
                hasarr = 100
            else:
                print("NABİON...")
                continue
        #boss'a hasar atıcaz
            fikrican -= hasarr
            print(f"FİKRİ -{hasarr} can kaybederek {fikrican}'a düştü")
            if fikrican <= 0:
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(1)
                print("...")
                print("FİKRİYİ ALT ETTİN...")
                break
            else:
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(1)
                print("...")
                print("İTS FİKRİ'S TURN")
                karaktercan -= bosshasarr
                print(f"{karakterismi} isimli karakter -{bosshasarr} hasar alarak canı {karaktercan}'a düştü")
                if karaktercan <= 0:
                    print(f"{karakterismi} ÖLDÜ...")
                    break
    else:
        print("FİKRİ SENİ GÖRMEDİ TÜYLERİNİ DÜZELTMEKLE MEŞGULDÜ HER ŞEY YOLUNDA.")
elif yolseçimi == 2:
    print("TERKEDİLMİŞ KİLİSEDE İLERLERKEN CEMİLE İSMİNDE ANTİK BİR CANAVARLA KARŞILAŞIYORSUN.")
    print("Seni duyabilir sessiz ol...")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    olasılık = random.randint(1,2)
    if olasılık == 1:
        print("SENİ FARKETTİ SAVAŞA HAZIRLAN!")
        while karaktercan > 0 and fikrican > 0:
            aksiyonsor = int(input("AKSİYONUNU SEÇ 1(TEKME) 2(YUMRUK) 3(ATEŞ TOPU)"))
            if aksiyonsor == 1:
                hasarr = 40
            elif aksiyonsor == 2:
                hasarr = 50
            elif aksiyonsor == 3:
                hasarr = 100
            else:
                print("Kanka nabiyon...")
                continue
        #boss'a hasar atıcaz
            fikrican -= hasarr
            print(f"CEMİLE -{hasarr} can kaybederek {fikrican}'a düştü")
            if fikrican <= 0:
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(1)
                print("...")
                print("CEMİLE YENİLDİ...")
                break
            else:
                time.sleep(3)
                print("İTS CEMİLE'S TURN")
                karaktercan -= bosshasarr
                time.sleep(1)
                print(".")
                time.sleep(1)
                print("..")
                time.sleep(1)
                print("...")
                print(f"{karakterismi} isimli karakter -{bosshasarr} hasar alarak canı {karaktercan}'a düştü")
                if karaktercan <= 0:
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("..")
                    time.sleep(1)
                    print("...")
                    print(f"{karakterismi} died...")
                    break
    else:
        print("Seni farketmedi ve kurtuldun.")




