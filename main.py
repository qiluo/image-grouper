#! /usr/bin/env python

"""Image Grouper.

Usage:
  image-grouper <source_dir> [-o <output_dir>] [-r] [--move] [--exifonly] [-f <format>] [-d]
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
  -d               show debugging info

"""
from docopt import docopt
import os
from logger import Logger

if __name__ == '__main__':
    args = docopt(__doc__, version='0.0.1')
    logger = Logger(args['-d'])
    logger.info(args)

    images = []
    for (dirpath, dirnames, filenames) in os.walk(os.path.abspath(args['<source_dir>'])):
        for filename in filenames:
            logger.info(os.sep.join([dirpath, filename]))
            images.extend(os.sep.join([dirpath, filename]))

        # no recurse, just top level dir
        if not args['-r']:
            break

def readExif(image_path):
    pass

def handleImageByDate(imagePath, date, shoudMove, outputDir):
    pass
