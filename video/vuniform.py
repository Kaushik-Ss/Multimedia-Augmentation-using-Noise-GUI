import cv2
import numpy as np

def vuniform(image,i,value):

    def add_uniform_noise(image, low=0, high=50):
        # Generate uniform noise
        noise = np.random.uniform(low, high, size=image.shape)

        # Add noise to the image
        noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)

        return noisy_image

    # Load video
    video_path = image
    cap = cv2.VideoCapture(video_path)

    # Check if video file is opened successfully
    if not cap.isOpened():
        print("Error opening video file.")

    # Create a VideoWriter object to save the noisy video
    output_path = 'output/uniform'+str(i)+'.mp4'
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

        # Add uniform noise to the frame
        noisy_frame = add_uniform_noise(frame, low=0, high=value*100)

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
