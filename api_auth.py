from flask import Flask,request
import json
from auth_db import authdb as t

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    response_home={ "Firstname":"","Surname":"","Username":"","Password":"","Address":"","Pincode":"",
                   "Phone Number":"","E-mail":""}
    return response_home

@app.route('/usercreate',methods=['POST'])
def create():
    # required is name, surname, username, address, pincode, phone number, e-mail,Password
    try:
        res=request.json
        # a=0
        sn=None
        fn=None
        ad=None
        unh=None
        pint=0
        pasw=None
        Pnu=0
        mal=None
        for key,value in list(res.items()):
            if key=="Firstname":
                    fn=value
            if key=="Surname":
                sn=value
            if key=="Username":
                unh=value
            if key=="Address":
                ad=value
            if key=="Pincode":
                pint=value
            if key=="Phone Number":
                Pnu=value 
            if key=="E-mail":
                mal=value 
            if key=="Password":
                pasw=value    
        save=t().createuser(fname=fn,surname=sn,addr=ad,pinc=pint,uname=unh,paswd=pasw,Pnumber=Pnu,mail=mal)
        if save:
            res.update({'operation':'user created'})
        else:
            res.update({'operation':'user not created'})
        pp=json.dumps(res)
        return pp
    except IOError:
        return Exception

@app.route('/userupdate',methods=['POST'])
def update():
    try:
        res=request.json
        ids=0
        sn=None
        fn=None
        ad=None
        unh=None
        pint=0
        pasw=None
        Pnu=0
        mal=None
        for key,value in list(res.items()):
            if key=="id":
                    # if value!=None:
                        ids=value 
            if key=="Firstname":
                    # if value!=None:
                        fn=value
            if key=="Surname":
                # if value!=None:
                        sn=value
            if key=="Username":
                # if value!=None:
                        unh=value
            if key=="Address":
                # if value!=None:
                        ad=value
            if key=="Pincode":
                # if value!=0:
                        pint=value
            if key=="Phone Number":
                # if value!=0:
                        Pnu=value 
            if key=="E-mail":
                # if value!=None:
                        mal=value 
            if key=="Password":
                # if value!=None:
                        pasw=value    
        save=t().updateuser(id=ids,fname=fn,surname=sn,addr=ad,pinc=pint,uname=unh,paswd=pasw,Pnumber=Pnu,mail=mal)
        if save:
            res.update({'operation':'user details updated'})
        else:
            res.update({'operation':'user details not updated'})
        pp=json.dumps(res)
        return pp
    except IOError:
        return Exception

@app.route('/deleteuser',methods=['DELETE'])
def deluser():
    res=request.json
    for key,value in list(res.items()):
        if key=="Username":
            yu=t().deleteuser(uname=value)
            if yu:
                res.update({'status':'Deleted successfully'})
            else:
                res.update({'status':'Operation unsuccesfull'})
        else:
             res.update({'status':'Username Not Found'})
    pp=json.dumps(res)
    return pp

@app.route('/showalluser',methods=['GET'])
def alluser():
    try:
        res=request.json
        yu=t().readalluser()
        p=[]
        res={}
        data=['id','Firstname','Surname','Address','Pincode','Username','Password','Phone Number','E-mail']
        for i in yu:
            res = {data[j]: i[j] for j in range(len(i))}        
            p.append(res)
        pp=json.dumps(p)
        return pp
    except IOError:
        return Exception
    
@app.route('/showuser',methods=['GET'])
def showuser():
    p=[]
    rest={}
    res=request.json
    for key,val in list(res.items()):
        if key=="Username":
            yu=t().readuser(uname=val)
            data=['id','Firstname','Surname','Address','Pincode','Username','Password','Phone Number','E-mail']
            for i in yu:
                rest = {data[j]: i[j] for j in range(len(i))}        
                p.append(rest)
    pp=json.dumps(p)
    return pp
    

@app.route('/deletealluser',methods=['DELETE'])
def deleteall():
    res=request.json
    for key,val in list(res.items()):
        if key =="trigger delete all":
            if val=="True":
                yu=t().deletealluser()
                if yu:
                    res.update({'status':'All records Deleted successfully'})
                else:
                    res.update({'status':'operation unsuccesfull'})
            else:
                 res.update({'status':'operation untriggered'})
        else:
             res.update({'status':'trigger delete all not Found'})
    pp=json.dumps(res)
    return pp

@app.route('/checkuser',methods=['GET'])
def authUser():
    res=request.json
    un=None
    pas=None
    for key,val in list(res.items()):
        if key =="Username":
            un=val
        if key=="Password":
            pas=val
        yu=t().auth_user(uname=un,passd=pas)
        if yu:
            res.update({'status':'Success'})
        else:
            res.update({'status':'Failed'})
    pp=json.dumps(res)
    return pp

if __name__=="__main__":
    app.debug=True
    app.run(port=1020)