import cv2
import numpy as np
from skimage.filters import frangi

def vanisotropic(image,i,value):
    def add_anisotropic_noise(image, strength=0.1):
        # Generate anisotropic noise using the Frangi filter
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        filtered_image = frangi(gray_image)
        noise = (filtered_image - np.min(filtered_image)) / (np.max(filtered_image) - np.min(filtered_image))
        noise = noise * 2 * strength - strength
        
        # Add noise to the image
        noisy_image = image.astype(np.float64) + noise[:, :, np.newaxis]
        noisy_image = np.clip(noisy_image, 0, 30).astype(np.uint8)
        
        return noisy_image

    # Load video
    video_path = image
    cap = cv2.VideoCapture(video_path)

    # Check if video file is opened successfully
    if not cap.isOpened():
        print("Error opening video file.")

    # Create a VideoWriter object to save the noisy video
    output_path = 'output/anisotropic'+str(i)+'.mp4'
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

        # Add anisotropic noise to the frame
        noisy_frame = add_anisotropic_noise(frame, value)

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
