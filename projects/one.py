rollNumberWiseDataStore = dict()
mobileNumberWiseDataStore = dict()
students=[]

def deleteStudent():
 while True:
  deleteBy= input("Delete By RollNmber (R) / Mobile Number (M) : ( R/M )  : ")
  if deleteBy not in "mrMR":
   print("Invalid input press M or R ")
  else: break
 if deleteBy in "Rr": 
  try: 
   roll_number  = int(input("Enter a RollNumber of Student to Delete  : "))
   if roll_number <=0: raise ValueError
  except: 
   print("Invalid roll Number")
   return
  if roll_number not in rollNumberWiseDataStore:
   print("Invalid roll Number")
   return
  student =rollNumberWiseDataStore[roll_number]
 else:
  mobileNumber = input("Enter mobile Number of student to search :")
  if mobileNumber not in mobileNumberWiseDataStore: 
   print("Invalid mobile Number ")
   return
  student = mobileNumberWiseDataStore[mobileNumber]
 print(f"Roll Number : {student[0]}")
 print(f"Name : {student[1]}")
 print(f"Mobile : {student[2]}")
 while True:
  remove =input("Do you wnat to delete (Y/N)? ")
  if remove not in "ynYN":
   print("Press Y or N")
  else: break
 if remove in "nN":
  print("Student not deleted ")
  return
 rollNumberWiseDataStore.pop(student[0])
 mobileNumberWiseDataStore.pop(student[2])
 i=0
 sz=len(students)
 while i<sz:
  t=students[i]
  if t[0] == student[0] : break
  i=i+1
 students.pop(i)
 print("Student Deleted")
 

def searchStudent():
 while True:
  searchBy= input("Search By RollNmber (R) / Mobile Number (M) : ( R/M )  : ")
  if searchBy not in "mrMR":
   print("Invalid input press M or R ")
  else: break
 if searchBy in "Rr": 
  try: 
   roll_number  = int(input("Enter a RollNumber of Student to Search  : "))
   if roll_number <=0: raise ValueError
  except: 
   print("Invalid roll Number")
   return
  if roll_number not in rollNumberWiseDataStore:
   print("Invalid roll Number")
   return
  student =rollNumberWiseDataStore[roll_number]
  print(f"Roll Number : {student[0]}")
  print(f"Name : {student[1]}")
  print(f"Mobile : {student[2]}")
  input("press enter to Continue...... ")
 else:
  mobileNumber = input("Enter mobile Number of student to search :")
  if mobileNumber not in mobileNumberWiseDataStore: 
   print("Invalid mobile Number ")
   return
  student = mobileNumberWiseDataStore[mobileNumber]
  print(f"Roll Number : {student[0]}")
  print(f"Name : {student[1]}")
  print(f"Mobile : {student[2]}")
  input("press enter to Continue...... ")

def editStudent():
 while True:
  searchBy= input("Search By RollNmber (R) / Mobile Number (M) : ( R/M )  : ")
  if searchBy not in "mrMR":
   print("Invalid input press M or R ")
  else: break
 if searchBy in "Rr": 
  try: 
   roll_number  = int(input("Enter a RollNumber of Student to Search  : "))
   if roll_number <=0: raise ValueError
  except: 
   print("Invalid roll Number")
   return
  if roll_number not in rollNumberWiseDataStore:
   print("Invalid roll Number")
   return
  student =rollNumberWiseDataStore[roll_number]
 else:
  mobileNumber = input("Enter mobile Number of student to search :")
  if mobileNumber not in mobileNumberWiseDataStore: 
   print("Invalid mobile Number ")
   return
  student = mobileNumberWiseDataStore[mobileNumber]
 print(f"Roll Number : {student[0]}")
 print(f"Name : {student[1]}")
 print(f"Mobile : {student[2]}")
 while True:
  edit=input("Edit (Y/N)")
  if edit not in "yYnN":
   print("Invalid input , press Y or N ")
  else : break
 if edit not in "yY":
  print("Student not edited ")
  return
 name =input("Enter a new name  : ")
 mobileNumber= input("Enter a new Mobile Number ")
 otherMobile=0
 if mobileNumber!=student[2]:
  otherMobile=student[2]
  if mobileNumber in mobileNumberWiseDataStore:
   print(f"{mobileNumber} has been alloted by {mobileNumberWiseDataStore[mobileNumber][1]}")
   return
 update =input("Update (Y/N) :")
 while True: 
  if update not in "yYnN":
   print("Invalid input , press Y or N ")
  else : break
 if update in "yY":
  student =(student[0],name ,mobileNumber)
  rollNumberWiseDataStore[student[0]]=student
  mobileNumberWiseDataStore[mobileNumber]=student
  if otherMobile!=0:
   del mobileNumberWiseDataStore[otherMobile] 
  i=0
  while i<len(students):
   t=students[i]
   if t[i]==students[i][0]:
    students[i]=student
    break
   i=i+1
  print("Student updated . ") 


def addStudent():
 try:
  rollNumber = int(input("Enter a Roll Number :"))
  if rollNumber<0 : raise ValueError
 except:
  print(f"Invalid roll Number ")
  return
 if rollNumber in rollNumberWiseDataStore : 
  print(f"{rollNumber} has been alloted by {rollNumberWiseDataStore[rollNumber][1]}")
  return
 name = input("Enter Name : ")
 mobileNumber=input("Enter mobile Number :")
 validSet =set("0123456789")
 mobSet = set(mobileNumber)
 valid = mobSet-validSet
 if len(valid)>1:
  print("Invalid Mobile Number")
  return
 if mobileNumber in mobileNumberWiseDataStore:
  print(f"{mobileNumber} has been alloted by {mobileNumberWiseDataStore[mobileNumber][1]}")
  return

 while True: 
  save = input("Press Save (Y/N) : ")
  if save not in "yYnN":
   print("Press (Y/N)")
   continue
  else: break

 if save in "yY":
  student = (rollNumber , name , mobileNumber)
  rollNumberWiseDataStore[rollNumber]=student
  mobileNumberWiseDataStore[mobileNumber]=student
  students.append(student)
  print("Student data Saved ")
 else :
  print("Data not Saved") 
 
def displayListOfStudent():
 if len(students)<1:
  print("no students are registered")
  return
 line="-"*68
 newPage=True
 pageSize=3
 sno=0
 for student in students:
  if newPage:
   print(line)
   print("S.no".center(10," "),"Roll_number".center(10," "),"Name".ljust(30," "),"Mobile".ljust(15," ")) 
   print(line)
   newPage=False
  sno+=1
  (roll_number , name ,mobile_number)=student
  recordLine = "%10d %10d %-30s %-15s " %(sno , roll_number , name , mobile_number)
  print(recordLine)
#  print(sno.center(10," "),roll_number.center(10," "),name.ljust(30," "),mobile_number.ljust(15," ")) 
  if sno%pageSize==0 or len(students)==sno:
   newPage=True
   print(line)
   input("Press Enter to continue ...............")



while True:
 print("1 . Add")
 print("2 . Edit")
 print("3 . Delete")
 print("4 . Search")
 print("5 . List")
 print("6 . Exit")
 
 try:
  choice =int(input("Enter your Choice (1 - 6 ) : "))
  if choice<1 or choice>6 : raise ValueError
 except:
  print("Invalid Choice ")
  continue
 if choice ==1: addStudent()
 if choice ==2: editStudent()
 if choice ==3: deleteStudent()
 if choice ==4: searchStudent()
 if choice ==5: displayListOfStudent()
 if choice ==6: break