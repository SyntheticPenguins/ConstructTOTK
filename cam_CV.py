import cv2

# webcam
camera = cv2.VideoCapture(0)
camera.set(3, 640)
camera.set(4, 480)

# face cascade
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# main loop
while True:
    success, img = camera.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    
    faces = faceCascade.detectMultiScale(imgGray)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, "TOILET", (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 255, 0), 1)
    
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 