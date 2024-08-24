
# Face Detection Library

![working](https://img.shields.io/badge/status-working-brightgreen)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![PyPI Version](https://img.shields.io/pypi/v/face_detection_lib)

A Python library for face detection using YOLOv8. This library enables real-time face detection via webcam, leveraging the YOLOv8 model for high-performance object detection.

## Features

- Real-time face detection with YOLOv8
- Easy integration with webcam
- Customizable detection thresholds and labels

## Installation

You can install the library via pip. Run the following command in your terminal:

```bash
pip install face_detection_lib
```

## Usage

To use the `face_detection_lib` library for face detection, follow these steps:

### Basic Usage

```python
from face_detection_lib.detector import FaceDetector

# Initialize the FaceDetector
detector = FaceDetector()

# Start the webcam and run face detection
detector.run_webcam()
```

### Custom Configuration

You can customize the face detection by passing parameters to the `FaceDetector` class. For example, you can set a custom model path, labels, or confidence threshold:

```python
from face_detection_lib.detector import FaceDetector

# Define custom parameters
custom_model_path = 'path/to/your/custom/model.pt'
custom_labels = {0: 'Person A', 1: 'Person B'}
custom_confidence_threshold = 0.7

# Initialize the FaceDetector with custom parameters
detector = FaceDetector(
    model_path=custom_model_path,
    labels=custom_labels,
    confidence_threshold=custom_confidence_threshold
)

# Start the webcam with custom settings
detector.run_webcam()
```

## Testing

Ensure that your library functions as expected by writing tests in the `tests/test_detector.py` file. Here's a basic example of how you might start testing:

```python
def test_face_detection():
    # Initialize the FaceDetector
    detector = FaceDetector()
    
    # Add tests to verify the functionality
    assert detector is not None
    # Further tests can be added here
```

### Running Tests

To run your tests, execute:

```bash
pytest
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, please submit a pull request or open an issue.

### Contributors
- [Sehastrajit](https://github.com/Sehastrajit)
- [Deena](https://github.com/Deena1412)




## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using `face_detection_lib`!
