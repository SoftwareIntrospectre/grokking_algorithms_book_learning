from os import listdir
from os.path import isfile, join, dirname, abspath, splitext

def recursive_printnames(dir):

    # search for files until no sub-directories remain. Print files with file extensions
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)
        if isfile(fullpath):
            root, ext = splitext(file)
            if ext:
                print(file)

        else:

            # recursively look for directories and files
            recursive_printnames(fullpath)

current_dir = dirname(abspath(__file__))
two_levels_up_start_dir = abspath(join(current_dir, '..', '..'))

recursive_printnames(two_levels_up_start_dir)