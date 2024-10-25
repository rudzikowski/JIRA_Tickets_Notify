import json
import datetime
from jira import JIRA
import time
import wave
import pyaudio

#------- Configuration Global Variables ------------
added_tickets = []
jira = None
jira_email = ""
jira_token = ""
jira_project_code = ""
jira_tickets_types = []
jira_closed_statuses = []
jira_URL = ""
#-----------------------------------------------------



#-----------Definitions of script functions------------
def ReadConfigFile():
    with open('config.json', 'r') as file:
        configJson = json.load(file)
        return configJson
    
def GetScriptConfigOf(variable):
    configJson = ReadConfigFile()
    match variable:
        case "email":
            return configJson["email"]
        case "url":
            return configJson["url"]
        case "token":
            return configJson["token"]
        case "projectCode":
             return configJson["projectCode"]
        case "ticketTypesConf":
            return configJson["ticketTypesConf"]
        case "ClosedStatus":
            return configJson["ClosedStatus"]
        case _:
            return False

def LogInToJira(url,email,token):
    jira = JIRA(url,basic_auth=(email, token))
    return jira
    

def StartNewDetectCycle(): 
    try:
        added_tickets = ReadTicketsFile()
        GetRecentThreats()
        CheckTicketsStatus()
    except Exception as err:
        print("Unexpected error")
        print(err)

def CheckTicketsStatus():
    NewIssuesToCheck = ReadTicketsFile()
    if(len(NewIssuesToCheck) != 0):
        for Ticket in NewIssuesToCheck:
            try:
                issue = jira.issue(Ticket)
                issueStatus = str(issue.fields.status)
                for closedStatus in jira_closed_statuses:
                    if(issueStatus == closedStatus):
                        print(str(datetime.datetime.now()) + " - Ticket closed: " + Ticket)
                        NewIssuesToCheck.remove(Ticket)
                        WriteTicketFile(NewIssuesToCheck)
                        break
            except:
                print(str(datetime.datetime.now()) + " - " + Ticket + " ticket does not exist in the system")
                NewIssuesToCheck.remove(Ticket)
                WriteTicketFile(NewIssuesToCheck)

def ReadTicketsFile():
    with open('array.json', 'r') as file:
        array_from_file = json.load(file)
        added_tickets = array_from_file['tickets']
        return added_tickets


def WriteTicketFile(ArrayToSave):
    jsontoadd = {'tickets':ArrayToSave}
    with open('array.json','w') as file:
        json.dump(jsontoadd,file)

def GetRecentThreats():
    data = GetTicketsFromJIRA()
    for ticket in data:
        Call_notification(ticket)

def GetTicketsFromJIRA():
    return jira.search_issues('project='+ str(jira_project_code) +' AND statusCategory="To Do"', maxResults=False)

def Call_notification(ticket):
    if(str(ticket) not in added_tickets):
        added_tickets.append(str(ticket))
        WriteTicketFile(added_tickets)
        ticketType = ticket.fields.issuetype
        print(str(datetime.datetime.now()) + " - New ticket detected: " + str(ticket) + " | Ticket type: " + str(ticketType))
        Notify(str(ticketType))

def Notify(ticket_type):
    try:
        CHUNK = 1024
        fileName = str(jira_tickets_types[ticket_type]) + ".wav"
        #The part of this function responsible for playing the sound in the file was generated using ChatGPT
        with wave.open(fileName, 'rb') as wf:
            p = pyaudio.PyAudio()
            stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True)
            while len(data := wf.readframes(CHUNK)):
                stream.write(data)
            stream.close()
            p.terminate()
    except Exception as err:
        print(err)

def WelcomeBanner():
    print("""
 .-._          _,.---._    ,--.--------.  .=-.-.   _,---.                             
/==/ \\  .-._ ,-.' , -  `. \\/==/,  -   , -\\/==/_ /.-`.' ,  \\ ,--.-.  .-,--.          
|==|, \\/ /, /==/_,  ,  - \\==\\.-.  - ,-./==|, |/==/_  _.-'/==/- / /=/_ /    \\  
|==|-  \\|  |==|   .=.     |`--`\\==\\- \\  |==|  /==/-  '..-.\\==\\, \\/=/. /         
|==| ,  | -|==|_ : ;=:  - |     \\==\\_ \\ |==|- |==|_ ,    / \\==\\  \\/ -/        
|==| -   _ |==| , '='     |     |==|- | |==| ,|==|   .--'   |==|  ,_/               
|==|  /\\ , |\\==\\ -    ,_ \\/      |==|, | |==|- |==|-  |      \\==\\-, /         
/==/, | |- | '.='. -   .'       /==/ -\\/ /==/. /==/   \\      /==/._/             
`--`./  `--`   `--`--''         `--`--` `--`-``--`---'      `--`-`    """)
    
    print("---------- Script for notifying about new events in the JIRA system ----------")
    print("------------------- Version: 2.0; Author: Artur Rudzik -----------------------") 
    print("------------------------Configuration has started-----------------------------")
#-------------------------------------------------------------

# ----------The executable part of the program----------------
if __name__ == "__main__":
    WelcomeBanner()
    confStatus = False
    try:
        jira_email = GetScriptConfigOf("email")
        jira_token = GetScriptConfigOf("token")
        jira_project_code = GetScriptConfigOf("projectCode")
        jira_tickets_types = GetScriptConfigOf("ticketTypesConf")
        jira_URL = GetScriptConfigOf("url")
        jira_closed_status = GetScriptConfigOf("ClosedStatus")
        confStatus = True
        try:
            jira = LogInToJira(jira_URL,jira_email,jira_token)
        except Exception as err:
            print("Błąd połączenia z JIRA: " + str(err))
            confStatus = False
    except Exception as err:
        print("Błąd w pliku konfiguracyjnym: " + str(err))
        confStatus = False
    

    if(confStatus):
        print("----------Configuration completed successfully----------")
        print("-------------------Monitoring Started-------------------")
        print("----------" + str(datetime.datetime.now()) + "----------")
        processOngoing = True 
        while(processOngoing):
            StartNewDetectCycle()
            time.sleep(20)
    
