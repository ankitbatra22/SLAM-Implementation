import click
from algorithms.videoProcess import open_video

@click.command()
@click.option('--display/--no-display', default = False, help='something!')
def display_video(display):
    print(display)
    if display == True:
        open_video()


if __name__ == '__main__':
    display_video()
    open_video()
    