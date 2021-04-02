import hashlib, sys, glob, argparse
import os

def read_txt(fname):
    f = open(fname, 'r')
    content = f.readlines()
    print(content)
    return content

def sha1(fname):
    sha1hash = hashlib.sha1()
    with open(fname,errors='ignore') as handle: #opening the file one line at a time for memory considerations
        for line in handle:
            sha1hash.update(line.encode('utf-8'))
    return(sha1hash.hexdigest())


def look_files(path):
    list_files = glob.glob(path+"\*")
    return list_files
    