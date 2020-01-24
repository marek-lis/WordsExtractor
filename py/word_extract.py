from words_extractor import Words_Extractor
from disk_scanner import *

print("Extract words from text files in input directory.")

files = scan_tree_for_files('./input')

print("Found %d files." % (len(files)))

extractor = Words_Extractor()

[extractor.extract(file, './output' +
                   get_relative_path(file, './input/')) for file in files]
