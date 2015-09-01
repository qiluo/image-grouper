# image-grouper
我只在OSX 10.10.5和Windows XP, Win7, Win10简单测试了本工具，其它系统和版本理论上也能工作，有bug的话请提交issue

Exif信息使用[exifread](https://pypi.python.org/pypi/ExifRead)读取，可能有兼容性问题，此时允许从文件最后修改时间判断

警告：请备份好文件之后再操作，本人对误操作、程序Bug造成的文件丢失不承担责任
## 用法
* 下载dist中对应平台的可执行文件，在命令行中执行
* clone本repo，安装python和依赖模块，执行

```
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
  ```

## 示例
```
# 遍历/path/to/image_source下所有文件，拷贝到/path/to/target_dir下子目录，子目录命名安装“年-月”
$ image-grouper /path/to/image_source -r -o /path/to/target_dir

# 遍历/path/to/image_source下所有文件，移动到/path/to/target_dir下子目录，子目录命名安装“年-月-日”
$ image-grouper /path/to/image_source -r -o /path/to/target_dir -f day --move

# 遍历/path/to/image_source下所有文件，只拷贝有exif信息的文件到/path/to/target_dir下子目录，子目录命名安装“年-月”
$ image-grouper /path/to/image_source -r -o /path/to/target_dir --exifonly
```

## 参数
* -o

  指定输出目录，不指定则同为源目录
* -r

  是否遍历源的子目录，不指定则默认为否
* --move

  是否移动文件，不指定则默认为拷贝文件到目标文件夹
* --exifonly

  本工具默认会从EXIF读取日期信息，如果无EXIF信息，会读取文件的修改时间。指定该选项后如果文件无EXIF信息，则跳过该文件不处理。当源目录包含非图片文件时建议指定
* -f

  指定目录名称模板。不指定则默认格式“年-月", 可以输入day，格式为"年-月-日"
* -d

  是否输出调试信息

## 感谢
* 剑英@CCF for inspiration
* [docopt](https://github.com/docopt/docopt)
* [exifread](https://pypi.python.org/pypi/ExifRead)
* [pyinstaller](http://pythonhosted.org/PyInstaller/)
* [JPG files redater by EXIF data (Python recipe)](http://code.activestate.com/recipes/550811-jpg-files-redater-by-exif-data/)
