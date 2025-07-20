import cv2 as cv
import face_recognition

# Load known image
known_image = face_recognition.load_image_file("Faisal Shaikh.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Initialize webcam
video_capture = cv.VideoCapture(0)

# Ensure window is initialized correctly
cv.namedWindow('Face Recognition', cv.WINDOW_NORMAL)

while True:
    ret, frame = video_capture.read()

    # Resize frame for faster processing
    small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert BGR (OpenCV format) to RGB (face_recognition format)
    rgb_small_frame = cv.cvtColor(small_frame, cv.COLOR_BGR2RGB)

    # Find face locations and encodings
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Scale back up to original size
        top, right, bottom, left = top*4, right*4, bottom*4, left*4

        # Compare faces
        matches = face_recognition.compare_faces([known_encoding], face_encoding)
        name = "Unknown"

        if True in matches:
            name = "Faisal Shaikh"

        # Draw rectangle and label
        cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv.putText(frame, name, (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv.imshow('Face Recognition', frame)

    # Press 'Q' to exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
cv.destroyAllWindows()
