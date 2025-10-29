# 🚀 APK Oluşturma - Basit Rehber

## ⚡ Hızlı Başlangıç

### Windows'ta:

**WSL2 Gereklidir!** Buildozer sadece Linux'ta çalışır.

1. **WSL2 Kurulumu:**
   ```powershell
   wsl --install
   ```

2. **WSL2'de Linux'a girin:**
   ```bash
   wsl
   ```

3. **Projeye gidin:**
   ```bash
   cd /mnt/d/Enes/klotski_pygame/klotski_pygame_styled/android_build
   ```

4. **Buildozer Kur:**
   ```bash
   # Önce setuptools kurun (Python 3.12 için gerekli)
   pip install setuptools
   # Sonra buildozer
   pip install buildozer
   ```

5. **APK Oluştur:**
   ```bash
   buildozer android debug
   ```

### Linux'ta:

1. **Buildozer Kur:**
   ```bash
   # Önce setuptools kurun (Python 3.12 için gerekli)
   pip install setuptools
   # Sonra buildozer
   pip install buildozer
   ```

2. **APK Oluştur:**
   ```bash
   cd android_build
   buildozer android debug
   ```

## 📱 main_android.py Test

Masaüstünde test etmek için:

```bash
cd android_build
python main_android.py
```

Android modunda değil, normal pencere açılacak ve test edebilirsiniz.

## 📦 APK Dosyası

APK şurada oluşur:
```
android_build/bin/klotski-1.0-*.apk
```

## ⚠️ Önemli

- İlk build **30-60 dakika** sürebilir
- İnternet bağlantısı gerekli (~2GB indirme)
- En az **5GB** boş disk alanı gereklidir

## 🔧 Sorun Giderme

### Python 3.12: "No module named 'distutils'"
```bash
pip install setuptools
```

Detaylı bilgi için: `TEST_MOBILE.md` ve `README_ANDROID.md`

