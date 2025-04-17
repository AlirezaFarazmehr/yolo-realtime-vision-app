import cv2
from tkinter import messagebox
from .utils import calculate_distance, save_results_to_csv

def detect_from_file(model, video_path, threshold=50):
    """
    Perform object detection on a video file using a trained YOLO model.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Cannot open video file!")
        return

    frame_number = 0
    total_objects = 0
    class_counts = {}
    results_data = []
    tracked_objects = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_number += 1
        results = model(frame, show=False)

        for result in results:
            boxes = result.boxes
            names = model.names
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = box.conf[0]
                cls = int(box.cls[0])
                label = names[cls]

                new_object = True
                for tracked in tracked_objects:
                    if calculate_distance((x1, y1, x2, y2), tracked['bbox']) < threshold:
                        new_object = False
                        break

                if new_object:
                    tracked_objects.append({'bbox': (x1, y1, x2, y2), 'frame': frame_number, 'label': label})
                    total_objects += 1
                    class_counts[label] = class_counts.get(label, 0) + 1
                    results_data.append([total_objects, label, f"{conf:.2f}", frame_number])

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("YOLOv8 Object Detection - Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    save_results_to_csv(total_objects, class_counts, results_data)

    summary = f"Total Objects Detected: {total_objects}\n\n"
    for cls, count in class_counts.items():
        summary += f"{cls}: {count}\n"
    messagebox.showinfo("Detection Summary", summary)
