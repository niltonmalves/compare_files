
import os
def read_txt(fname):
    f = open(fname, 'r')
    content = f.readlines()
    print(content)
    return content


# for i in read_txt('output_files_matched_copy.txt'):
#     os.remove(i.split('\n')[0])


    