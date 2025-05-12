# **Gesture Recognition System**
## **Purpose**
This code creates a real-time gesture recognition system that counts the number of fingers held up in front of a camera. It's designed to:
Detect and track a single hand within a defined Region of Interest (ROI)
Identify and count extended fingers
Display the finger count on the video feed
Operate in real-time using a webcam

## **Technologies Used**
OpenCV (cv2): For video capture, image processing, and display
MediaPipe: Specifically the Hands module for hand landmark detection
Provides 21 precise landmarks for each detected hand
Handles hand pose estimation and tracking

## **Computer Vision Techniques:**
Region of Interest (ROI) processing
Color space conversion (BGR to RGB)
Image flipping for mirror effect

## **Usage**
Run the script with Python (requires installed dependencies)
Position your hand within the green rectangular ROI on screen
The system will:
Detect your hand
Track finger positions
Count how many fingers are extended
Display the count above the ROI box
Press 'q' to quit the application

## **Key Features**
Fixed ROI for focused processing
Real-time performance (optimized by processing only the ROI)
Finger counting logic for both thumb and other fingers
Visual feedback with landmarks and count display

## **Conclusion**
This implementation demonstrates a practical application of MediaPipe's hand tracking capabilities for gesture recognition. The system effectively:
Balances accuracy and performance through ROI processing
Provides clear visual feedback
Could serve as a foundation for more complex gesture-based interfaces
Shows potential for integration into HCI (Human-Computer Interaction) systems

