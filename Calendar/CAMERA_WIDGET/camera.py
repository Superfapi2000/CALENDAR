import cv2

# Open a camera using the default camera index (usually 0)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error opening the camera.")
    exit()

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Continuously capture frames from the camera
while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
    
    # Check if the frame was captured successfully
    if not ret:
        print("Error capturing the frame.")
        break
    
    # Write the frame to the output file
    out.write(frame)
    
    # Display the captured frame
    cv2.imshow('Camera', frame)
    
    # Check if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
out.release()
cv2.destroyAllWindows()
