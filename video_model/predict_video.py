import cv2

def predict_video(video_path):

    cap = cv2.VideoCapture(video_path)

    frame_count = 0

    while True:

        success, frame = cap.read()

        if not success:
            break

        frame_count += 1

    cap.release()

    return f"Video Processed Successfully | Frames: {frame_count}"