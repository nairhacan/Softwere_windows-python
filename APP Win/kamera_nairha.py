import cv2

# Buka kamera (0 = kamera utama)
kamera = cv2.VideoCapture(0)

while True:
    berhasil, frame = kamera.read()
    if not berhasil:
        break

    cv2.imshow("Kamera Nairha", frame)

    # Tekan tombol 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
