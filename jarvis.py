import click 
import os
import shutil
#action= ['create','new',update','move','destroy','recycle','append']
#object = ['file','directory','document','folder']
def CreateController(prompt):
  objectItem = ''
  actionItem = ''
  action= ['create','new','destroy','remove','delete','recycle','move','update','append']
  object = ['file','document','directory','folder']
  for i in prompt:
    if i in action:
      actionItem = str(action.index(i))
    if i in object:
      objectItem = str(object.index(i))
  return [actionItem,objectItem]

def PerformAction(controller):
  if controller[0] =='' and controller[1] == '':
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
    elif int(controller[0]) == 5:
      if int(controller[1]) in range(0,2):
        MoveFile()
      else:
        MoveDirectory()
    else:
      print("bad request")
    

def CreateFile():
  print("create a new file")
  #prompt = input("what is the name of your file(include extension): ")
  #file = (prompt,'w+')
  
  #DeleteFile()
  #This will remove a specific file from your current directory.
  #You will choose the file from a list of files, and then type it in.  You must supply the full name including extension
def DeleteFile():
  print("delete file")
  print(os.listdir("."))
  prompt = input("select a file to be delted and type it in: ")
  os.remove(prompt)

def UpdateFile():
  print("append file")

#CreateDirectory()
#This allows you to create a new directory in your current directory.  
def CreateDirectory():
  print("create directory")
  prompt = input("what is the name of your new directory: ")
  CurrentDirectory = os.getcwd()
  os.makedirs(os.path.join(CurrentDirectory,prompt))

def DeleteDirectory():
  CurrentDirectory = os.getcwd()
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
      print("dont delete me")
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
      print("dont delete me")
    else:
      print("my appologies, I did not understand your response")

  print("delete directory")

def MoveDirectory():
  print("move directory")


def Jarvis():
  while True:
    prompt = input("how may I serve you: ")
    #prompt = "new file"
    if prompt == 'exit()':
      exit()
    promptlist = list(prompt.split(" "))
    PerformAction(CreateController(promptlist))


if __name__ == '__main__':
  Jarvis()