import os
import shutil


#### Renaming the folders according to our folders dictionary only ####
def rename_folders():
    for folder in os.listdir(directory):
        if os.path.isdir(os.path.join(directory,folder)):
            os.rename(os.path.join(directory,folder),os.path.join(directory,folder.lower()))


#### Crete Folders if they are not existing ####
def create_folder(extension,file):
    flag=False
    for folder in folders:
        if '.'+extension in folders[folder]:
            if folder not in os.listdir(directory):
                os.mkdir(os.path.join(directory,folder))
            shutil.move(os.path.join(directory,file),os.path.join(directory,folder))
        flag=True

    if flag!=True:
        if miscelleaneous_folder not in os.listdir(directory):
            os.mkdir(os.path.join(directory,miscelleaneous_folder))
        shutil.move(os.path.join(directory,file),os.path.join(directory,miscelleaneous_folder))


folders={
    'audios':['.mp3','.wav'],
    'videos':['.mp4'],
    'documents':['.pdf','.xlsx','.xls','zip','.rar','.doc','.docx'],
    'images':['.png','.jpg']
    }


directory = input("Enter the full path of the folder : ")

miscelleaneous_folder = input("\nEnter the folder name for miscelleaneous files : ")

rename_folders()

all_files_list = os.listdir(directory)

for file in all_files_list:
    if os.path.isfile(os.path.join(directory,file)):
        create_folder(file.split('.')[-1],file)

print("\nFiles moved to there respective folders successfully!!")


