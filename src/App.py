#!/usr/bin/env python3

from PIL import Image, ExifTags, UnidentifiedImageError
from pathlib import Path
import argparse


def test():
    src = "test.jpg"
    image = Image.open(src)
    print(_find_exif_data(image))
    
    remove_exif(image, save_path=src)

    
def _find_exif_data(path):
    image = Image.open(path)
    exif_data = image._getexif()
    if exif_data:
        exif = {
            ExifTags.TAGS[k]: v
            for k, v in exif_data.items()
                if k in ExifTags.TAGS
        }
    
        return exif
    
    return None


def show_exif_data(path):
    exif = _find_exif_data(path)
    
    if exif:
        for k, v in exif.items():
            print(k, v)
    else:
        print("no exif data found")


def remove_exif(path, save_path=None):
    image = Image.open(path)
    data = list(image.getdata())
    clean_image = Image.new(image.mode, image.size)
    clean_image.putdata(data)
    
    if save_path:
        clean_image.save(save_path)
    
    return clean_image


def _is_image(path):
    try:
        image = Image.open(path)
        return True
    
    except UnidentifiedImageError:
        return False
    
    return False


def file_scan(path:Path, scan=False, remove=False):
    if _is_image(path):
        print(f"scan file: {path.resolve()}")
    
        if scan:
            show_exif_data(path)
            print()
            
        if remove:
            print('removing exif data')
            remove_exif(path, path)


def folder_scan(path, scan=False, remove=False):
    print(f"scan folder: {path.resolve()}")
    files = list(filter(_is_image, path.glob('**/*')))
    
    for file in files:
        print(file.resolve())
        if scan:
            show_exif_data(path)
            print()
            
        if remove:
            print('removing exif data')
            remove_exif(file, file)


def main():
    parser = argparse.ArgumentParser(prog="Exif Remove", description="Scans and removes Exif Data on images")
    parser.add_argument('-t', '--target', metavar='target', type=str, help="image or path")
    parser.add_argument('-s', '--scan', action="store_true", help="scan file(s) and verbose exif")
    parser.add_argument('-r', '--remove', action="store_true", help="removes exif from file(s)")
    
    args = parser.parse_args()
    
    if args.target:
        target = Path(args.target)
        if target.exists():
            if target.is_file():
                file_scan(target, args.scan, args.remove)
            elif target.is_dir():
                folder_scan(target, args.scan, args.remove)
    
    else:
        print("no target given")
    
    exit()


if __name__ == "__main__":
    main()
