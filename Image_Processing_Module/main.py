# main.py

import cv2
import time
from Image_Processing_Module.image_processor import ImageProcessor


def main():
    image_processor = ImageProcessor()
    frame_count = 0

    try:
        while True:
            # Capture a frame
            frame = image_processor.capture_frame()

            # Detect the line
            result = image_processor.detect_line(frame)

            if result[0] is not None:
                line_position, display_frame = result
                frame_center = frame.shape[1] // 2
                if abs(line_position - frame_center) < 50:
                    print(f"Line detected near center: {line_position}")
                elif line_position < frame_center:
                    print(f"Line detected on left: {line_position}")
                else:
                    print(f"Line detected on right: {line_position}")
            else:
                _, display_frame = result
                print("No line detected")

            # Save the frame with the detected line
            cv2.imwrite(f"debug_frame_{frame_count:04d}.jpg", display_frame)
            frame_count += 1

            # Optional: display the frame (if you're running this on a system with a display)
            cv2.imshow('Line Detection', display_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            time.sleep(0.1)  # Adjust delay as needed

    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        image_processor.close()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()