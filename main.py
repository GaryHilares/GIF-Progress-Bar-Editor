from PIL import Image, ImageSequence
import sys

colors = {
    "white": (255,255,255),
    "red": (255,0,0),
    "green": (0,255,0),
    "blue": (0,0,255),
    "black": (0,0,0)
}

def get_gif_frames_and_duration(gif_filename):
    gif = Image.open(sys.argv[1])
    gif_frames = []
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
    return [gif_frames, gif.info['duration']]

def add_progress_bar_to_images(gif_frames,bar_height,rgb_color):
    for i in range(len(gif_frames)):
        width, height = gif_frames[i].size
        pixels = gif_frames[i].load()
        for j in range(int(width*i/len(gif_frames))):
            for k in range(1,bar_height+1):
                pixels[j, height-k] = rgb_color
    return gif_frames

def assemble_and_save_gif(target_filename,gif_duration,gif_frames):
    gif_frames[0].save(target_filename, format='GIF',
                   append_images=gif_frames[1:],
                   save_all=True,
                   duration=gif_duration, loop=0)

def main():
    if len(sys.argv) == 1:
        print('Insufficient arguments')
        sys.exit()
    filename = sys.argv[1]
    rgb_color = colors[sys.argv[2]] if len(sys.argv) >= 3 and sys.argv[2] in colors else colors["blue"]
    bar_height = int(sys.argv[3]) if len(sys.argv) >= 4 and sys.argv[3].isnumeric() else 3
    frames, duration = get_gif_frames_and_duration(filename)
    frames_with_progress_bar = add_progress_bar_to_images(frames,bar_height,rgb_color)
    assemble_and_save_gif('progress_bar_{}'.format(filename),duration,frames_with_progress_bar)

if __name__ == '__main__':
    main()
