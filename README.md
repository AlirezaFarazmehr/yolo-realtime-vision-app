# 🎯 Real-Time Object Detection with YOLO in Python 🚀

Welcome to a complete end-to-end object detection project using **YOLOv11**! 🧠  
Detect objects in **real-time** from your **webcam** 🎥 or **video files** 🎞️ using a **custom-trained model**.  
Includes a user-friendly **Python GUI** with live preview and CSV result export. 📊

---

## 🌟 Features

✅ Real-time object detection (video or webcam)  
✅ Custom-trained YOLOv11 model with Roboflow 📦  
✅ Easy-to-use GUI with `Tkinter` 🖱️  
✅ Object tracking to avoid duplicates 🧩  
✅ CSV report generation 📑  
✅ Built with modular Python scripts 🐍

---

## 🧠 Model Details

The detection model was trained on a **custom dataset** including classes like:

- 👤 Person  
- 📱 Mobile  
- 🪑 Chair  
- 🧾 Desk  
- 🪟 Table  

Training was done via [Roboflow](https://roboflow.com) and integrated in **Google Colab** using their API key.  
The final trained model is saved as `best.pt`.

---

## 📁 Project Structure

```
yolo_app/
├── main.py                  # Main app launcher
├── requirements.txt         # Required Python packages
├── best.pt                  # Trained YOLOv11 model weights 🧠
├── detection/
│   ├── model_loader.py      # Load YOLO model
│   ├── video_detection.py   # Detect from video
│   ├── webcam_detection.py  # Detect from webcam
│   ├── utils.py             # Helper functions
└── gui/
    └── interface.py         # GUI with Tkinter
```

---

## ▶️ How to Run

```bash
# 1️⃣ Clone this repository
git clone https://github.com/yourusername/yolo-real-time-detection
cd yolo-real-time-detection

# 2️⃣ Install requirements
pip install -r requirements.txt

# 3️⃣ Put your best.pt YOLO model in root folder

# 4️⃣ Launch the app
python main.py
```

---

## 📦 Requirements

- Python 3.8+
- ultralytics 🔥
- opencv-python 📷
- pandas 📊
- tkinter (built-in)

Install with:

```bash
pip install ultralytics opencv-python pandas
```

---

## 📜 License

This project is licensed under the **MIT License** 🧾  
See [LICENSE](LICENSE) file for more information.

---

## 👨‍💻 Author

Developed by **[Alireza Farazmehr]**  
For educational purposes 🧪 — feel free to use, modify, and contribute! 🤝

---

## 🏷️ Tags

`#YOLOv11` `#Python` `#ObjectDetection` `#ComputerVision` `#Tkinter` `#RealTime`
