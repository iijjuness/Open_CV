import cv2

path = '/Users/iijjuness/PycharmProjects/pythonProject3/lec9/images/*.bmp'
# Load the image
img = cv2.imread(path)

# Define the output video file name, codec, frame rate, and frame size
out_filename = 'output.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 30.0
frame_size = (600, 400)

# Create the VideoWriter object
out = cv2.VideoWriter(out_filename, fourcc, fps, frame_size)

# Write the frames to the video
for i in range(100):
    # Create a new frame by copying the original image
    frame = img.copy()

    # Add some text to the frame
    cv2.putText(frame, f"Frame {i}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Write the frame to the video
    out.write(frame)

# Release the VideoWriter object
out.release()

# Destroy any OpenCV windows
cv2.destroyAllWindows()
