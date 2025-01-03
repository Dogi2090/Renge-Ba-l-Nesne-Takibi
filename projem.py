import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

# Renkli nesnenin merkezlerini saklamak için bir liste
positions = []

# Kamera başlat
cap = cv2.VideoCapture(0)

# Zaman bilgisi için başlangıç zamanı
start_time = time.time()

print("Nesne takibini durdurmak için 'q' tuşuna basın.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Kamera akışı alınamadı!")
        break

    # Görüntüyü HSV renk uzayına çevir
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Yeşil renk aralığını tanımla
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])
    mask = cv2.inRange(hsv_frame, lower_green, upper_green)

    # Maske üzerinde kontur bulma
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Minimum boyut filtresi
            # Konturun etrafına bir dikdörtgen çiz
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Nesnenin merkezi
            cx = x + w // 2
            cy = y + h // 2
            positions.append((cx, cy))

            # Merkeze bir daire çiz
            cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)

            # Merkez koordinatlarını ekrana yazdır
            cv2.putText(frame, f"({cx}, {cy})", (cx + 10, cy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Görüntüyü göster
    cv2.imshow("Renk Takibi", frame)

    # Çıkış için 'q' tuşuna bas
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Nesne hareketini görselleştirme
if positions:
    positions = np.array(positions)
    plt.plot(positions[:, 0], positions[:, 1], marker='o', linestyle='-', color='r')
    plt.title("Nesnenin Hareket Yolu")
    plt.xlabel("X Koordinatı")
    plt.ylabel("Y Koordinatı")
    plt.show()
else:
    print("Takip edilen nesne bulunamadı.")
