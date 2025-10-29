# Klo. 🎮

Klotski bulmaca oyunu - Pygame ile geliştirilmiş modern ve eğlenceli bir puzzle oyunu.

## 🎯 Özellikler

- **Süre Takibi**: Ne kadar hızlı çözdüğünüzü görün
- **Hamle Sayacı**: Minimum hamleyle çözmeye çalışın
- **Modern UI**: Koyu tema, çerçeveli arayüz, renkli bloklar
- **Sürükle-Bırak**: Blokları fare ile sürükleyerek hareket ettirin
- **8-bit Sesler**: Nostaljik 8-bit temalı ses efektleri
- **Arkaplan Müziği**: Müzik albümü (yapımcılar müzik isimlerinde belirtilmiştir)
- **Çoklu Dil**: Türkçe ve İngilizce dil desteği
- **Tam Ekran Modu**: F11 ile tam ekran oynayın
- **Ayarlar Menüsü**: Ses seviyesi, müzik seviyesi ve dil ayarları

## 🎮 Kontroller

- **FARE**: Blokları sürükleyip bırakarak hareket ettirin
- **H**: İpucu göster
- **U**: Son hamleyi geri al
- **R**: Yeniden başla
- **ESC**: Ana menüye dön
- **F11**: Tam ekran modunu aç/kapa

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler

- Python 3.7+
- pygame

### Kurulum

```bash
# Bağımlılıkları yükle
pip install -r requirements.txt

# Oyunu çalıştır
python main.py
```

## 📦 Proje Yapısı

```
klotski_pygame_styled/
├── main.py              # Ana oyun dosyası
├── assets/
│   ├── audio/           # Ses dosyaları (otomatik oluşturulur)
│   └── fonts/           # Bytesized font dosyası
├── levels/              # Oyun seviyeleri
├── settings.json        # Ayarlar (otomatik oluşturulur)
└── requirements.txt     # Python bağımlılıkları
```

## 🎵 Müzik

Oyun içerisinde kullanılan müzikler, müzik dosya isimlerinde belirtilen yapımcılar tarafından hazırlanmıştır.

## 🌍 Dil Desteği

- 🇹🇷 Türkçe
- 🇬🇧 English

Dili ayarlar menüsünden değiştirebilirsiniz.

## 🌐 Demo

Projenin GitHub Pages demo sayfasını ziyaret edin:

🔗 **[GitHub Pages Demo](https://ness246.github.io/Klo./)**

## 📝 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.

---

**Geliştirici**: Ness246  
**Oyun Adı**: Klo.  
**Platform**: Windows, macOS, Linux (Python + Pygame)
