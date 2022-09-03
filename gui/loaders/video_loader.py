import cv2


class VideoLoader:
    def __init__(self, video_path: str):
        self.video_path: str = video_path
        self.video = cv2.VideoCapture(self.video_path)

    def get_video_frames(self):
        frames = []
        frame_counter = 0
        while True:
            ret, frame = self.video.read()
            if ret is False:
                break
            if frame_counter % 30 == 0:
                frames.append(frame)
            frame_counter = (frame_counter + 1) % 30

        print(f"Using: {len(frames)} frames")
        return frames
