import requests
import os
URL = "https://little-rescuer.vercel.app/api/uploadImage"

class ImageUploader:
    def __init__(self, image_path):
        self.image_path = image_path
        print("Image Uploader Initialized")

    def setNewImagePath(self, new_image_path):
        self.image_path = new_image_path

    def upload(self):
        print("Uploading Image")
        if not os.path.isfile(self.image_path):
            return "File does not exist"

        with open(self.image_path, 'rb') as image_file:
            files = { 'image': image_file }
            response = requests.post(URL, files = files)
            if response.ok:
                print("Image Uploaded Successfully")
            return response.text
