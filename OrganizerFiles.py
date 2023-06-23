import os
import shutil
import time

def organizerFiles():
    downloadDir = r"C:\Users\YourUser\Downloads"

    # Dictionary mapping file extensions to folders
    fileTypes = {
        'jpg': 'images',
        'png': 'images',
        'gif': 'images',
        'doc': 'documents',
        'docx': 'documents',
        'pdf': 'documents',
        'xlsx': 'documents',
        'txt': 'documents',
        'mp4': 'videos',
        'avi': 'videos',
        'mkv': 'videos',
        'exe': 'programs',
        'msi': 'programs',
    }

    totalFiles = len(os.listdir(downloadDir))
    movedFiles = 0

    for file in os.listdir(downloadDir):
        routeFile = os.path.join(downloadDir, file)

        if os.path.isfile(routeFile):
            extension = file.split(".")[-1].lower()
            if extension in fileTypes:
                destinationDir = os.path.join(downloadDir, fileTypes[extension])
                if not os.path.exists(destinationDir):
                    os.makedirs(destinationDir)

                destinationRoute = os.path.join(destinationDir, file)
                shutil.move(routeFile, destinationRoute)
                print(f"Archivo {file} movido a {destinationRoute}")

            movedFiles += 1
            progress = movedFiles / totalFiles
            progressBar(totalFiles, movedFiles, progress)
    time.sleep(0.5)
    progressBar(totalFiles, movedFiles, 1)
    print("\n¡Tarea completada!")

def progressBar(total, current, progress):
    barLength = 50
    filledLength = int(round(barLength * progress))
    bar = '#' * filledLength + '-' * (barLength - filledLength)
    percentage = round(progress * 100, 2)
    print(f'[{bar}] {percentage}% complete ', end='\r')

# RUN
organizerFiles()