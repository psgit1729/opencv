import cv2

# Load pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Read and resize the image
rimg = cv2.imread("rahul.png")
img = cv2.resize(rimg, (800, 800), interpolation=cv2.INTER_AREA)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the image
cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
