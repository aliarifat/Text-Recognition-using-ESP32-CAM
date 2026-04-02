# 📷 Text Recognition using ESP32-CAM

## 📖 Overview

**ESP32-CAM OCR: Real-Time Text Recognition from Video Feed**

Recognize and extract text in real time from an ESP32-CAM video feed using Python, OpenCV, and EasyOCR.

This project demonstrates how to build a lightweight OCR pipeline where an ESP32-CAM streams images over Wi-Fi, and a Python client processes those images to detect and display text.

---

## 🚀 Features

- 📡 Live image streaming from ESP32-CAM over HTTP  
- 🔍 Real-time Optical Character Recognition (OCR)  
- ⚡ Fast image processing using OpenCV  
- 🧠 Text extraction powered by EasyOCR  
- 🖥️ Live camera preview with detected text output  

---

## 🧠 Use Cases

- 🚗 Self-driving systems (road sign detection)  
- 🧾 Automated document reading  
- 🔞 Content moderation (text in images)  
- 💊 Smart healthcare assistants (medicine labels)  
- 📱 Social media image text analysis  

---

## 🧩 System Architecture

### 🔹 Overview
ESP32-CAM → WiFi HTTP Server → Python Client → OpenCV Processing → EasyOCR → Text Output

### 🔹 Components

#### ESP32-CAM
- Captures images (800x600 resolution)  
- Hosts HTTP server (`/cam-hi.jpg`)  
- Streams JPEG images over Wi-Fi  

#### Python Client
- Fetches images via HTTP  
- Processes images using OpenCV  
- Extracts text using EasyOCR  
- Displays video + recognized text  

---

## 🔄 Workflow

### 1. ESP32-CAM Setup
- Connects to Wi-Fi  
- Starts web server  
- Serves images at:
  http://<ESP32_IP>/cam-hi.jpg
  
### 2. Image Processing (Python)
- Fetch image via HTTP request  
- Decode into OpenCV format  
- Resize to `400x300`  
- Convert to grayscale  

### 3. OCR Processing
- EasyOCR detects text  
- Extracted text printed to terminal  

### 4. User Interaction
- Live video preview  
- Press `q` to exit  

---

## 🧰 Hardware Requirements

| Component | Quantity |
|----------|--------|
| ESP32-CAM Module | 1 |
| FTDI USB-to-Serial (3.3V/5V) | 1 |
| Jumper Wires | ~5 |
| Micro USB Cable | 1 |

---

## 🔌 Circuit Connections

| ESP32-CAM | FTDI |
|----------|------|
| VCC | 5V |
| GND | GND |
| U0R | TX |
| U0T | RX |
| IO0 | GND (for flashing) |

> ⚠️ After uploading code, disconnect IO0 from GND and reset the board.

---

## 💻 Code Files

- `esp32_cam_basic.ino` → ESP32-CAM firmware  
- `text_reader.py` → Python OCR script  

---

## ⚙️ Setup Instructions

### 1. ESP32-CAM

- Install ESP32 board in Arduino IDE  
- Upload the code  
- Open Serial Monitor  
- Copy the IP address  

---

### 2. Python Environment

#### Create virtual environment

```bash
python -m venv ocr_env
source ocr_env/bin/activate  # Linux/Mac
ocr_env\Scripts\activate     # Windows
Install dependencies
pip install opencv-python numpy easyocr requests
3. Run the Project
Update IP in script
ESP32_CAM_URL = "http://<YOUR_IP>/cam-hi.jpg"
Run
python main.py
📸 Demo
Place the camera in front of text
Watch real-time detection in terminal
View live feed in OpenCV window
```
<img width="590" height="487" alt="Screenshot 2025-03-19 201037" src="https://github.com/user-attachments/assets/1826f43b-aecf-4fdb-8d9f-2426b898df6a" />
<img width="594" height="493" alt="Screenshot 2025-03-19 200838" src="https://github.com/user-attachments/assets/bf006fc1-f3de-4544-b773-4b0ddf124e2e" />
<img width="630" height="74" alt="Screenshot 2025-03-19 193907" src="https://github.com/user-attachments/assets/8733aed0-c626-4983-8fd5-536637d1d88d" />
<img width="563" height="242" alt="Screenshot 2025-03-19 193807" src="https://github.com/user-attachments/assets/a596beec-b8bb-4136-a1b0-94d7ca5e70d3" />



