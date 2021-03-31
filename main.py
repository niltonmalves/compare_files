import hashlib, sys, glob

files =glob.glob(r"C:\Users\alves\Documents\GRADUACAOPUC\2021_1\ENG1011 Fen trans\teste\*")

# files = [sys.argv[1], sys.argv[2]] #these are the arguments we take
print(files)
def sha1(fname):
    sha1hash = hashlib.sha1()
    with open(fname,errors='ignore') as handle: #opening the file one line at a time for memory considerations
        for line in handle:
            sha1hash.update(line.encode('utf-8'))
    return(sha1hash.hexdigest())
print('Comparing Files:',files[0],'and',files[1])
files_matched =[]
files_matched_copy =[]

if sha1(files[0]) == sha1(files[1]):
    print('Matched')
    files_matched.append(files[0])
    files_matched_copy.append(files[1])


else:
    print('Not Matched')
print("copy: ",files_matched_copy)
