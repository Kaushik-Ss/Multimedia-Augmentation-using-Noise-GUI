import cv2
import numpy as np

def add_impulse_noise(image, probability=0.01, salt_vs_pepper=0.5):
    # Copy the image to avoid modifying the original
    noisy_image = np.copy(image)

    # Generate random indices for noise pixels
    height, width, _ = image.shape
    num_pixels = int(height * width * probability)
    indices = np.random.choice(range(height * width), size=num_pixels, replace=False)

    # Assign random values for salt and pepper noise
    salt = np.random.randint(low=0, high=256, size=(num_pixels // 2, 3))
    pepper = np.random.randint(low=0, high=256, size=(num_pixels // 2, 3))

    # Add salt and pepper noise to the noisy image
    noisy_image = np.reshape(noisy_image, (height * width, 3))
    noisy_image[indices[:num_pixels // 2]] = salt
    noisy_image[indices[num_pixels // 2:]] = pepper
    noisy_image = np.reshape(noisy_image, (height, width, 3)).astype(np.uint8)

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

    # Add impulse noise to the frame
    noisy_frame = add_impulse_noise(frame, probability=0.01, salt_vs_pepper=0.5)

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
