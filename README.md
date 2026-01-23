# HandWritten Digit Recognition

**A Python-based project that recognizes handwritten digits (0–9) using machine learning / deep learning techniques. This project includes training a model on the MNIST dataset and building a simple app to make predictions.**

Built as a submission for **Turing's Playground WOC 9**

Github Repository → [https://github.com/anshulk02101/-Driver-Drowsiness-Detection-System-with-SOS-Alert](https://github.com/anshulk02101/-Driver-Drowsiness-Detection-System-with-SOS-Alert)

## 📖 Table of Contents
- [✨ Key Features](#-key-features)
- [📊 Dataset](#-dataset)
- [📸 Screenshotst](#-screenshots)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 How to Run locally](#-how-to-run-locally)
- [🔮 Future Plans](#-future-plans)
- [🙏 Acknowledgments](#-acknowledgments)

## ✨ Key Features

- Real-time **drowsiness, blink rate & yawning** detection using Teachable Machine + TensorFlow.js
- Modern **cyberpunk/neon dark mode** interface
- **Journey Safety Report** — session stats, blink/yawn metrics, longest drowsy period, SOS status
- **Gemini AI Safety Analysis** — intelligent summary of the driving session
- **Quick Rest Finder** — finds nearby rest stops, coffee spots, quiet parks & hotels (~15 km radius)
- Live **geolocation** tracking + Google Maps integration
- **SOS emergency email** alert system
- Start/Stop monitoring with clean status feedback

## 📊 Dataset
The system is trained on a robust dataset tailored for driver monitoring:

* **Drowsiness Model Dataset:** https://www.kaggle.com/datasets/ismailnasri20/driver-drowsiness-dataset-ddd
* **Phone Detection Dataset:** https://universe.roboflow.com/driver-behavior-and-state-detection/driver-bfepd


## 📸 Screenshots

### 1. Initialize Page
Main entry point with dramatic "NEURAL SAFETY ACTIVATED" visual

![landing_page](https://github.com/anshulk02101/-Driver-Drowsiness-Detection-System-with-SOS-Alert/blob/main/screenshots/Initialize.png)

### 2. Active Monitoring + Journey Safety Report
Detailed statistics dashboard — session duration, blinks/min, yawns, drowsy periods, SOS status, Gemini AI section

![Monitoring](https://github.com/anshulk02101/-Driver-Drowsiness-Detection-System-with-SOS-Alert/blob/main/screenshots/Monitoring.png)

![Report](https://github.com/anshulk02101/-Driver-Drowsiness-Detection-System-with-SOS-Alert/blob/main/screenshots/Report.png)

### 3. Core Capabilities Overview
Futuristic showcase of the system's main features: real-time ocular tracking, visual capture, multi-modal alerts, live GPS geolocation, and manual SOS activation.

![core_capabilities](https://github.com/anshulk02101/-Driver-Drowsiness-Detection-System-with-SOS-Alert/blob/main/screenshots/Core_capabilities.png)

### 4. Neural Technology Stack Overview
Futuristic showcase of the tech stack used in the project

![tech-stack](https://github.com/anshulk02101/-Driver-Drowsiness-Detection-System-with-SOS-Alert/blob/main/screenshots/Tech_stack.png)

### 5. Quick Rest Finder
Beautiful neon buttons to locate nearby safe rest locations via GPS

![rest_Stop](https://github.com/anshulk02101/-Driver-Drowsiness-Detection-System-with-SOS-Alert/blob/main/screenshots/Rest_stop.png)

### 6. Phone!
Phone detection model — Monitors Driver on using phone during driving

![Phone!](https://github.com/anshulk02101/-Driver-Drowsiness-Detection-System-with-SOS-Alert/blob/main/screenshots/Phone!.png)

## 🛠️ Tech Stack

- **Frontend**          → HTML5, CSS3 (neon/cyberpunk style), JavaScript
- **Machine Learning**  → Google Teachable Machine → TensorFlow.js
- **Camera Access**     → WebRTC (getUserMedia)
- **Email**     → Emailjs
- **Geolocation**       → Browser Geolocation API + Google Maps links
- **AI Analysis**       → Google Gemini API integration (for safety report summary)

## 🚀 How to Run Locally

```bash
# Clone the project
git clone https://github.com/anshulk02101/-Driver-Drowsiness-Detection-System-with-SOS-Alert.git

# Enter directory
cd Driver-Drowsiness-Detection-System-with-SOS-Alert

# Open with VS Code Live Server (recommended)
# OR simply double-click index.html (but some features need http://localhost)
```

## ⚠️ Important Notes

- Allow **camera** and **location** access when prompted by the browser
- Best experience on **Google Chrome** (desktop version recommended)
- Some advanced features may require additional setup:
  - **Gemini AI** analysis → needs Google Gemini API key
  - **SOS emergency email** → requires email service configuration/API key

## 🔮 Future Plans

- Integrate real **SMS / WhatsApp** emergency alerts (using third-party APIs)
- Improve **mobile responsiveness** and touch support
- Train a more accurate drowsiness detection model 
- Implement **session history** storage (localStorage or cloud-based)
- Add **Dark / Light** theme toggle
- Performance optimization for low-end devices
- Add **multi-language support**

## 🙏 Acknowledgments

Special thanks to:

- [Google Teachable Machine](https://teachablemachine.withgoogle.com/)  
- [Emailjs](https://www.emailjs.com/)
- Google **Gemini** (for intelligent safety analysis)  
- **Google TechSprint 2025-26** organizers and team  
- All individuals, researchers, and communities worldwide working on road safety & driver assistance technologies

Your work inspires projects like this 💙
