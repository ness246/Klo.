# Klo. - Android APK Build Kılavuzu

Bu klasör, Klo. oyununun Android APK'sını oluşturmak için gerekli dosyaları içerir.

## Gereksinimler

1. **Buildozer**: Android APK oluşturmak için gerekli
2. **Python 3**: Buildozer çalıştırmak için
3. **Android SDK & NDK**: Android geliştirme araçları
4. **Linux veya WSL/WSL2 (Windows için)**: Buildozer Linux gerektirir

## Kurulum

### 1. Buildozer Kurulumu

```bash
# Önce setuptools kurun (Python 3.12 için gerekli - distutils içerir)
pip install setuptools

# Sonra buildozer'ı kurun
pip install buildozer
```

### 2. Android SDK & NDK Kurulumu

Buildozer ilk çalıştırıldığında Android SDK ve NDK'yı otomatik indirir ve kurar.

### 3. Gerekli Dosyaları Kontrol Edin

- `logo.png` - Ana dizinde olmalı (icon olarak kullanılacak)
- `assets/` - Oyun varlıkları
- `levels/` - Oyun seviyeleri
- `main_android.py` - Android için optimize edilmiş ana dosya

## APK Oluşturma

### 1. Buildozer Config Düzenleme (İsteğe Bağlı)

`buildozer.spec` dosyasını gerektiğinde düzenleyin:

- `title`: Uygulama adı
- `package.name`: Paket adı
- `package.domain`: Paket domain'i
- `version`: Uygulama versiyonu
- `icon.filename`: Icon dosyası yolu
- `presplash.filename`: Açılış ekranı dosyası

### 2. İlk Build (Uzun Sürebilir)

```bash
cd android_build
buildozer android debug
```

İlk build oldukça uzun sürer (30-60 dakika) çünkü:
- Android SDK indirir
- Android NDK indirir
- Python for Android derler
- Pygame2 ve bağımlılıkları derler
- APK oluşturur

### 3. Sonraki Buildler (Daha Hızlı)

```bash
buildozer android debug
```

### 4. Release APK (İmzalı)

Release APK oluşturmak için:

```bash
buildozer android release
```

**Not**: Release APK için keystore gerekir. İlk kez buildozer bir keystore oluşturur.

## APK Konumu

APK dosyası şu konumda oluşturulur:

```
android_build/bin/klotski-<version>-<arch>.apk
```

## Mobil Optimizasyonlar

`main_android.py` dosyasında yapılan mobil optimizasyonlar:

1. **Dinamik Ekran Çözünürlüğü**: Android cihazların farklı ekran boyutlarına otomatik uyum
2. **Dokunmatik Kontroller**: Dokunmatik ekranlar için optimize edilmiş drag threshold ve hitbox padding
3. **Tam Ekran Modu**: Android'de otomatik tam ekran
4. **F11 Tuşu Kaldırıldı**: Android'de olmayan tuş referansları kaldırıldı
5. **Android Geri Butonu**: ESC tuşu Android geri butonuna eşlendi

## Sorun Giderme

### Buildozer bulunamıyor
```bash
pip install --upgrade buildozer
```

### Android SDK/NDK indirme sorunları
Buildozer config'de `android.sdk_path` ve `android.ndk_path` kullanarak manuel yollar belirleyebilirsiniz.

### Pygame import hatası
`requirements` listesinde `pygame2` kullanıldığından emin olun. Pygame2 Android için gerekli.

### ModuleNotFoundError: No module named 'distutils' (Python 3.12)
Python 3.12'de `distutils` modülü kaldırılmıştır. Çözüm:

```bash
# Virtual environment içinde
source venv/bin/activate
pip install setuptools
```

Alternatif olarak sistem paketi kurun (Ubuntu/Debian):
```bash
sudo apt install python3-distutils python3-setuptools
```

### Dosya bulunamadı hataları
`source.dir` değerinin doğru olduğundan emin olun. Varsayılan olarak `..` (üst dizin) kullanılır.

## Test

Oluşturulan APK'yı test etmek için:

1. **USB Debugging**: Android cihazda USB debugging'i açın
2. **ADB**: `adb install bin/klotski-*.apk` komutuyla kurulum yapın
3. Veya APK'yı cihaza aktarıp manuel olarak kurun

## Bilinen Sorunlar

- İlk build çok uzun sürer (normal)
- Bazı müzik dosyaları (.ogg) APK boyutunu artırabilir
- Tam ekran modu bazı cihazlarda sorun çıkarabilir (buildozer config'de `fullscreen = 0` yaparak test edin)

## Geliştirici Notları

- `main_android.py` dosyası `main.py`'den kopyalanmıştır ve Android için optimize edilmiştir
- Buildozer build sırasında `main_android.py`'yi `main.py` olarak kopyalar
- `assets` ve `levels` klasörleri otomatik olarak APK'ya dahil edilir

## İletişim

Sorularınız için: GitHub Issues veya README.md'deki iletişim bilgileri

