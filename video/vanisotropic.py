import cv2
import numpy as np

def vanisotropic(image, i, value):
    def add_anisotropic_noise(image, strength=value):
        noise = np.random.normal(0, strength, image.shape).astype(np.float32)
        noisy_image = image.astype(np.float32) + noise
        noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
        return noisy_image
    video_path = image
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file.")

    output_path = 'output/anisotropic' + str(i) + '.mp4'
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        noisy_frame = add_anisotropic_noise(frame, value)
        out.write(noisy_frame)
        cv2.imshow('Noisy Frame', noisy_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

