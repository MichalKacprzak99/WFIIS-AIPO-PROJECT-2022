import cv2
import numpy as np
import math


class RoadSideDetector:
    def count_angle_line(self, x1, y1, x2, y2):
        angle = abs(math.atan2(abs(y2 - y1), abs(x2 - x1)) * 180.0 / math.pi)
        return angle


    def is_near_center_line(self, width, x1, x2):
        center = width / 2
        max_distance = width / 4
        if abs(center - x1) < max_distance and abs(center - x2) < max_distance:
            return True
        else:
            return False

    def detect(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        width = img.shape[1]
        img_canny = cv2.Canny(img, 100, 200)

        lines = cv2.HoughLinesP(img_canny, 1, np.pi / 180, threshold=50, minLineLength=50, maxLineGap=10)

        # if there are no or too little lines found
        if lines is None or len(lines) < 4:
            return None

        sum_left_lines = 0
        sum_right_lines = 0

        for line in lines:
            x1, y1, x2, y2 = line[0]
            angle = self.count_angle_line(x1, y1, x2, y2)

            # eliminate lines near horizontal and near vertical
            if 0 <= angle <= 20 or 80 <= angle <= 90:
                continue

            # make lines near center more important
            multiplier = 1.5 if self.is_near_center_line(width, x1, x2) else 1

            if y1 < y2 and x1 < x2:
                sum_left_lines += multiplier
            elif y1 < y2 and x1 > x2:
                sum_right_lines += multiplier
            elif y1 > y2 and x1 < x2:
                sum_right_lines += multiplier
            elif y1 > y2 and x1 > x2:
                sum_left_lines += multiplier

        return "right" if sum_right_lines >= sum_left_lines else "left"

