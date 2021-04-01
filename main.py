import hashlib, sys, glob, argparse
from util import read_txt
import os

def dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"readable_dir:{path} is not a valid path")


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-path', type=dir_path)
args = parser.parse_args()



def sha1(fname):
    sha1hash = hashlib.sha1()
    with open(fname,errors='ignore') as handle: #opening the file one line at a time for memory considerations
        for line in handle:
            sha1hash.update(line.encode('utf-8'))
    return(sha1hash.hexdigest())


# files =glob.glob(r"C:\Users\alves\Documents\GRADUACAOPUC\2021_1\ENG1011 Fen trans\teste\*")
files =glob.glob(args.path+"\*")

# files = [sys.argv[1], sys.argv[2]] #these are the arguments we take
print(files)



def run():
    global files
    files_matched =[]
    files_matched_copy =[]
    contador = len(files) # repeticoes

    while (contador > 0):
        print("contagem regressiva: ", contador)
        # do stuff
        #varrer toda lista a partir do segundo item, e retirar item da lista se repetido.
        for index in range(1, len(files)):
            print("index: ", index)
            # print("files:", files)
            try:

                if sha1(files[0]) == sha1(files[index]):
                    # print('Matched',files[0], "and ",files[index])
                    # print("index do if: ", index)
                    # print("files:", files)
                    # print(files[index])
                    files_matched.append(files[0])
                    files_matched_copy.append(files[index])
                    files.pop(index)
                # else:
                #     print('Not Matched: ',files[0], "and ",files[index])
            except:
                print(" IndexError: list index out of range ")
            
        
        try:
            files.pop(0)
        except:
            print("IndexError: pop from empty list")
    

        contador-=1
    else:
        print ("end While")
        print("copy final: ",files_matched_copy)

    # file.writelines(["%s\n" % item  for item in list])


    with open('output_files_matched_copy.txt', 'a') as f1:
        f1.writelines(["%s\n" % item  for item in files_matched_copy])
    with open('output_files_matched.txt', 'a') as f2:
        f2.writelines(["%s\n" % item  for item in files_matched])

if __name__ == "__main__":
    run()
    print("start deleting from output_files_matched_copy.txt")
    for i in read_txt('output_files_matched_copy.txt'):
        os.remove(i.split('\n')[0])
    print("end")

