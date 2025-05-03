import cv2 as cv
import numpy as np
from PIL import Image

# Define HSV color range for blue detection
lowerColor = np.array([100,180,100])  # Lower bound of blue in HSV
upperColor = np.array([140,240,255])  # Upper bound of blue in HSV

# Open the webcam (0 = default camera)
cam = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    isTrue, frame = cam.read()
    
    # Convert the frame from BGR to HSV color space
    hsvImage = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Create a mask for pixels within the HSV color range
    mask = cv.inRange(hsvImage, lowerColor, upperColor)

    # Convert mask to a PIL image to use getbbox (bounding box)
    mask_ = Image.fromarray(mask)

    # Get bounding box around detected area
    bbox  = mask_.getbbox()
    
    if not bbox == None:
        x1, y1, x2, y2 = bbox
        # Draw rectangle around detected area
        cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
        # Add label text above the rectangle
        cv.putText(frame, "Blue", (x1 + 10, y1 - 20), cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    # Show the original camera feed with rectangle
    cv.imshow('Original Camera Feed', frame)

    # Press 'q' to exit
    if cv.waitKey(1) & 0XFF == ord('q'):
        break

# Release the webcam and destroy all OpenCV windows
cam.release()
cv.destroyAllWindows()
