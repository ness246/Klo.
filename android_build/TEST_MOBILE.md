# main_android.py Test ve APK Oluşturma Rehberi

## 📱 main_android.py'yi Test Etme

### Yöntem 1: Masaüstünde Test (Önerilen)

`main_android.py` dosyası hem Android hem de masaüstünde çalışacak şekilde tasarlanmıştır.

```bash
cd android_build
python main_android.py
```

**Not**: Android modunda olmadığı için normal pencere modunda açılacak ve test edebilirsiniz.

### Yöntem 2: Android Emulator ile Test

1. **Android Studio'yu kurun** ve bir Android emulator oluşturun
2. **PyGame2 Android APK Build** sistemi kullanarak test APK oluşturun
3. Emulator'a APK'yı yükleyin

## 🔨 APK Oluşturma

### Gereksinimler

- **Linux** (veya Windows için **WSL2**)
- **Python 3.8+**
- **Buildozer**

### Adım 1: Buildozer Kurulumu

```bash
pip install buildozer
```

### Adım 2: İlk Build (UZUN SÜREBİLİR - 30-60 dakika)

```bash
cd android_build
buildozer android debug
```

**İlk build sırasında:**
- Android SDK indirilir (~1GB)
- Android NDK indirilir (~1GB)
- Python-for-Android derlenir
- Pygame2 ve bağımlılıkları derlenir
- APK oluşturulur

### Adım 3: APK Dosyasını Bulma

APK dosyası şu konumda oluşur:

```
android_build/bin/klotski-1.0-<arch>.apk
```

Örnek:
- `android_build/bin/klotski-1.0-arm64-v8a.apk`
- `android_build/bin/klotski-1.0-armeabi-v7a.apk`

### Adım 4: APK'yı Android Cihaza Yükleme

#### Seçenek A: USB ile (ADB)
```bash
adb install android_build/bin/klotski-1.0-*.apk
```

#### Seçenek B: Manuel
1. APK dosyasını Android cihaza kopyalayın (USB, Bluetooth, vs.)
2. Android cihazda "Bilinmeyen kaynaklardan uygulama yükleme" iznini verin
3. APK dosyasına dokunarak yükleyin

## 🐛 Sorun Giderme

### Buildozer bulunamıyor
```bash
pip install --upgrade buildozer
```

### Android SDK/NDK indirme sorunları
Buildozer config dosyasında (`buildozer.spec`) manuel yollar belirleyebilirsiniz:
```ini
android.sdk_path = /path/to/android/sdk
android.ndk_path = /path/to/android/ndk
```

### Pygame import hatası
`buildozer.spec` dosyasında `requirements` listesinde `pygame2` olduğundan emin olun.

### Windows'ta Buildozer
Windows'ta doğrudan çalışmaz! WSL2 kullanın:
1. Windows'ta WSL2 kurun
2. WSL2 içinde Linux kurun (Ubuntu önerilir)
3. WSL2 içinde buildozer kurun ve çalıştırın

## 📝 Önemli Notlar

1. **İlk build çok uzun sürer** - Normal, sabırlı olun
2. **İnternet bağlantısı gerekli** - İlk build sırasında çok veri indirilir
3. **Disk alanı** - En az 5GB boş alan gereklidir
4. **main_android.py** dosyası build sırasında otomatik olarak `main.py` olarak kopyalanır

## 🔍 Buildozer Config Düzenleme

`buildozer.spec` dosyasında değiştirebileceğiniz önemli ayarlar:

```ini
# Uygulama adı
title = Klo.

# Paket adı
package.name = klotski

# Versiyon
version = 1.0

# Icon
icon.filename = %(source.dir)s/logo.png

# Tam ekran (Android'de)
fullscreen = 1

# Yönlendirme (portrait/landscape/all)
orientation = portrait
```

## 📦 Release APK (İmzalı)

Release APK oluşturmak için:

```bash
buildozer android release
```

İlk kez bir keystore oluşturmanız istenir. Şifre unutmayın!

## 🎮 Mobil Optimizasyonlar

`main_android.py` dosyasında yapılan optimizasyonlar:

- ✅ Dinamik ekran çözünürlüğü
- ✅ Dokunmatik kontroller (daha yüksek threshold)
- ✅ Tam ekran modu
- ✅ Android geri butonu desteği
- ✅ F11 tuşu kaldırıldı (Android'de yok)

## ❓ Daha Fazla Yardım

- `README_ANDROID.md` dosyasına bakın
- Buildozer dokümantasyonu: https://buildozer.readthedocs.io/
- Python-for-Android: https://python-for-android.readthedocs.io/

