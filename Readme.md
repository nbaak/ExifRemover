# Exif Remover
Scans and/or Removes Exif Data from image files.

## Usage
./App.py -h

```
Scans and removes Exif Data on images

options:
  -h, --help            show this help message and exit
  -t target, --target target
                        image or path
  -s, --scan            scan file(s) and verbose exif
  -r, --remove          removes exif from file(s)
```

## Installation
To use this Tool, you need to install the Python Image Library PIL(<a href="https://pillow.readthedocs.io/en/stable/">Pillow</a>).

```bash
python3 -m pip install --upgrade Pillow
```