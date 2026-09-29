# ============================================
# PROJECT PHOTOBOOTH - PERTEMUAN 9
# Persiapan & Eksplorasi Kamera
# ============================================

import cv2
import numpy as np
from PIL import Image
from datetime import datetime

# ============================================
# BAGIAN 1: CEK VERSI & SETUP
# ============================================

print("=" * 50)
print("PROJECT PHOTOBOOTH - PERTEMUAN 9")
print("=" * 50)
print(f"Versi OpenCV: {cv2.__version__}")
print(f"Versi NumPy: {np.__version__}")
print("=" * 50)

# ============================================
# BAGIAN 2: BUKA KAMERA
# ============================================

cap = cv2.VideoCapture(0)

# Cek apakah kamera berhasil dibuka
if not cap.isOpened():
    print("❌ Kamera TIDAK terdeteksi!")
    print("   Coba ganti cv2.VideoCapture(0) jadi (1) atau (2)")
    exit()
else:
    print("✅ Kamera berhasil dibuka!")

# Set resolusi kamera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# ============================================
# BAGIAN 3: TAMPILKAN VIDEO FEED
# ============================================

print("\n📸 Tekan 'c' untuk CAPTURE foto")
print("❌ Tekan 'q' untuk KELUAR\n")

foto_counter = 0  # Hitung berapa foto yang diambil

while True:
    # Baca frame dari kamera
    ret, frame = cap.read()
    
    if not ret:
        print("❌ Gagal membaca frame dari kamera")
        break
    
    # Tampilkan video feed
    cv2.imshow("Photobooth - Pertemuan 9", frame)
    
    # Baca tombol yang ditekan
    key = cv2.waitKey(1) & 0xFF
    
    # Tombol 'c' untuk capture
    if key == ord('c'):
        foto_counter += 1
        nama_file = f"foto_{foto_counter}_{datetime.now().strftime('%H%M%S')}.jpg"
        cv2.imwrite(nama_file, frame)
        print(f"✅ Foto tersimpan: {nama_file}")
    
    # Tombol 'q' untuk keluar
    elif key == ord('q'):
        print("\n👋 Keluar dari program...")
        break

# ============================================
# BAGIAN 4: CLEANUP
# ============================================

cap.release()
cv2.destroyAllWindows()
print(f"\nTotal foto yang diambil: {foto_counter}")
print("Program selesai!")