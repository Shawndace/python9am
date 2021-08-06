from os.path import dirname, basename, join, isfile
import glob

allfiles = glob.glob(join(dirname(__file__), '*.py'))

__all__ = [basename(file)[:-3] for file in allfiles]
