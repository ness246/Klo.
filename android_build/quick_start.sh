#!/bin/bash
# Hızlı Başlangıç Scripti - Linux/WSL için

echo "=================================="
echo "Klo. Android APK Builder"
echo "=================================="
echo ""

# Buildozer kontrolü
if ! command -v buildozer &> /dev/null; then
    echo "❌ Buildozer bulunamadı!"
    echo "Kurulum: pip install buildozer"
    exit 1
fi

echo "✅ Buildozer bulundu"
echo ""

# Build başlat
echo "🚀 APK oluşturuluyor..."
echo "⏳ İlk build 30-60 dakika sürebilir..."
echo ""

buildozer android debug

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ APK başarıyla oluşturuldu!"
    echo "📦 Dosya konumu:"
    echo "   android_build/bin/"
    ls -lh bin/*.apk 2>/dev/null || echo "   (Dosyalar listeleniyor...)"
else
    echo ""
    echo "❌ APK oluşturulurken hata oluştu!"
    echo "📋 Log dosyalarına bakın:"
    echo "   .buildozer/android/platform/build/dists/klotski/logs/"
fi

