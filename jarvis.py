import click 
import os
import shutil
#global variables
CurrentDirectory = os.getcwd()

def CreateController(prompt):
  objectItem = ''
  actionItem = ''
  action= ['create','new','destroy','remove','delete','recycle','move','rename','append']
  object = ['file','document','directory','folder']
  for i in prompt:
    if i in action:
      actionItem = str(action.index(i))
    if i in object:
      objectItem = str(object.index(i))
  return [actionItem,objectItem]

def PerformAction(controller):
  if controller[0] =='' or controller[1] == '':
    print("choose something else")
  else:
    if int(controller[0]) in range(0,2):
      if int(controller[1]) in range(0,2):
        CreateFile()
      else:
        CreateDirectory()
    elif int(controller[0]) in range(2,6):
      if int(controller[1]) in range(0,2):
        DeleteFile()
      else:
        DeleteDirectory()
    elif int(controller[0]) == 6:
      if int(controller[1]) in range(0,2):
        MoveFile()
      else:
        MoveDirectory()
    elif int(controller[0]) == 7:
      if int(controller[1]) in range(0,2):
        ReNameFile()
      else:
        ReNameDirectory()
    else:
      print("bad request")
    
#CreateFile()
#This will allow you to create a new file in the current directory
def CreateFile():
  print("create a new file")
  prompt = input("what is the name of your file(include extension): ")
  file = open(prompt,"w+")
  file.close()
  
  #DeleteFile()
  #This will remove a specific file from your current directory.
  #You will choose the file from a list of files, and then type it in.  You must supply the full name including extension
def DeleteFile():
  print("delete file")
  print(os.listdir("."))
  prompt = input("select a file to be delted and type it in: ")
  os.remove(prompt)

#CreateDirectory()
#This allows you to create a new directory in your current directory.  
def CreateDirectory():
  print("create directory")
  prompt = input("what is the name of your new directory: ")
  os.makedirs(os.path.join(CurrentDirectory,prompt))

#DeleteDirectory()
#Allows for you delete a given directory
#It will prompt with a list of directories for you to choose from.  Then it will ask if you truly want to delete that directory.
def DeleteDirectory():
  print("Delete Directory")
  print(os.listdir(CurrentDirectory))
  DirectoryPrompt = input("what folder would you like to delete: ")
  DeletionItem = os.path.join(CurrentDirectory,str(DirectoryPrompt))
  if os.listdir(DeletionItem) == []:
    prompt = input("are you sure you want to delete the empty folder "+DirectoryPrompt+"? This action can not be undone (yes/no): ")
    if prompt.capitalize().find("Y") == 0:
      try:
        os.rmdir(DeletionItem)
        print("Directory '%s' has been removed successfully" %DeletionItem)
      except OSError as error:
        print(error)
        print("Directory '%s' can not be removed" %DeletionItem)
    elif prompt.capitalize().find("N") == 0:
      print("don't delete me")
    else:
      print("my appologies, I did not understand your response")
  else:
    prompt = input("are you sure you want to delete the folder "+DirectoryPrompt+"?  This will delete it and all its contents.  This action can not be undone (yes/no): ")
    if prompt.capitalize().find("Y") == 0:
      try:
        shutil.rmtree(DeletionItem)
      except OSError as error:
        print(error)
        print("Directory '%s' can not be removed" %DeletionItem)
    elif prompt.capitalize().find("N") == 0:
      print("don't delete me")
    else:
      print("my appologies, I did not understand your response")

#ReName()
#Allows you to rename any given file
def ReNameFile():
  print("file rename")
  sep = "."
  print(os.listdir(CurrentDirectory))
  NewNamePrompt = ''
  OriginalPrompt = input("please choose the file that you wish to rename: ")
  if OriginalPrompt in os.listdir(CurrentDirectory):
    FileExtension = OriginalPrompt.split(sep)[1]
    NewNamePrompt = input("what is the new name for your file(DO NOT include .extension): ")
    try:
      os.rename(OriginalPrompt,NewNamePrompt+"."+FileExtension)
    except OSError as error:
      print(error)
      print("'%s' file can not be created" %NewNamePrompt)
  else:
    print(NewNamePrompt)
    NotFoundPrompt = input("it appears that your file was not found, would you like to create it instead(yes/no): ")
    if NotFoundPrompt.capitalize().find("Y") == 0:
      open(NewNamePrompt, "w+")
    elif NotFoundPrompt.capitalize().find("N") == 0:
      print("ok, maybe next time")
    else:
      print("hmmm, I didn't understand your response, please try again")

def ReNameDirectory():
  print("directory rename")
  print(os.listdir(CurrentDirectory))
  OriginalPrompt = input("please choose a folder to rename: ")
  #if os.listdir(OriginalPrompt) == []:
  NewNamePrompt = input("please enter a new name for your folder: ")
  try:
    os.rename(OriginalPrompt,NewNamePrompt)
  except OSError as error:
    print(error)
    print("we had an issue updating {} to {}." .format(OriginalPrompt, NewNamePrompt))
  #else:


#MoveFile()
#Allows you to easily move your file from one directory to another
def MoveFile():
  print("move file")
  print(os.listdir(CurrentDirectory))
  SourcePrompt = input("what file would you like to move: ")
  MoveItem = os.path.join(CurrentDirectory,str(SourcePrompt))
  DestinationPrompt = input("what is full directory that you would like to move '%s' to: " %SourcePrompt)
  shutil.move(MoveItem,DestinationPrompt)


def MoveDirectory():
  print("move directory")

def Jarvis():
  while True:
    prompt = input("how may I serve you: ")
    #prompt = "new file"
    if prompt == 'exit()':
      exit()
    promptlist = list(prompt.split(" "))
    #CreateController(promptlist)
    PerformAction(CreateController(promptlist))


if __name__ == '__main__':
  Jarvis()