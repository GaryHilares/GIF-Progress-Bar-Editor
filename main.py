from PIL import Image, ImageSequence
import sys

if len(sys.argv) == 1:
    print('Insufficient arguments')
    sys.exit()

gif_filename = sys.argv[1]
gif = Image.open(gif_filename)
gif_duration = gif.info['duration']
gif_frames_number = gif.n_frames
width, height = gif.size
gif_frames = []

def get_frames():
    pal = gif.getpalette()
    prev = gif.convert('RGBA')
    prev_dispose = True
    for i, frame in enumerate(ImageSequence.Iterator(gif)):
        dispose = frame.dispose

        if frame.tile:
            x0, y0, x1, y1 = frame.tile[0][1]
            if not frame.palette.dirty:
                frame.putpalette(pal)
            frame = frame.crop((x0, y0, x1, y1))
            bbox = (x0, y0, x1, y1)
        else:
            bbox = None

        if dispose is None:
            prev.paste(frame, bbox, frame.convert('RGBA'))
            gif_frames.append(prev.copy())
            prev_dispose = False
        else:
            if prev_dispose:
                prev = Image.new('RGBA', gif.size, (0, 0, 0, 0))
            out = prev.copy()
            out.paste(frame, bbox, frame.convert('RGBA'))
            gif_frames.append(out.copy())

def add_progress_bar_to_images():
    for i in range(gif_frames_number):
        pixels = gif_frames[i].load()
        for j in range(int(width*i/gif_frames_number)):
            pixels[j, height-3] = (0, 0, 255)
            pixels[j, height-2] = (0, 0, 255)
            pixels[j, height-1] = (0, 0, 255)

def assemble_and_save_gif():
    gif_frames[0].save('progress_bar_{}'.format(gif_filename), format='GIF',
                   append_images=gif_frames[1:],
                   save_all=True,
                   duration=gif_duration, loop=0)

def main():
    get_frames()
    add_progress_bar_to_images()
    assemble_and_save_gif()

if __name__ == '__main__':
    main()
