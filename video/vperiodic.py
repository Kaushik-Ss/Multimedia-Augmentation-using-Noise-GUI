import cv2
import numpy as np

def add_periodic_noise(image, frequency=10, strength=50):
    # Create mesh grid of image dimensions
    x, y = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))

    # Generate periodic noise pattern
    noise = strength * np.sin(2*np.pi*frequency*(x+y)/(image.shape[0]+image.shape[1]))

    # Reshape noise to match the shape of the image
    noise = np.tile(noise[:, :, np.newaxis], (1, 1, 3))

    # Add noise to the image
    noisy_image = np.clip(image + noise.astype(np.uint8), 0, 255)

    return noisy_image

# Load video
video_path = 'video/sample.mp4'
cap = cv2.VideoCapture(video_path)

# Check if video file is opened successfully
if not cap.isOpened():
    print("Error opening video file.")

# Create a VideoWriter object to save the noisy video
output_path = 'video/output/noisy_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Choose codec
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Process each frame of the video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Add periodic noise to the frame
    noisy_frame = add_periodic_noise(frame, frequency=10, strength=50)

    # Write the noisy frame to the output video
    out.write(noisy_frame)

    # Display the noisy frame (optional)
    cv2.imshow('Noisy Frame', noisy_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video objects and close windows
cap.release()
out.release()
cv2.destroyAllWindows()