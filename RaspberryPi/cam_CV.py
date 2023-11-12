import cv2
import os
    
class Camera:
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        self.camera.set(3, 640)
        
        frame_num = int(self.camera.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_width = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.video_writer = cv2.VideoWriter(f"Videos//Video {len(os.listdir('//home//pi//SwordBot//src//Videos')) + 1}.mp4",fourcc, 25.0,(frame_width,frame_height))
        
        self.faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    def tick(self):
        # called every tick
        success, img = self.camera.read()
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        faces = self.faceCascade.detectMultiScale(imgGray)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(img, "TARGET", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 1)
            
        self.video_writer.write(img)
        return img, faces
    def kill(self):
        self.camera.release()
        self.video_writer.release()
        del self