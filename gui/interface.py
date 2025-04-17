import tkinter as tk
from tkinter import filedialog
from detection.video_detection import detect_from_file
from detection.webcam_detection import use_webcam
from detection.model_loader import load_model

def start_gui():
    """
    Launch the main GUI interface for selecting detection mode.
    """
    model = load_model()

    root = tk.Tk()
    root.title("Object Detection")
    root.geometry("300x150")

    label = tk.Label(root, text="Select an option for object detection:")
    label.pack(pady=10)

    btn_file = tk.Button(root, text="Open Video File", command=lambda: detect_from_file(model, filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov")]), threshold=50))
    btn_file.pack(pady=5)

    btn_webcam = tk.Button(root, text="Use Webcam", command=lambda: use_webcam(model))
    btn_webcam.pack(pady=5)

    btn_exit = tk.Button(root, text="Exit", command=root.quit)
    btn_exit.pack(pady=10)

    root.mainloop()
