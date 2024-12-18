
      _ ___ ____      _      _   _  ___ _____ ___ _______   __
     | |_ _|  _ \    / \    | \ | |/ _ \_   _|_ _|  ___\ \ / /
  _  | || || |_) |  / _ \   |  \| | | | || |  | || |_   \ V / 
 | |_| || ||  _ <  / ___ \  | |\  | |_| || |  | ||  _|   | |  
  \___/|___|_| \_\/_/   \_\ |_| \_|\___/ |_| |___|_|     |_|  
                                                              
README
    JIRA NOTIFY - is an open-source tool for creating sound notifications
    each time a new TO DO ticket is detected on the JIRA project board.
    This tool is universal, and works for any type of project.

LIBRARIES
    This script uses the following libraries:
        json - https://docs.python.org/3/library/json.html
        datetime - https://docs.python.org/3/library/datetime.html
        JIRA - https://jira.readthedocs.io/
        waves - https://docs.python.org/3/library/time.html
        pyaudio - https://pypi.org/project/PyAudio/

TERMS OF USE
    The program is free and open source. If you would like to support the author by writing a post on Linkedin about my code. 
    I would be very grateful for such feedback. Please tag me in the post(https://www.linkedin.com/in/artur-rudzik/)

AUTHOR
      Artur Rudzik - 
        LINKEDIN: https://www.linkedin.com/in/artur-rudzik/
        GITHUB: https://github.com/rudzikowski/

SOURCE CODE
      https://github.com/rudzikowski/JIRA_Tickets_Notify/


CONFIGURATION
    PREPARATION
    1. SOUND FILES
        Prepare sound files with the .wav extension that you want to play when the script detects a new ticket. 
        Place the files in the same folder as the script.

    2. CONFIG FILE
        Complete the config.json file as follows:

        "url": - enter url to your JIRA service.
        "email": - enter your user email.
        "token": - enter your authentication token.
        "projectCode": - enter code of your jira project.
        "ticketTypesConf": - Enter the names of the ticket types in the dictionary, along with the name of the audio file (without the .wav extension),
        that you want to play when a new ticket arrives. The number of types is unlimited. Example: {"example1":"sound1","example2":"sound2"}. You can also use one sound to all of the types by entering the same name.
        "ClosedStatus": - Enter what text define "DONE" status in your JIRA project.
    
    3. LAST CHECK
        Make sure the following are in the same folder as the script you are running:
        1. config.json file completed correctly,
        2. array.json file,
        3. .wav files whose names are entered into the configuration file.
