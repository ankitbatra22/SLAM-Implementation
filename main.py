import click
from algorithms.hough_lanes import generate_lines
from algorithms.ORB_features import draw_keypoints
from algorithms.optical_flow import compute_optical_flow
from algorithms import object_detection
import cv2
import os


@click.command()
@click.option('--display/--no-display', default=False, help='something!')
@click.option('--flow/--no-flow', default=False, help='something!')
@click.argument('file', nargs=1)
def display_video(display, flow, file):
    if display and not flow:
        video_path = os.path.join(os.getcwd(), "videos")
        print(os.path.join(video_path, file))
        cap = cv2.VideoCapture(os.path.join(video_path, file))
        while cap.isOpened():
            ret, frame = cap.read()
            hough_transform = generate_lines(frame)
            orb_frame = draw_keypoints(frame, hough_transform)
            object_detect = object_detection.draw_boxes(frame, orb_frame)
            cv2.imshow("highlighted", object_detect)  # Shows original video with detected lane lines.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    elif display and flow:
        video_path = os.path.join(os.getcwd(), "videos")
        print(os.path.join(video_path, file))
        cap = cv2.VideoCapture(os.path.join(video_path, file))

        ret, prev = cap.read()

        while cap.isOpened():
            ret, next = cap.read()

            rgb = compute_optical_flow(prev, next)
            cv2.imshow("highlighted", rgb)  # Shows original video with detected lane lines.

            prev = next
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    display_video()
