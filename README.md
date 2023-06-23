# ORGANIZED FILES

Small script that allows me to identify the extensions that I have in the download folder, it classifies the file if it is an image, video, document and moves it to the folder where all the documents should be.

## Used technologies

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PowerShell](https://img.shields.io/badge/PowerShell-%235391FE.svg?style=for-the-badge&logo=powershell&logoColor=white)

## Supported operating systems

![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

## Install

1 - Download the repository.

2 - Change the path to your download folder in the file **OrganizerFiles.py**.

3 - According to your operating system open the organizerFiles file with the extension .bat (windows) or .sh (linux) with a text editor.

4 - Change the path to the address where the project is downloaded.

## Run in Windows

1 - Click on the modified .bat file with the path to your download folder.

## Run in Linux

1 - After changing the address in your .sh file you must set the execution permissions with the following command:

```shell
chmod +x OrganizerFiles.sh
```

2 - Finally, you can run the .sh file using the following command:

```shell
./OrganizerFiles.sh
```

## Automatic task (Optional for Windows)

1 - Open the Task Scheduler. You can look for it in the Start menu or open it from the Control Panel.

2 - In the left navigation pane, select "Create task".

3 - In the "General" tab, assign a descriptive name to the task in the "Name" field.

4 - Go to the "Triggers" tab and click "New" to configure the task execution frequency.

5 - In the "Actions" tab, click on "New" and select "Start a program". Enter the full path to the Python interpreter followed by the full path to the Python script file you wish to run.

6 - Configure any additional options you want for the task, such as conditions and advanced settings.

7 - Click "OK" to save the scheduled task.
