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
import exifread

# what tags use to redate file (use first found)
DT_TAGS = ["Image DateTime", "EXIF DateTimeOriginal", "DateTime"]

def readExifDate(image_path):
    """read date from exif, return in format of ('2005:10:20 23:22:28'),
    return None if any error"""
    f = open(image_path, 'rb')
    try:
        tags = exifread.process_file(f, details=False)
        for dt_tag in DT_TAGS:
            try:
                dt_value = '%s' % tags[dt_tag]
                logger.info('%s: %s' % (dt_tag, dt_value))
            except:
                continue

        if dt_value:
            return dt_value
    finally:
        f.close()

    return None


def handleImageByDate(imagePath, date, shouldMove, outputDir):
    pass

if __name__ == '__main__':
    args = docopt(__doc__, version='0.0.1')
    logger = Logger(args['-d'])
    logger.info(args)

    images = []
    for (dirpath, dirnames, filenames) in os.walk(os.path.abspath(args['<source_dir>'])):
        for filename in filenames:
            logger.info(os.sep.join([dirpath, filename]))
            images.extend(os.sep.join([dirpath, filename]))
            date = readExifDate(os.sep.join([dirpath, filename]))
            logger.info(date)

        # no recurse, just top level dir
        if not args['-r']:
            break
