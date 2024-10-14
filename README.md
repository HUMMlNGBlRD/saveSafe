# saveSafe
This is a quick and somewhat dirty scraping module intended for creating local backups of a Google Drive folder.


# Main Functionality

## download
**Outputs:** None  
**Inputs:**
- **folder_ID: str**  
  The folder ID of the Google Drive folder to download.  

Ensures that the only folder is 'backup' and then downloads the Google Drive folder.
If possible, any files that are missing their file extensions will have it regenerated via the regenerateFiletypes function.  

## backup
**Outputs:** None  
**No Inputs**

  Takes a backup of all folders that aren't the 'backup' folder and saves them in the 'backup' folder.
  If there is no 'backup' folder, one will be created.


# Sub Functionality
The module comes with a small amount of extra file management functionality

## regenerateFiletypes
**Outputs:** None  
**Inputs:**
- **files: list[str] (Optional)**  
  A list of file paths to attempt to regenerate the types of.
  If left unspecified the path argument will be used instead  
- **path: str (Optional)**  
  A path to a folder. Every file in the given folder will be tested for a unused file type.  
  If this is also left unspecified the current directory is used.  
- **out: bool (Optional)**  
  A boolean to control if the function prints the taken action for each tried file.  

Checks a given set of files or a folder for files without file extension and assigns
the correct extension if it is catalogued in the global variable 'fileTypes'.  
This function will currently break if os.open is imported

## download_folder
**Outputs:** A list with paths to all downloaded files  
**Inputs:**  
- **folder_ID: str (Optional)**
  The ID of the folder to download. If no ID is provided a default ID is used to download a degrading meme instead.  

## map_folder
**Optputs:** a list containing paths to all files that are in the given folder and its sub folders
**Inputs:**
- **Directory: str (Optional)**
  The directory to be searched. If left as None the current directory will be mapped.  

Looks through all sub folders of a directory by recursively looking for all files
contained in all entries of the given directory until there are only files left
and returns a list of all files found.  

## is_folder
**Outputs:** A boolean saying if the given directory is a folder
**Inputs:**
- **directory: str**  
  A directory to be checked  

Checks if a directory is a folder and returns a boolean.


# Extras

## Warnings

1. The 'os' module has an 'open' function which conflicts with the default 'open' function so 'os' must be imported with an alias.
