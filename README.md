# JIRA NOTIFY
Open-source tool for creating sound notifications
each time a new TO DO ticket is detected on the JIRA project board.
This tool is universal, and works for any type of project.

## AUTHOR 
#### Artur Rudzik
- [LINKEDIN](https://www.linkedin.com/in/artur-rudzik/)
- [GITHUB](https://github.com/rudzikowski/)
## CONFIGURATION
### SOUND FILES
Prepare sound files with the .wav extension that you want to play when the script detects a new ticket. 
Place the files in the same folder as the script.

### CONFIG FILE
Complete the `config.json` file as follows:

```JSON
{
  "url": "https://your-jira-instance.atlassian.net",
  "email": "your_email@example.com",
  "token": "your_authentication_token",
  "projectCode": "YOUR_PROJECT_CODE",
  "ticketTypesConf": {
    "Bug": "bug_sound",
    "Task": "task_sound",
    "Story": "story_sound"
  },
  "ClosedStatus": ["Closed","Done","Complited"]
}
```

- "url": - enter url to your JIRA service.
- "email": - enter your user email.
- "token": - enter your authentication token.
- "projectCode": - enter code of your jira project.
- "ticketTypesConf": - Enter the names of the ticket types in the dictionary, along with the name of the audio file (without the .wav extension),
        that you want to play when a new ticket arrives. The number of types is unlimited. Example: {"example1":"sound1","example2":"sound2"}. You 
        can also use one sound to all of the types by entering the same name.
- "ClosedStatus": - Enter what text define "DONE" status in your JIRA project, it might be a few of words, thats why you are able to enter it inside the array.
    
### LAST CHECK
Make sure the following are in the same folder as the script you are running:
1. config.json file completed correctly,
1. array.json file,
1. .wav files whose names are entered into the configuration file.

# MAKE EXE FILE
If you want to quick run this script without console writing.
Do this steps to export it to exe file:
1. Install pyinstaller library: `pip install pyinstaller`
1. Type this command in the script folder: `pyinstaller -F tickets_notification.py`
1. Wait until the end of export process and then move exe file from dist folder to main directory with all configuration files.
1. Run script whenever you need to by starting `tickets_notification.exe`



## LIBRARIES
This script uses the following libraries:
- [json](https://docs.python.org/3/library/json.html)
- [datetime](https://docs.python.org/3/library/datetime.html)
- [JIRA](https://jira.readthedocs.io/)
- [waves](https://docs.python.org/3/library/time.html)
- [pyaudio](https://pypi.org/project/PyAudio/)

## TERMS OF USE
The program is free and open source. If you would like to support the author by writing a post on Linkedin about my code. 
I would be very grateful for such feedback. Please tag me in the post right [here](https://www.linkedin.com/in/artur-rudzik/)
    
