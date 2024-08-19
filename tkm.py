import random
import time
def kurallar():
    print("Taş makası yener.")
    print("Kağıt taşı yener.")
    print("Makas kağıdı yener.")
    print("Bunlara uygun olan seçimi yapan oyuncu turu kazanır.")
    print("Galibiyet sayısı 2 olan oyuncu oyunu kazanır.")
    print("Oyundan çıkmak için 'exit' yazmalısınız.")

def start():
    L = ["taş", "kağıt", "makas"]
    oyuncu_galibiyeti = 0
    bilgisayar_galibiyeti = 0
    oyun_sayisi = 0
    
    while True:
        oyun_sayisi += 1
        print(f"\n{oyun_sayisi}. Oyun Başlıyor...")
        
        oyuncu_kazanim = 0
        bilgisayar_kazanim = 0
        
        while oyuncu_kazanim < 2 and bilgisayar_kazanim < 2:
            print("Windows tercihini yaptı.")
            player = input("Lütfen bir seçim yapınız (taş, kağıt, makas): \n").lower()
            if player == 'exit':
                print("Oyundan çıkılıyor...")
                return
            if player not in L:
                print("Yanlış tercih yapıldı. Ana menüye yönlendiriliyor...")
                kurallar()
                continue

            w = random.choice(L)
            print(f"Seçimler yapıldı: Windows'un seçimi = {w} \n Kullanıcı seçimi = {player}")

            if (player == "taş" and w == "makas") or \
               (player == "kağıt" and w == "taş") or \
               (player == "makas" and w == "kağıt"):
                print("Kullanıcı turu kazandı!")
                oyuncu_kazanim += 1
            elif player == w:
                print("Berabere kalındı, yeniden başlanacak.")
                continue
            else:
                print("Windows turu kazandı!")
                bilgisayar_kazanim += 1
        
        if oyuncu_kazanim == 2:
            oyuncu_galibiyeti += 1
            print(f"{oyun_sayisi}. Oyunu Siz Kazandınız!")
        else:
            bilgisayar_galibiyeti += 1
            print(f"{oyun_sayisi}. Oyunu Windows Kazandı!")
        
        tekrar = input("Başka bir oyun oynamak ister misiniz? (E/H): ").lower()
        if tekrar != 'e':
            print(f"Oyun Bitti! Toplam {oyuncu_galibiyeti} kez kazandınız, Windows {bilgisayar_galibiyeti} kez kazandı.")
            break

def tas_kagit_makas_selda_erdal():
    print("Hoşgeldiniz. Taş, Kağıt, Makas oyununda Windows rastgele bir seçim yapar ve seçim sırası size geçer.")
    print("Her iki taraf da seçimini yaptığında oyun kazananın hanesine 1 puan ekler ve tur sayacı 1 artar.")
    print("Oyunu kazanmanın kuralları gayet basit. Eğer kuralları öğrenmek istiyorsanız 'yardım' yazabilirsiniz.")
    print("Oyuna hemen başlamak için 'başla' yazınız. Oyundan çıkmak için 'exit' yazmalısınız.")

    while True:
        menu = input("Ne yapmak istiyorsunuz? (başla, yardım, exit):\n ").lower()
        if menu == "başla":
            print("Oyun başlıyor...(3sn)")
            time.sleep(3)
            start()
        elif menu == "yardım":
            kurallar()
        elif menu == "exit":
            print("Oyun sonlandırılıyor... (3sn) ")
            time.sleep(3)
            break
        else:
            print("Geçersiz seçenek, lütfen tekrar deneyin.")

# Oyunu başlat
tas_kagit_makas_selda_erdal()

print("Biz bu uygulamayi Selda Yeleser & Erdal Kabacaoğlu ekip çalışmasıyla geliştirdik bilginize.")