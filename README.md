# Text-Recognition-using-ESP32-CAM
📷 ESP32-CAM OCR: Real-Time Text Recognition from Video Feed

Recognize and extract text in real time from an ESP32-CAM video feed using Python, OpenCV, and EasyOCR.

This project demonstrates how to build a lightweight OCR pipeline where an ESP32-CAM streams images over Wi-Fi, and a Python client processes those images to detect and display text.

🚀 Features
📡 Live image streaming from ESP32-CAM over HTTP
🔍 Real-time Optical Character Recognition (OCR)
⚡ Fast image processing using OpenCV
🧠 Text extraction powered by EasyOCR
🖥️ Live camera preview with detected text output
🧠 Use Cases
🚗 Self-driving systems (road sign detection)
🧾 Automated document reading
🔞 Content moderation (text in images)
💊 Smart healthcare assistants (medicine labels)
📱 Social media image text analysis
🧩 System Architecture
Overview
ESP32-CAM  →  WiFi HTTP Server  →  Python Client  →  OpenCV Processing  →  EasyOCR  →  Text Output
Components
🔹 ESP32-CAM
Captures images (800x600 resolution)
Hosts HTTP server (/cam-hi.jpg)
Streams JPEG images over Wi-Fi
🔹 Python Client
Fetches images via HTTP
Processes images using OpenCV
Extracts text using EasyOCR
Displays video + recognized text
🔄 Workflow
1. ESP32-CAM Setup
Connects to Wi-Fi
Starts web server
Serves images at:
http://<ESP32_IP>/cam-hi.jpg
2. Image Processing (Python)
Fetch image via HTTP request
Decode into OpenCV format
Resize to 400x300
Convert to grayscale
3. OCR Processing
EasyOCR detects text
Extracted text printed to terminal
4. User Interaction
Live video preview
Press q to exit
🧰 Hardware Requirements
Component	Quantity
ESP32-CAM Module	1
FTDI USB-to-Serial (3.3V/5V)	1
Jumper Wires	~5
Micro USB Cable	1
🔌 Circuit Connections
ESP32-CAM	FTDI
VCC	5V
GND	GND
U0R	TX
U0T	RX
IO0	GND (for flashing)

⚠️ After uploading code, disconnect IO0 from GND and reset the board.

💻 ESP32-CAM Code
#include <WebServer.h>
#include <WiFi.h>
#include <esp32cam.h>

const char* WIFI_SSID = "SSID";
const char* WIFI_PASS = "password";

WebServer server(80);

static auto hiRes = esp32cam::Resolution::find(800, 600);

void serveJpg() {
  auto frame = esp32cam::capture();
  if (!frame) {
    server.send(503, "", "");
    return;
  }

  server.setContentLength(frame->size());
  server.send(200, "image/jpeg");

  WiFiClient client = server.client();
  frame->writeTo(client);
}

void handleJpgHi() {
  esp32cam::Camera.changeResolution(hiRes);
  serveJpg();
}

void setup() {
  Serial.begin(115200);

  esp32cam::Config cfg;
  cfg.setPins(esp32cam::pins::AiThinker);
  cfg.setResolution(hiRes);
  cfg.setBufferCount(2);
  cfg.setJpeg(80);

  esp32cam::Camera.begin(cfg);

  WiFi.begin(WIFI_SSID, WIFI_PASS);
  while (WiFi.status() != WL_CONNECTED) delay(500);

  Serial.println(WiFi.localIP());

  server.on("/cam-hi.jpg", handleJpgHi);
  server.begin();
}

void loop() {
  server.handleClient();
}
🐍 Python Code
import cv2
import requests
import numpy as np
import easyocr
import time

ESP32_CAM_URL = "http://<ESP32_IP>/cam-hi.jpg"

reader = easyocr.Reader(['en'], gpu=False)

def capture_image():
    try:
        response = requests.get(ESP32_CAM_URL, timeout=2)
        if response.status_code == 200:
            img_arr = np.frombuffer(response.content, np.uint8)
            return cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    except:
        return None

while True:
    frame = capture_image()
    if frame is None:
        continue

    frame = cv2.resize(frame, (400, 300))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    results = reader.readtext(gray, detail=0, paragraph=True)

    if results:
        print("Detected:", " ".join(results))

    cv2.imshow("ESP32 Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
⚙️ Setup Instructions
1. ESP32-CAM
Install ESP32 board in Arduino IDE
Upload code
Open Serial Monitor
Copy IP address
2. Python Environment
Create virtual environment
python -m venv ocr_env
source ocr_env/bin/activate  # Linux/Mac
ocr_env\Scripts\activate     # Windows
Install dependencies
pip install opencv-python numpy easyocr requests
3. Run the Project
Update:
ESP32_CAM_URL = "http://<YOUR_IP>/cam-hi.jpg"
Run:
python main.py
📸 Demo
Place camera in front of text
Watch real-time detection in terminal
View live feed in OpenCV window
⚡ Performance Tips
Use good lighting for better OCR accuracy
Adjust resolution for speed vs quality
Enable GPU in EasyOCR if available
Apply filters (thresholding, sharpening)
🔧 Possible Improvements
📊 Save detected text to database
🌐 Build web dashboard
🧾 Multi-language OCR
📱 Mobile app integration
🎯 Bounding boxes on detected text
🤝 Contributing

Pull requests are welcome! Feel free to improve performance, UI, or add features.

📜 License

This project is open-source under the MIT License.

🙌 Acknowledgements
ESP32-CAM community
OpenCV
EasyOCR
