import csv
import math

def save_results_to_csv(total_objects, class_counts, results_data, output_file="detection_results.csv"):
    """
    Save detection results and summary to a CSV file.
    """
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Total Objects Detected", total_objects])
        writer.writerow([])
        writer.writerow(["Class", "Count"])
        for cls, count in class_counts.items():
            writer.writerow([cls, count])
        writer.writerow([])
        writer.writerow(["ID", "Class", "Confidence", "Frame Number"])
        writer.writerows(results_data)

def calculate_distance(box1, box2):
    """
    Calculate Euclidean distance between the centers of two bounding boxes.
    """
    x1_center = (box1[0] + box1[2]) / 2
    y1_center = (box1[1] + box1[3]) / 2
    x2_center = (box2[0] + box2[2]) / 2
    y2_center = (box2[1] + box2[3]) / 2
    return math.sqrt((x2_center - x1_center)**2 + (y2_center - y1_center)**2)
