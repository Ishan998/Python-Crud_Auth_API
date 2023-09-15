import mysql.connector as con

class authdb:
    def __init__(self):
        self.host="127.0.0.1"
        self.user="root"
        self.password="root"
        self.database="userAuth"
        
    def connection(self):
        try:
            self.g=con.connect(host=self.host,user=self.user,password=self.password,database=self.database)
            self.cur=self.g.cursor()
            return True
        except IOError:
            return Exception
    def createtable(self):
        if self.connection():
            cmd=f"CREATE TABLE UserAuth( ID int AUTO_INCREMENT PRIMARY KEY,FirstName varchar(255),LastName varchar(255) NOT NULL,Address varchar(255),pincode int,Username varchar(255),Password varchar(255),phoneNumber int, Email varchar(255))"
            try:
                self.cur.execute(cmd)

                return True
            except IOError:
                return Exception
        else:
            return ConnectionAbortedError

    def createuser(self,fname,surname,addr,pinc,uname,paswd,Pnumber,mail):
        if self.connection():
            val=(fname,surname,addr,pinc,uname,paswd,Pnumber,mail)
            qr="INSERT INTO UserAuth(Firstname,Lastname,Address,pincode,Username,Password,phoneNumber,Email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            try:
                self.cur.execute(qr,val)
                self.g.commit()
                return True
            except IOError:
                return Exception
        else:
            return ConnectionAbortedError
        
    def updateuser(self,id,fname,surname,addr,pinc,uname,paswd,Pnumber,mail):
        if self.connection()==True:
            sn=None
            fn=None
            ad=None
            unh=None
            pint=0
            pasw=None
            Pnu=0
            mal=None
            try:
                if surname!=None:
                    sn=surname
                else:
                    return False
                if fname!=None:
                    fn=fname
                if pinc!=0:
                    pint=pinc
                if addr!=None:
                    ad=addr
                if uname!=None:
                    unh=uname
                if paswd!=None:
                    pasw=paswd
                if Pnumber!=0:
                    Pnu=Pnumber
                if mail!=None:
                    mal=mail
                cmd=(f"update UserAuth set FirstName='{fn}',LastName='{sn}',Address='{ad}',pincode={pint},Username='{unh}',Password='{pasw}',phoneNumber={Pnu},Email='{mal}' where ID={id}")
                self.cur.execute(cmd)
                self.g.commit()
                return True
            except IOError:
                return Exception
        else:
            return ConnectionAbortedError
        
    def readuser(self,uname):
        if self.connection()==True:
            ad=self.g.cursor()
            try:
                t=ad.execute(f"Select * from UserAuth where Username='{uname}'")
                y=ad.fetchall()
                return y
            except IOError:
                return Exception
        else:
            return ConnectionAbortedError
        
    def readalluser(self):
        if self.connection()==True:
            ad=self.g.cursor()
            try:
                ad.execute("Select * from UserAuth")
                y=ad.fetchall()
                return y
            except IOError:
                return Exception
        else:
            return ConnectionAbortedError
        
    def deleteuser(self,uname):
        if self.connection()==True:
            ad=self.g.cursor()
            try:
                op=None
                ad.execute(f"SELECT ID from UserAuth where Username='{uname}'")
                op=ad.fetchone()
                # print(op[0])
                if op!=None:
                    for i in op:
                        if i!=0:  
                            cmd=(f"delete from UserAuth where Username='{uname}'")
                            ad.execute(cmd)
                            self.g.commit()
                            # y=ad.fetchall()
                            return True
                        else:
                            return False
                else:
                    return False
            except IOError:
                return Exception
        else:
            return ConnectionAbortedError
        
    def deletealluser(self):
        if self.connection()==True:
            ad=self.g.cursor()
            try:
                ad.execute("DELETE from UserAuth")
                self.g.commit()
                print("DELETED")
                return True
            except IOError:
                return Exception
        else:
            return ConnectionAbortedError
        
    def deletable(self):
        if self.connection()==True:
            ad=self.g.cursor()
            try:
                ad.execute("DROP TABLE UserAuth")
                self.g.commit()
                print("DELETED")
                return True
            except IOError:
                return Exception
        else:
            return ConnectionAbortedError

    def auth_user(self,uname,passd):
        if self.connection()==True:
            ad=self.g.cursor()
            if uname!=None and passd!=None:
                try:
                    ad.execute(f"SELECT Password from UserAuth where Username='{uname}'")
                    check=ad.fetchone()
                    check2=check
                    print(check)
                    for i in check2:
                        # print(type(i))
                        if passd==i:
                            return True
                        else:
                            return False
                except IOError:
                    return Exception
            else:
                return False
        else:
            return ConnectionAbortedError

if __name__=="__main__":
    au=authdb()
    # p=au.deletealluser()
    # p=au.createtable()
    # p=au.deletable()
    # p=au.readalluser()
    # p=au.readuser(uname="ShrutiNK05")
    p=au.deleteuser(uname="Sheetal.kumar03")
    # p=au.auth_user(uname="varunHample03",passd="test@123")
    # p=au.auth_user(uname="Aman.Trivedi)3",passd="test@123")
  
    # p=au.createuser(fname='Varun',surname='hample',addr="hill top near sarana road solan himanchal pradesh",
    #                     pinc=440102,uname="varunHample03",paswd="test@123",Pnumber=1234567890,mail="varun.hample03@gmail.com")
    print(p)
    # print(au.createtable())