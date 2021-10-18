<h1 align="center">
  GIF Progress Bar Editor
</h1>

<p align="center">
  <img alt="badge-lastcommit" src="https://img.shields.io/github/last-commit/GaryNLOL/GIF_Progress_Bar_Editor?style=for-the-badge">
  <img alt="badge-openissues" src="https://img.shields.io/github/issues-raw/GaryNLOL/GIF_Progress_Bar_Editor?style=for-the-badge">
  <img alt="badge-license" src="https://img.shields.io/github/license/GaryNLOL/GIF_Progress_Bar_Editor?style=for-the-badge">
  <img alt="badge-contributors" src="https://img.shields.io/github/contributors/GaryNLOL/GIF_Progress_Bar_Editor?style=for-the-badge">
  <img alt="badge-codesize" src="https://img.shields.io/github/languages/code-size/GaryNLOL/GIF_Progress_Bar_Editor?style=for-the-badge">
</p>

## What is GIF_Progress_Bar_Editor?
GIF Progress Bar Editor is a tool that provides an easy and fast way to add a progress bar to your GIF.

### Dependencies
- [Pillow](https://pillow.readthedocs.io/en/stable/#).

## Usage
### Installation
Source code:
1. Clone the GitHub repository.
2. Install the dependencies with `pip install -r requirements.txt`.

That's it!

### Commands
Just use the command:
```python3
py main.py ${your filename}
```

That's it! The script does the rest.

There are also optional parameters that allow you to personalize your gif:
```python3
py main.py ${your filename} color=${your color} out=${your output filename} height=${your progress bar height}
```
Where:
- `color` is a name color (Currently only colors in `['white','red','green','blue','black']` are supported) representing the color of the progress bar.
- `height` is an integer representing the height of the progress bar.
- `out` is a string representing the output filename.

### Example
Before:

<p align="center">
   <img alt="Supple-Crystal" src="https://user-images.githubusercontent.com/46727048/137753081-ce02743a-720e-4200-9b8b-2b540338b8da.gif" />
</p>

Command:

`py main.py Supple-Crystal.gif color=red height=5 out=my_gif.gif`

After:

<p align="center">
   <img alt="my_gif" src="https://user-images.githubusercontent.com/46727048/137754676-2c59810c-d977-4b91-ae4b-959382c36a31.gif" />
</p>

Image taken from [Supple Crystal](https://github.com/GaryNLOL/Supple-Crystal/).

## License
All the code owned in this repository is under the [MIT license](https://github.com/GaryNLOL/GIF_Progress_Bar_Editor/blob/main/LICENSE).

## Contributors
Thanks to these wonderful people for making GIF Progress Bar Editor possible!

<p align="center"><a href="https://github.com/GaryNLOL/GIF_Progress_Bar_Editor/graphs/contributors"><img src="https://contrib.rocks/image?repo=GaryNLOL/GIF_Progress_Bar_Editor" /></a></p>
