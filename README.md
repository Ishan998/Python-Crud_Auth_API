# Python-Crud_Auth_API

# Technologoies Used: 
1) Python 3.115
2) Mysql Server
3) Postman Software
4) Flask Micro Web FrameWork

# Enviroment Used:
Windows 11, Visual Studio Code, Mysql Workbench ,Git

# Description:
This is an REST API Performing C.R.U.D (CREATE,READ,UPDATE,DELETE) operations also Autheticating a User using its 'Username' and 'Password'. Where it stores Data using Mysql Server ,It is designed to recieve request and get the response in JSON format as shown in the Screen screenshots using PORT : 1020. This API can Create a User with details like : Firstname. Surname, Username, Password, Address , Pincode , Phone Number , E-mail . API uses for further operations as : Updating User details , Authicating User details, Showing all Users with their details, Showing Specific user with details , Deleting a user and its details, Deleting all records in the database . Note:- This the Application is for Demo Purpose only.
** Base JSON File which will be used to get response according to the actions required with appropriate methods **
{
    "Address": "",
    "E-mail": "",
    "Firstname": "",
    "Password": "",
    "Phone Number": "",
    "Pincode": "",
    "Surname": "",
    "Username": ""
}
API as different URLs for operations like :-
1) User Create (url:  http://127.0.0.1:1020/usercerate ,METHOD ="POST")
2) User Update  (url:  http://127.0.0.1:1020/userupdate ,METHOD ="PUT")
3) Authentication of User (url:  http://127.0.0.1:1020/checkuser ,METHOD ="POST")
4) Showing all Users in Database (url:  http://127.0.0.1:1020/showalluser ,METHOD ="GET")
5) Showing Specific user (url:  http://127.0.0.1:1020/showuser ,METHOD ="GET")
6) Delete a user (url:  http://127.0.0.1:1020/deleteuser ,METHOD ="DELETE")
7) Delete all records (url:  http://127.0.0.1:1020/deletealluser ,METHOD ="DELETE")

# User HOME :

![apihome1](https://github.com/Ishan998/Python-Crud_Auth_API/assets/55241531/886205e1-bb50-4ccc-9e91-6c86fc4056f9)

# User Create :

![apiusercreate](https://github.com/Ishan998/Python-Crud_Auth_API/assets/55241531/ba1d1af0-a416-4665-aef3-5f59944952b0)

# User Update :
![userupdateshruti1](https://github.com/Ishan998/Python-Crud_Auth_API/assets/55241531/900b923c-933d-48f3-bf33-4538bc821b11)
 
![userupdated](https://github.com/Ishan998/Python-Crud_Auth_API/assets/55241531/3caf5810-769f-4344-991e-9c70bb199b39)

# Authentication Of User :

![Authticating a user](https://github.com/Ishan998/Python-Crud_Auth_API/assets/55241531/829afc3b-e8d9-4aab-8ac2-cdda9e678629)


# Showing All Users :

https://github.com/Ishan998/Python-Crud_Auth_API/assets/55241531/1c283128-0e10-4a57-a6c4-dca3fac25170

# Showing Specific User :

![show1User](https://github.com/Ishan998/Python-Crud_Auth_API/assets/55241531/192aba77-902c-4867-9322-1824f6e26edb)

# Delete a User :
![user deleted](https://github.com/Ishan998/Python-Crud_Auth_API/assets/55241531/63ef330c-7b7f-4324-bfa0-bc533ca94648)

# Delete All Records :

![all records deleted](https://github.com/Ishan998/Python-Crud_Auth_API/assets/55241531/f3de3528-63ee-4a01-b27b-41442353b920)
