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
  -f <format>       output dir name format, specify month for yyyy-mm or day for yyyy-mm-dd [default: month]
  -d                show debugging info

"""
from docopt import docopt
import os
import time
import shutil
from logger import Logger
import exifread

# what tags use to redate file (use first found)
DT_TAGS = ["Image DateTime", "EXIF DateTimeOriginal", "DateTime"]
VALID_IMAGE_TYPE = ['.jpg', '.JPG']


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
                return exif_info2time(dt_value)
    finally:
        f.close()

    return None


def exif_info2time(ts):
    """changes EXIF date ('2005:10:20 23:22:28') to number of seconds since 1970-01-01"""
    tpl = time.strptime(ts + 'UTC', '%Y:%m:%d %H:%M:%S%Z')
    return time.mktime(tpl)


def calcOutputDirPath(imageFilePath, isExifOnly, outputParentDir):
    date = readExifDate(imageFilePath)
    if date:
        dt = date
    elif not isExifOnly:
        logger.info('using file last modified time')
        dt = os.path.getmtime(imageFilePath)
    else:
        dt = None

    # %Y-%m by default
    dateFormat = '%Y-%m-%d' if args['-f'] == 'day' else '%Y-%m'
    targetDirName = time.strftime(dateFormat, time.localtime(dt)) if dt else None
    return os.sep.join([outputParentDir, targetDirName])

if __name__ == '__main__':
    args = docopt(__doc__, version='0.0.1')
    logger = Logger(args['-d'])
    logger.info(args)

    for (dirpath, dirnames, filenames) in os.walk(os.path.abspath(args['<source_dir>'])):
        for filename in filenames:
            for ext in VALID_IMAGE_TYPE:
                if filename.endswith(ext):
                    filepath = os.sep.join([dirpath, filename])
                    logger.info(filepath)
                    targetDirName = calcOutputDirPath(filepath, args[
                                                      '--exifonly'], os.path.abspath(args['-o']) if args['-o'] else os.path.abspath(args['<source_dir>']))
                    logger.info('output dir name is %s' % targetDirName)
                    try:
                        os.makedirs(targetDirName)
                    except:
                        pass

                    try:
                        if not args['--move']:
                            logger.info('coping image from %s to %s' %
                                        (filepath, targetDirName))
                            shutil.copy2(filepath, targetDirName)
                        else:
                            logger.info('moving image from %s to %s' %
                                        (filepath, targetDirName))
                            shutil.move(filepath, targetDirName)
                    except:
                        logger.error('failed to copy/move %s' % filepath)
                        pass

                    break

        # no recurse, just top level dir
        if not args['-r']:
            break
