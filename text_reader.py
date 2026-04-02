import cv2
import requests
import numpy as np
import easyocr
import time

# Replace with your ESP32-CAM IP
ESP32_CAM_URL = "http://192.168.1.101/cam-hi.jpg"

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'], gpu=False)

def capture_image():
    """ Captures an image from the ESP32-CAM """
    try:
        start_time = time.time()
        response = requests.get(ESP32_CAM_URL, timeout=2)  # Reduced timeout for faster response
        if response.status_code == 200:
            img_arr = np.frombuffer(response.content, np.uint8)
            img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
            print(f"[INFO] Image received in {time.time() - start_time:.2f} seconds")
            return img
        else:
            print("[Error] Failed to get image from ESP32-CAM.")
            return None
    except Exception as e:
        print(f"[Error] {e}")
        return None

print("[INFO] Starting text recognition...")

while True:
    frame = capture_image()
    if frame is None:
        continue  # Skip this iteration if the image wasn't retrieved

    # Resize image for faster processing
    frame_resized = cv2.resize(frame, (400, 300))

    # Convert to grayscale (better OCR accuracy)
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

    # Process image with EasyOCR
    start_time = time.time()
    results = reader.readtext(gray, detail=0, paragraph=True)
    print(f"[INFO] OCR processed in {time.time() - start_time:.2f} seconds")

    if results:
        detected_text = " ".join(results)
        print(f"[INFO] Recognized Text: {detected_text}")

    # Display the image feed
    cv2.imshow("ESP32-CAM Feed", frame_resized)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cv2.destroyAllWindows()
