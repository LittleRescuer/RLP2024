# Import necessary scripts and files to run the program
from Communications_Module.image_sender import ImageUploader
from Image_Processing_Module.image_processor import ImageProcessor
from Movement_Module.movement_controller import MovementController
from time import sleep, time

print("Modules Imported Successfully")

# Create Instances of the imported classes
imageUploader = ImageUploader(None)
imageProcessor = ImageProcessor()
movementController = MovementController()



# Create functions to interact with the classes
def uploadImage(frame):
    print("Uploading Image")
    finalFrameName = f"frame_{time()}.jpg"
    imageProcessor.writeImage(frame, finalFrameName)

    imageUploader.setNewImagePath(finalFrameName)
    return imageUploader.upload()

def captureFrame():
    print("Capturing Frame")
    return imageProcessor.capture_frame()

def detectLine(frame):
    print("Detecting Line")
    result = imageProcessor.detect_line(frame)
    if result[0] is not None:
        line_position, _ = result
        frame_center = frame.shape[1] // 2
        if abs(line_position - frame_center) < 50:
            return { "position": "center", "line_position": line_position }
        elif line_position < frame_center:
            return { "position": "left", "line_position": line_position }
        else:
            return { "position": "right", "line_position": line_position }
    else:
        return { "position": None, "line_position": None }

def main():
    startTime = time()

    while True:
        frame = captureFrame()
        line = detectLine(frame)
        if line["position"] == "center" or line["position"] is None:
            movementController.moveForward()
        elif line["position"] == "left":
            movementController.moveLeft()
            sleep(0.5)
            continue
        elif line["position"] == "right":
            movementController.moveRight()
            sleep(0.5)
            continue

        actualTime = time()
        if actualTime - startTime > 25:
            break
        print("Time Elapsed: ", actualTime - startTime)
        sleep(5)
    movementController.stop()
    
    finalFrame = captureFrame()
    uploadImage(finalFrame)

if __name__ == "__main__":
    main()