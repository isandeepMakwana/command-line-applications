`Python projects`
Creates a small projects for Beginners 

  ##1
    create a student Record Mangment console application . application i am used basic python like list, dict , tuples and no use any looping for search , show  , etc 
    
---
### Roll and Mobile Number Wise Student Data Store

This Python script manages student data through roll and mobile number-wise storage. It provides functionalities to add, edit, delete, search, and list student records.

#### Data Structures:
- `rollNumberWiseDataStore`: Dictionary storing student data with roll numbers as keys.
- `mobileNumberWiseDataStore`: Dictionary storing student data with mobile numbers as keys.
- `students`: List containing tuples of student data.

### Functions:

#### 1. `addStudent()`
- **Usage**: Adds a new student record to the data store.
- **Demo**:

```bash
Enter a Roll Number : 101
Enter Name : John Doe
Enter mobile Number : 1234567890
Press Save (Y/N) : Y
Student data Saved
```


#### 2. `editStudent()`
- **Usage**: Edits an existing student record.
- **Demo**:

```bash
Search By RollNumber (R) / Mobile Number (M) : ( R/M ) : R
Enter a RollNumber of Student to Search : 101
Roll Number : 101
Name : John Doe
Mobile : 1234567890
Edit (Y/N)Y
Enter a new name : John Smith
Enter a new Mobile Number 9876543210
Update (Y/N) : Y
Student updated.

```


#### 3. `deleteStudent()`
- **Usage**: Deletes an existing student record.
- **Demo**:

```bash
Delete By RollNumber (R) / Mobile Number (M) : ( R/M ) : R
Enter a RollNumber of Student to Delete : 101
Roll Number : 101
Name : John Smith
Mobile : 9876543210
Do you want to delete (Y/N)? Y
Student Deleted
```


#### 4. `searchStudent()`
- **Usage**: Searches for a student record by roll number or mobile number.
- **Demo**:

```bash
Search By RollNumber (R) / Mobile Number (M) : ( R/M ) : M
Enter mobile Number of student to search : 9876543210
Roll Number : 101
Name : John Smith
Mobile : 9876543210
press enter to continue......
```


#### 5. `displayListOfStudent()`
- **Usage**: Displays a list of all registered students with their details.
- **Demo**:

```bash
S.no   Roll_number      Name                        Mobile
1         101          John Smith                  9876543210
Press Enter to continue ...............  

```

### Usage:
Execute the script and choose options from the menu (1-6) to perform desired operations.
### Note:
Roll numbers and mobile numbers should be unique.
Input validation is implemented to ensure data integrity.
Feel free to reach out for any further assistance or clarification.
