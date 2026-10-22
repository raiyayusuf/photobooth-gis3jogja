import cv2
import numpy as np
from PIL import Image

def potong_tengah(img, target_w, target_h):
    h, w = img.shape[:2]
    if (w/h) > (target_w/target_h):
        nw = int(h * (target_w/target_h))
        img = img[:, (w-nw)//2 : (w+nw)//2]
    else:
        nh = int(w / (target_w/target_h))
        img = img[(h-nh)//2 : (h+nh)//2, :]
    return cv2.resize(img, (target_w, target_h))

try:
    frame_pil = Image.open("frame_template.png").convert("RGBA")
    FW, FH = frame_pil.size
except:
    print("frame_template.png tidak ada!")
    exit()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

KW, KH = 500, 250
f1, f2, f3 = None, None, None
nomor_foto = 1 

cv2.namedWindow("Photobooth", cv2.WINDOW_AUTOSIZE)
cv2.moveWindow("Photobooth", 100, -10)

print("SPASI = Jepret | Q = Keluar\n")

while True:
    ret, frame = cap.read()
    if not ret: break

    frame = cv2.flip(frame, 1)
    frame = potong_tengah(frame, KW, KH)
    live = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    kanvas = Image.new("RGBA", (FW, FH), (0, 0, 0, 255))

    if f1 is None: 
        kanvas.paste(live, (50, 50))
    else:
        kanvas.paste(f1, (50, 50))
        if f2 is None: 
            kanvas.paste(live, (50, 325))
        else:
            kanvas.paste(f2, (50, 325))
            if f3 is None: 
                kanvas.paste(live, (50, 600))
            else: 
                kanvas.paste(f3, (50, 600))

    hasil = Image.alpha_composite(kanvas, frame_pil)
    cv2.imshow("Photobooth", cv2.cvtColor(np.array(hasil), cv2.COLOR_RGBA2BGR))

    key = cv2.waitKey(1) & 0xFF

    if key == 32:
        if f1 and f2 and f3: continue

        for i in range(3, 0, -1):
            ret, bg = cap.read()
            bg = cv2.flip(bg, 1)
            bg = potong_tengah(bg, KW, KH)
            
            cv2.putText(bg, str(i), (220, 160), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), 8)
            cd_pil = Image.fromarray(cv2.cvtColor(bg, cv2.COLOR_BGR2RGB))
            
            k_cd = Image.new("RGBA", (FW, FH), (0, 0, 0, 255))
            if f1 is None: 
                k_cd.paste(cd_pil, (50, 50))
            elif f2 is None: 
                k_cd.paste(cd_pil, (50, 325))
            else: 
                k_cd.paste(cd_pil, (50, 600))
            
            if f1: k_cd.paste(f1, (50, 50))
            if f2: k_cd.paste(f2, (50, 325))
            
            hasil_cd = Image.alpha_composite(k_cd, frame_pil)
            cv2.imshow("Photobooth", cv2.cvtColor(np.array(hasil_cd), cv2.COLOR_RGBA2BGR))
            cv2.waitKey(1000)

        ret, jepret = cap.read()
        jepret = cv2.flip(jepret, 1)
        jepret = potong_tengah(jepret, KW, KH)
        baru = Image.fromarray(cv2.cvtColor(jepret, cv2.COLOR_BGR2RGB))

        if f1 is None: 
            f1 = baru
        elif f2 is None: 
            f2 = baru
        elif f3 is None:
            f3 = baru
            
            k_final = Image.new("RGBA", (FW, FH), (0, 0, 0, 255))
            k_final.paste(f1, (50, 50))
            k_final.paste(f2, (50, 325))
            k_final.paste(f3, (50, 600))
            akhir = Image.alpha_composite(k_final, frame_pil)
            
            nama_file = f"hasil_photobooth{nomor_foto}.jpg"
            akhir.convert("RGB").save(nama_file)
            print(f"Tersimpan: {nama_file}")
            
            cv2.imshow("Hasil", cv2.cvtColor(np.array(akhir), cv2.COLOR_RGBA2BGR))
            cv2.moveWindow("Hasil", 650, 0)
            
            nomor_foto += 1
            f1, f2, f3 = None, None, None

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()