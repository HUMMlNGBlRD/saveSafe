import gdown
import os as os
from os import listdir, remove, rename, chdir, getcwd
from shutil import copy, rmtree


#TODO find out if you're using "directory correctly xD"

def backup() -> bool:
    """
    creates a backup of the downloaded folder
    Needs a downloaded folder...
    returns True if a backup was saved
    """
    rmtree("backup")
    ensure_path("backup")
    folders = get_folders_in()
    folders.remove("backup")

    if len(folders) > 0:
        files = map_folder(folders[0])
        for i in files:
            ensure_path("backup/"+get_parent_folder(i))
            copy(i,"backup/"+get_parent_folder(i))
        return True
    return False
    



def download_folder(folder_id = None) -> list:
    """
    Downloads the contents of a google drive folder.
    might make some weird shit if the given folder is already downloaded.
    """
    if folder_id==None:
        print("You need a folder ID, dumbass")
        return
    
    
    li = gdown.download_folder(id=folder_id)

    return li


def clean_download() -> bool:
    """
    Find a folder that is not the "backup" folder and deletes it
    returns True if successful
    """
    folders = get_folders_in()
    folders.remove("backup")
    if len(folders) > 0:
        rmtree(folders[0])
        return True
    return False


def regenerateFiletypes(path = None, files = None, out = False) -> None:
    """
    Checks if typeless files are from a given list of file types
    File types are stored in a tuple as (magic number, file extension, title)
    """
    fileTypes = [("PNG",".png","png"),
                 (" Ï ",".jpg","jpeg"),
                 ("PK",".docx","docs document")
                 ]
    if files == None:
        if path == None:
            files = map_folder()
        else:
            files = map_folder(path)
    
    for i in files:

        if '.' not in i:
            file_head = open(i,'r',encoding='cp850').read()[:10]
            type_found = False
            
            for j in fileTypes:
                
                if j[0] in file_head and not type_found:
                    rename(i,i+j[1])
                    if out:
                        print("found file of type \"" + j[2] + "\": " + i)
                    type_found = True

            if not type_found and out:
                print("No file type recognised for \"" + i + "\"")
        else:
            if out:
                print("\"" + i + "\" already has a file type")




def map_folder(directory = None) -> list[str]:
    """
    Returns a list of all file directories in a directory.
    Assumes the current directory if none is given.
    """
    if directory != None:
        files = [directory + "/" + i for i in listdir(directory)]
    else:
        files = listdir()
    finished = False
    while not finished:
        finished = True
        temp_files = files.copy()
        files = []
        for i in temp_files:
            try:
                directory = listdir(i)
                for j in directory:
                    files.append(i+"/"+j)
                finished = False
            except:
                files.append(i)

    return files





def is_folder(directory: str) -> bool:
    """
    Checks if a directory is a folder.
    Will return False if either the directory is not a folder or doesn't exist
    """
    try:
        listdir(directory)
        return True
    except FileNotFoundError:
        print("\"" + directory + "\" doesn't exist bud...")
        return False
    except:
        return False



def get_folders_in(directory = None) -> list[str]:
    """
    returns a list of all folders in a given folder.
    Assumes the current directory if none is given.
    """
    if directory == None:
        files = listdir()
    elif is_folder(directory):
        files = listdir(directory)
    else:
        raise NotADirectoryError("You need to give the function a directory...")

    folders = []
    for i in files:
        if is_folder(i):
            folders.append(i)
    return folders



def get_parent_folder(directory: str) -> str:
    """
    Gets the folder a specified file is in, in relation to the current directory.
    """
    split = directory.split("/")
    parent_folder = ""
    for i in split[:-1]:
        parent_folder = parent_folder+i+"/"
    return parent_folder



def ensure_path(path: str) -> bool:
    """
    Ensures that a folder exists by checking for it and creating it if it doesn't exist
    returns True if a it created a folder and False if it already existed.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    return False



def ensure_structure(paths = None) -> None:
    """
    Ensures that a certain amount of things is present in the current directory.
    edit the paths list to add new folders to the structure or parse your own list.
    """
    if paths == None:
        paths = ["backup\\"
                ]
    created = 0
    for i in paths:
        if ensure_path(i) == True:
            created += 1

    print("Folder structure ensured")
    print("created " + str(created) + " new folders")





def download(directory: str) -> None:
    """download a google drive folder, by folder ID"""
    ensure_structure()
    clean_download()
    download_folder(directory)
    regenerateFiletypes()


download('11-RjVpovhXaWv8VUhvz5asQokF9OYOIl')








































