# Import necessary scripts and files to run the program
from Communications_Module.image_sender import ImageUploader
from Image_Processing_Module.image_processor import ImageProcessor
from Movement_Module.movement_controller import MovementController
from Camera_Tracking_Module.servo_controller import ServoController
from time import sleep, time

print("Modules Imported Successfully")

# Create Instances of the imported classes
imageUploader = ImageUploader(None)
imageProcessor = ImageProcessor()
movementController = MovementController()
servoController = ServoController()



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
    
# Returns True if has to continue to the next loop iteration
def decideMovement(line):
    if line["position"] == "center" or line["position"] is None:
        movementController.moveForward()
        return False
    elif line["position"] == "left":
        movementController.moveLeft()
        return True
    elif line["position"] == "right":
        movementController.moveRight()
        return True
        

def main():
    startTime = time()

    while True:
        frame = captureFrame()
        line = detectLine(frame)
        

        actualTime = time()
        print("Time Elapsed: ", actualTime - startTime)
        if actualTime - startTime > 15:
            break

        hasToContinue = decideMovement(line)
        if hasToContinue:
            sleep(0.5)
            continue
        else :
            sleep(5)
    
    movementController.stop()

    servoController.moveToMax()
    print("Waiting for the servo to rotate")
    sleep(10) # Wait for the servo to move
    
    finalFrame = captureFrame()
    uploadImage(finalFrame)
    
    imageProcessor.close()

if __name__ == "__main__":
    main()