# ============================================
# PROJECT PHOTOBOOTH - PERTEMUAN 9
# Persiapan & Eksplorasi Kamera
# ============================================

import cv2
from datetime import datetime

# Buka kamera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Kamera tidak terdeteksi!")
    exit()

# Set resolusi
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("📸 Tekan 'c' untuk CAPTURE")
print("❌ Tekan 'q' untuk KELUAR\n")

# Loop video feed
while True:
    ret, frame = cap.read()
    
    cv2.imshow("Photobooth", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    # Capture foto
    if key == ord('c'):
        nama_file = f"foto_{datetime.now().strftime('%H%M%S')}.jpg"
        cv2.imwrite(nama_file, frame)
        print(f"✅ Tersimpan: {nama_file}")
    
    # Keluar
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Program selesai!")