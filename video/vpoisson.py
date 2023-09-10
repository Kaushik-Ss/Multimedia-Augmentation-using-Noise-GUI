import cv2
import numpy as np

def vpoisson(image,i,value):
    def add_poisson_noise(image):
        # Generate Poisson noise
        noisy_image = np.random.poisson(image)

        # Clip the pixel values to the valid range
        noisy_image = np.clip(noisy_image, 0, value*100).astype(np.uint8)

        return noisy_image

    # Load video
    video_path = image
    cap = cv2.VideoCapture(video_path)

    # Check if video file is opened successfully
    if not cap.isOpened():
        print("Error opening video file.")

    # Create a VideoWriter object to save the noisy video
    output_path = 'output/poisson'+str(i)+'.mp4'
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

        # Convert the frame to grayscale for Poisson noise
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Add Poisson noise to the frame
        noisy_frame = add_poisson_noise(gray_frame)

        # Convert the noisy frame back to color
        noisy_frame = cv2.cvtColor(noisy_frame, cv2.COLOR_GRAY2BGR)

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
