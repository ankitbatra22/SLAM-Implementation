import click
from algorithms.hough_lanes import generate_lines
import cv2
import os


@click.command()
@click.option('--display/--no-display', default=False, help='something!')
@click.argument('file', nargs=1)
def display_video(display, file):
    if display:
        video_path = os.path.join(os.getcwd(),"videos")
        print(os.path.join(video_path, file))
        cap = cv2.VideoCapture(os.path.join(video_path, file))
        while cap.isOpened():
            ret, frame = cap.read()
            hough_transform = generate_lines(frame)
            cv2.imshow("highlighted", hough_transform)  # Shows original video with detected lane lines.
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    display_video()
