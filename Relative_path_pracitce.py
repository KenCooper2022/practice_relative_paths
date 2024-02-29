import os 
def search(file_name):
    roodir='C:\\'
    for subdir,dirs,files, in os.walk(rootdir):
        for file in files:
            if (os.path.join(subdir,file))==os.path.join(subdir,file_name):
                print('done')
                print(os.path.join(subdir,file))
                print(os.path.join(subdirs,file_name))
                relative_path = os.path.relpath(os.path.join(subdir,file),start= rootdir)
                return relative_path
    print('this should be the relative path : ',search('dummy_text.txt'))
    print('done')