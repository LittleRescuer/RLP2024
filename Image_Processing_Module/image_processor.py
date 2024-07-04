# Image_Processing_Module/image_processor.py

import cv2
import numpy as np
from picamera2 import Picamera2


class ImageProcessor:
    def __init__(self):
        self.picam2 = Picamera2()
        self.picam2.start()

    def capture_frame(self):
        frame = self.picam2.capture_array()
        return cv2.rotate(frame, cv2.ROTATE_180)

    def detect_line(self, frame):
        # Create a copy of the frame for drawing
        display_frame = frame.copy()

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply threshold
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Find the largest contour
            largest_contour = max(contours, key=cv2.contourArea)

            # Get the moments of the largest contour
            M = cv2.moments(largest_contour)

            if M["m00"] != 0:
                # Calculate the centroid of the contour
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # Draw the contour and centroid on the display frame
                cv2.drawContours(display_frame, [largest_contour], 0, (0, 255, 0), 2)
                cv2.circle(display_frame, (cx, cy), 7, (0, 0, 255), -1)
                cv2.putText(display_frame, f"({cx}, {cy})", (cx - 20, cy - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                # Draw a vertical line at the center of the frame
                frame_center = frame.shape[1] // 2
                cv2.line(display_frame, (frame_center, 0), (frame_center, frame.shape[0]), (255, 0, 0), 2)

                return cx, display_frame

        # If no line is detected, just draw the center line
        frame_center = frame.shape[1] // 2
        cv2.line(display_frame, (frame_center, 0), (frame_center, frame.shape[0]), (255, 0, 0), 2)
        return None, display_frame

    def close(self):
        self.picam2.close()