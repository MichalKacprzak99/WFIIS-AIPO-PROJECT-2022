import cv2


class VideoLoader:
    def __init__(self, video_path: str):
        self.video_path: str = video_path
        self.video = cv2.VideoCapture(self.video_path)

    def get_video_frames(self):
        frames = []
        while True:
            ret, frame = self.video.read()
            if ret is False:
                break
            frames.append(frame)

        return frames
