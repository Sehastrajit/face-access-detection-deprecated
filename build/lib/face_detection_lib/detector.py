import torch
import cv2
import numpy as np
import pkg_resources
from ultralytics import YOLO

class FaceDetector:
    def __init__(self, model_path=None, labels=None, confidence_threshold=0.5):
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f"Using device: {self.device}")
        
        # Use embedded model if no path is provided
        if model_path is None:
            model_path = pkg_resources.resource_filename(__name__, 'models/best.pt')
        
        # Load the YOLOv8 model
        self.model = YOLO(model_path)
        
        # Set the threshold for prediction
        self.confidence_threshold = confidence_threshold
        
        # Define the label mapping
        self.labels = labels or {0: 'Safe', 1: 'Threat'}
    
    def process_frame(self, frame):
        # Perform object detection
        results = self.model(frame, device=self.device)
        processed_frame = frame.copy()
        
        # Process results
        for r in results:
            boxes = r.boxes

            for box in boxes:
                # Bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                
                # Confidence
                conf = box.conf[0]
                
                # Class name
                cls = int(box.cls[0])
                label = self.labels.get(cls, 'Unknown')

                if conf > self.confidence_threshold:
                    color = (0, 255, 0) if cls == 0 else (0, 0, 255)

                    # Draw bounding box
                    cv2.rectangle(processed_frame, (x1, y1), (x2, y2), color, 2)

                    # Display label
                    label_text = f'{label} ({conf:.2f})'
                    cv2.putText(processed_frame, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        
        return processed_frame

    def run_webcam(self):
        # Open a connection to the webcam
        cap = cv2.VideoCapture(0)
        
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                break

            # Process the frame
            processed_frame = self.process_frame(frame)

            # Display the resulting frame
            cv2.imshow('Detection', processed_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Release the webcam and close the window
        cap.release()
        cv2.destroyAllWindows()
