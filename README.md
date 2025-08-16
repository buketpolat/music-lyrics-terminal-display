# 🎵 Music Lyrics Terminal Display  

Bu proje, terminal üzerinde şarkı sözlerini **renkli** ve **yavaş yavaş akarak** gösteren basit bir Python uygulamasıdır.  
Örnek olarak **Evanescence - Bring Me To Life** şarkı sözleri kullanılmıştır.  

## 🚀 Özellikler  
- Terminal ekranında şarkı sözlerini harf harf yazdırır.  
- Renkli yazı desteği için **colorama** kütüphanesini kullanır.  
- Karaoke tarzı efekt için harf arası gecikme eklenmiştir.  

## 📦 Gereksinimler  
Python 3.x ve aşağıdaki kütüphane gereklidir:  

```bash
pip install colorama
```

## ▶️ Kullanım  
1. Depoyu klonlayın veya `music.py` dosyasını indirin.  
2. Terminalde çalıştırın:  

```bash
python music.py
```

3. Şarkı sözleri renkli ve efektli bir şekilde ekranda görünecektir.  

## 🛠 Özelleştirme  
- `lyrics` listesine istediğiniz şarkı sözlerini ekleyebilirsiniz.  
- `time.sleep(0.06)` değerini değiştirerek yazı hızını ayarlayabilirsiniz.  
- Renkleri değiştirmek için `colors` listesinde düzenleme yapabilirsiniz.  

## 📷 Örnek Çıktı  

```
== Bring Me To Life ==

(Wake me up)wake me up inside
(I can't wake up)wake me up inside
(Save me)call my name and save me from the dark
...
```
