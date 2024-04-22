import cv2

# Open video file or capture device
cap = cv2.VideoCapture(0)  # Use 0 for webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break  # End of video or error

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Display the result
    cv2.imshow('Canny Edges', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  # Exit loop if 'q' is pressed

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
