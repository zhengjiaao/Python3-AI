from ultralytics import YOLO
import cv2

# 检测 bus.jpg 图像，包括(person、bicycle、car、motorcycle、bus)

# Load the pre-trained YOLOv8n model
# model = YOLO("yolov8n.pt")
model = YOLO("yolov8n.onnx")

# Image URL and output path for saving the annotated image
image_url = "https://ultralytics.com/images/bus.jpg"
output_path = "detected_bus.jpg"

# Perform prediction on the image URL
results = model(image_url)

# Visualize and save the results
for result in results:
    annotated_frame = result.plot()

    print(annotated_frame)

    # Display the annotated image
    cv2.imshow("Detected Objects", annotated_frame)
    cv2.waitKey(0)  # Wait for any key press to close the window

    # Save the annotated image to disk
    cv2.imwrite(output_path, annotated_frame)

cv2.destroyAllWindows()  # Close all OpenCV windows
