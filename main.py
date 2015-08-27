#! /usr/bin/env python

"""Image Grouper.

Usage:
  image-grouper <source_dir> [-o <output_dir>] [-r] [--move] [--exifonly] [-f <format>]
  image-grouper (-h | --help)
  image-grouper (-v | --version)

Arguments:
  source_dir        path to image source directory

Options:
  -h --help         show this screen
  -v --version      show version
  -o <output_dir>   specify output dir
  -r                read source recursively [default: False]
  --move            move images instead of copying, source will be deleted,
                    use it by caution [default: False]
  --exifonly        read exif only [default: False]
  -f <format>       date format

"""
from docopt import docopt


if __name__ == '__main__':
    args = docopt(__doc__, version='0.0.1')
    print(args)
