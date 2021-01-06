import cv2


def compute_orb_features(image):
    orb = cv2.ORB_create()

    kp = orb.detect(image, None)

    kp, des = orb.compute(image, kp)

    return kp


def draw_keypoints(image_original, image_processed):
    kp = compute_orb_features(image_original)

    return cv2.drawKeypoints(image_processed, kp, outImage=None, color=(0, 255, 0), flags=0)
