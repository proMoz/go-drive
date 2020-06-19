import sys
import os
from google_drive.upload import upload_file

args = sys.argv
main_path =  os.path.dirname(os.path.abspath(__file__))
files_path = os.path.join(main_path, "files")
if("-f" in args):
    file_indx = args.index("-f") + 1
    for i in range( file_indx , len(args) ):
        file = os.path.join(main_path, os.path.normpath(args[i]))
        print(file)
        # upload_file(file, "1nNosPm3SFXWEjv4Vxlv65XS0sxwbOcaN")
else:
    print("no file seletecd with -f \n uploading all files in folder filles if exsite")
    files = os.listdir(files_path)
    for file in files:
        print(os.path.join(files_path, file))
        # upload_file(file, "1nNosPm3SFXWEjv4Vxlv65XS0sxwbOcaN")


