# Klo. 🎮

<div align="center">

![Klo. Logo](logo.png)

**🇹🇷 Retro 8-bit/16-bit Temalı Klotski Bulmaca Oyunu**  
**🇬🇧 Retro 8-bit/16-bit Themed Klotski Puzzle Game**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-Latest-green.svg)](https://www.pygame.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/ness246/Klo.)

[🌐 Websitesi / Website](https://ness246.github.io/Klo./) • [📦 İndir / Download](https://github.com/ness246/Klo./archive/refs/heads/main.zip) • [🐛 Hata Bildir / Report Bug](https://github.com/ness246/Klo./issues)

**🇹🇷 / 🇬🇧 Bu README iki dilde mevcuttur. Aşağıdan istediğiniz dili seçin.**  
**This README is available in two languages. Choose your preferred language below.**

</div>

---

<details>
<summary><b>🇹🇷 Türkçe / Turkish (Tıklayarak Aç)</b></summary>

## 📖 Hakkında

**Klo.**, 20. yüzyılın başlarında ortaya çıkan klasik Klotski bulmacasının modern bir yorumudur. Retro 8-bit/16-bit estetiğiyle harmanlanmış, göz dostu renkler ve akıcı oynanış sunan bir puzzle oyunudur.

Hedef bloğu (2x2 sarı blok) EXIT noktasına taşıyarak her seviyeyi tamamlayın. Minimum hamle ve süre ile çözerek kendinize meydan okuyun!

## ✨ Özellikler

### 🎨 Görsel ve Tasarım
- **Retro 8-bit/16-bit Tema**: Atari/NES/SNES esintili görsel tasarım
- **Göz Dostu Renkler**: Göz yormayan, yumuşatılmış retro renk paleti
- **Parlayan Efektler**: Blokları sürüklerken hafif glow efektleri
- **Modern Arayüz**: Koyu tema, çerçeveli arayüz, pixelated font desteği

### 🎮 Oynanış
- **Sürükle-Bırak Kontrolleri**: Blokları fare ile akıcı şekilde hareket ettirin
- **Süre Takibi**: Her bulmacayı ne kadar hızlı çözdüğünüzü görün
- **Hamle Sayacı**: Minimum hamleyle çözerek kendinize meydan okuyun
- **Geri Alma**: Son hamleyi geri alın (U tuşu)
- **Yeniden Başlat**: Puzzle'ı sıfırdan başlatın (R tuşu)
- **Önizleme Sistemi**: Blokları sürüklerken altında görünen preview efekti

### 🎵 Ses ve Müzik
- **8-bit Ses Efektleri**: Hareket, hata ve buton tıklama sesleri
- **Arkaplan Müziği**: Çeşitli retro temalı müzik parçaları
- **Ses Kontrolleri**: Ses efekti ve müzik seviyelerini ayarlayın
- **Dinamik Müzik**: Oyun başladığında rastgele müzik seçimi

### 🌍 Dil ve Yerelleştirme
- **Çoklu Dil Desteği**: Türkçe ve İngilizce
- **Kolay Dil Değiştirme**: Ayarlar menüsünden dil seçimi
- **Yerelleştirilmiş Arayüz**: Tüm metinler çeviri sistemine dahil

### ⚙️ Ayarlar ve Özelleştirme
- **Tam Ekran Modu**: F11 ile tam ekran oynayın
- **Ayarlar Menüsü**: Ses, müzik ve dil ayarları
- **Durum Kaydetme**: Oyun tercihleriniz otomatik kaydedilir
- **Esnek Çözünürlük**: Fullscreen'de otomatik ölçeklendirme

### 📚 İçerik
- **Nasıl Oynanır Kısmı**: Oyun kuralları ve kontroller
- **Çoklu Seviye**: Farklı zorluk seviyelerinde bulmacalar
- **Başarı Sistemi**: Her seviye için tamamlanma istatistikleri

## 🎮 Kontroller

| Tuş/İşlem | Açıklama |
|-----------|----------|
| **Fare** | Blokları sürükleyip bırakarak hareket ettirin |
| **U** | Son hamleyi geri al |
| **R** | Bulmacayı yeniden başlat |
| **ESC** | Ana menüye dön / Oyunu duraklat |
| **F11** | Tam ekran modunu aç/kapa |

## 🚀 Kurulum

### Gereksinimler

- **Python 3.7+**
- **Pygame** (otomatik yüklenir)

### Kurulum Adımları

1. **Projeyi İndirin**
   ```bash
   git clone https://github.com/ness246/Klo..git
   cd Klo.
   ```
   
   Veya GitHub'dan ZIP olarak indirin.

2. **Bağımlılıkları Yükleyin**
   ```bash
   pip install -r requirements.txt
   ```

3. **Oyunu Çalıştırın**
   ```bash
   python main.py
   ```

### Font Dosyası (Opsiyonel)

Oyun için özel pixelated font (`Bytesized.ttf`) kullanılmaktadır. Font dosyası `assets/fonts/` klasörüne yerleştirilmelidir. Eğer dosya bulunamazsa, sistem varsayılan fontu kullanılacaktır.

## 📦 Proje Yapısı

```
Klo./
├── main.py                 # Ana oyun dosyası
├── README.md              # Bu dosya
├── LICENSE                # MIT Lisansı
├── requirements.txt        # Python bağımlılıkları
├── settings.json          # Kullanıcı ayarları (otomatik oluşturulur)
├── logo.png              # Oyun logosu
├── index.html            # GitHub Pages web sitesi
├── assets/
│   ├── audio/            # Ses ve müzik dosyaları (otomatik oluşturulur)
│   └── fonts/            # Bytesized.ttf font dosyası
└── levels/               # Oyun seviyeleri (JSON formatında)
    ├── A-01.json
    └── B-01.json
```

## 🎯 Oyun Kuralları

1. **Amaç**: Hedef bloğu (2x2 sarı "T" bloğu) EXIT noktasına taşıyın.
2. **Hareket**: Blokları fare ile sürükleyerek hareket ettirebilirsiniz.
3. **Kısıtlamalar**: Bloklar sadece yatay veya dikey hareket edebilir, çapraz hareket yoktur.
4. **Çarpışma**: Bloklar birbirinin üzerine gelemez veya tahtanın dışına çıkamaz.
5. **Hedef**: EXIT noktası genellikle tahtanın alt kısmında, 2x2 boyutundadır.

## 🎵 Müzik ve Sesler

Oyun içerisinde kullanılan müzikler ve ses efektleri:

- **Ses Efektleri**: 8-bit temalı, programatik olarak oluşturulmuş sesler
- **Arkaplan Müziği**: Retro temalı müzik parçaları
- **Yapımcı Bilgisi**: Müzik yapımcıları müzik dosya isimlerinde belirtilmiştir

## 🌐 Web Sitesi

Projenin web sitesini ziyaret edin:

🔗 **[https://ness246.github.io/Klo./](https://ness246.github.io/Klo./)**

Web sitesi retro 8-bit/16-bit temasıyla tasarlanmış ve projenin tüm bilgilerini içermektedir.

## 🛠️ Teknoloji

- **Python 3.7+**: Programlama dili
- **Pygame**: Oyun motoru ve grafik kütüphanesi
- **JSON**: Seviye ve ayar dosyaları
- **HTML/CSS/JS**: Web sitesi (GitHub Pages)

## 📝 Geliştirme

### Seviye Oluşturma

Seviyeler JSON formatında `levels/` klasöründe saklanır. Örnek format:

```json
{
  "id": "A-01",
  "grid": {"cols": 4, "rows": 5},
  "blocks": [
    {"id": "T", "w": 2, "h": 2, "x": 1, "y": 0, "type": "target", "color": "T"},
    {"id": "L", "w": 1, "h": 2, "x": 0, "y": 0, "color": "red"}
  ],
  "par": 20,
  "exit": [1, 3],
  "difficulty": 2
}
```

### Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## 🐛 Bilinen Sorunlar

Şu anda bilinen önemli bir sorun yoktur. Hata bulursanız lütfen [GitHub Issues](https://github.com/ness246/Klo./issues) üzerinden bildirin.

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. İstediğiniz gibi kullanabilir, değiştirebilir ve dağıtabilirsiniz.

## 👨‍💻 Geliştirici

**Ness246**

- GitHub: [@ness246](https://github.com/ness246)
- Proje: [Klo. Repository](https://github.com/ness246/Klo.)

## 🙏 Teşekkürler

- Klotski bulmacasının orijinal yaratıcıları
- Pygame geliştiricileri
- Retro oyun topluluğu
- Müzik yapımcıları (müzik dosya isimlerinde belirtilmiştir)

## 📞 İletişim

Sorularınız, önerileriniz veya geri bildirimleriniz için [GitHub Issues](https://github.com/ness246/Klo./issues) kullanabilirsiniz.

---

</details>

<details>
<summary><b>🇬🇧 English (Click to Expand)</b></summary>

## 📖 About

**Klo.** is a modern interpretation of the classic Klotski puzzle that originated in the early 20th century. It's a puzzle game that combines retro 8-bit/16-bit aesthetics with eye-friendly colors and smooth gameplay.

Complete each level by moving the target block (2x2 yellow block) to the EXIT point. Challenge yourself to solve with minimum moves and time!

## ✨ Features

### 🎨 Visual and Design
- **Retro 8-bit/16-bit Theme**: Atari/NES/SNES-inspired visual design
- **Eye-Friendly Colors**: Non-straining, muted retro color palette
- **Glow Effects**: Subtle glow effects when dragging blocks
- **Modern Interface**: Dark theme, framed interface, pixelated font support

### 🎮 Gameplay
- **Drag & Drop Controls**: Move blocks smoothly with mouse
- **Time Tracking**: See how fast you solve each puzzle
- **Move Counter**: Challenge yourself to solve with minimum moves
- **Undo**: Undo last move (U key)
- **Restart**: Start puzzle from scratch (R key)
- **Preview System**: Preview effect visible below blocks while dragging

### 🎵 Sound and Music
- **8-bit Sound Effects**: Movement, error, and button click sounds
- **Background Music**: Various retro-themed music tracks
- **Audio Controls**: Adjust sound effect and music levels
- **Dynamic Music**: Random music selection when game starts

### 🌍 Language and Localization
- **Multi-language Support**: Turkish and English
- **Easy Language Switching**: Language selection from settings menu
- **Localized Interface**: All texts included in translation system

### ⚙️ Settings and Customization
- **Fullscreen Mode**: Play in fullscreen with F11
- **Settings Menu**: Sound, music, and language settings
- **State Saving**: Your game preferences are automatically saved
- **Flexible Resolution**: Automatic scaling in fullscreen

### 📚 Content
- **How to Play Section**: Game rules and controls
- **Multiple Levels**: Puzzles with different difficulty levels
- **Achievement System**: Completion statistics for each level

## 🎮 Controls

| Key/Action | Description |
|------------|-------------|
| **Mouse** | Drag and drop blocks to move them |
| **U** | Undo last move |
| **R** | Restart puzzle |
| **ESC** | Return to main menu / Pause game |
| **F11** | Toggle fullscreen mode |

## 🚀 Installation

### Requirements

- **Python 3.7+**
- **Pygame** (automatically installed)

### Installation Steps

1. **Download the Project**
   ```bash
   git clone https://github.com/ness246/Klo..git
   cd Klo.
   ```
   
   Or download as ZIP from GitHub.

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Game**
   ```bash
   python main.py
   ```

### Font File (Optional)

The game uses a special pixelated font (`Bytesized.ttf`). The font file should be placed in the `assets/fonts/` folder. If the file is not found, the system default font will be used.

## 📦 Project Structure

```
Klo./
├── main.py                 # Main game file
├── README.md              # This file
├── LICENSE                # MIT License
├── requirements.txt        # Python dependencies
├── settings.json          # User settings (auto-generated)
├── logo.png              # Game logo
├── index.html            # GitHub Pages website
├── assets/
│   ├── audio/            # Sound and music files (auto-generated)
│   └── fonts/            # Bytesized.ttf font file
└── levels/               # Game levels (JSON format)
    ├── A-01.json
    └── B-01.json
```

## 🎯 Game Rules

1. **Objective**: Move the target block (2x2 yellow "T" block) to the EXIT point.
2. **Movement**: You can move blocks by dragging them with the mouse.
3. **Constraints**: Blocks can only move horizontally or vertically, no diagonal movement.
4. **Collision**: Blocks cannot overlap or go outside the board.
5. **Target**: The EXIT point is usually at the bottom of the board, 2x2 in size.

## 🎵 Music and Sounds

Music and sound effects used in the game:

- **Sound Effects**: 8-bit themed, programmatically generated sounds
- **Background Music**: Retro-themed music tracks
- **Producer Information**: Music producers are credited in music file names

## 🌐 Website

Visit the project website:

🔗 **[https://ness246.github.io/Klo./](https://ness246.github.io/Klo./)**

The website is designed with retro 8-bit/16-bit theme and contains all project information.

## 🛠️ Technology

- **Python 3.7+**: Programming language
- **Pygame**: Game engine and graphics library
- **JSON**: Level and settings files
- **HTML/CSS/JS**: Website (GitHub Pages)

## 📝 Development

### Level Creation

Levels are stored in JSON format in the `levels/` folder. Example format:

```json
{
  "id": "A-01",
  "grid": {"cols": 4, "rows": 5},
  "blocks": [
    {"id": "T", "w": 2, "h": 2, "x": 1, "y": 0, "type": "target", "color": "T"},
    {"id": "L", "w": 1, "h": 2, "x": 0, "y": 0, "color": "red"}
  ],
  "par": 20,
  "exit": [1, 3],
  "difficulty": 2
}
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Added new feature'`)
4. Push your branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 🐛 Known Issues

There are currently no known major issues. If you find a bug, please report it via [GitHub Issues](https://github.com/ness246/Klo./issues).

## 📄 License

This project is licensed under the [MIT License](LICENSE). You can use, modify, and distribute it as you wish.

## 👨‍💻 Developer

**Ness246**

- GitHub: [@ness246](https://github.com/ness246)
- Project: [Klo. Repository](https://github.com/ness246/Klo.)

## 🙏 Acknowledgments

- Original creators of Klotski puzzle
- Pygame developers
- Retro gaming community
- Music producers (credited in music file names)

## 📞 Contact

You can use [GitHub Issues](https://github.com/ness246/Klo./issues) for questions, suggestions, or feedback.

---

</details>

---

<div align="center">

**⭐ If you like this project, don't forget to give it a star! ⭐**  
**⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın! ⭐**

Made with curiosity by Ness246

</div>
