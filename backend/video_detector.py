from video_model.predict_video import predict_video


def detect_video(video_path):

    result = predict_video(video_path)

    return result