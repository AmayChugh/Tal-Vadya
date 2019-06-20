from flask import Flask,render_template,request
from werkzeug.datastructures import ImmutableMultiDict
from itertools import permutations
import random 
import sqlite3
taal_dict={
    '1':'Dhaa',
    '2':'Dhin',
    '3':'Ga',
    '4':'Ka',
    '5':'Kat',
    '6':'Naa',
    '7':'Na',
    '8':'Taa',
    '9':'Tak',
    '10':'Tee',
    '11':'TiraKita',
    '12':'Tita',
    '13':'Tin',
    '14':'Too'
}
app = Flask(__name__)
@app.route('/register',methods = ['POST', 'GET'])
def register():
    def create_table():
        c.execute("CREATE TABLE IF NOT EXISTS Registered_Users(NAME TEXT, EMAIL TEXT,PASSWORD TEXT)")
    def data_entry(name,email,password):
        c.execute("INSERT INTO Registered_Users (NAME, EMAIL, PASSWORD) VALUES (?, ?, ?)",
            (name, email, password))
        conn.commit()
        c.close()
        conn.close()
    if request.method == 'POST' :
        name= request.form['namevar']
        email=request.form['emailid']
        password=request.form['passwd']
        conn = sqlite3.connect('registrations.db')
        c = conn.cursor()
        create_table()
        data_entry(name,email,password)
    return render_template("register.html")

@app.route("/login",methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        email_id=request.form['emailid']
        password=request.form['password']
        conn = sqlite3.connect('registrations.db')
        c = conn.cursor()
        def read_from_db(email):
            users=[]
            c.execute('SELECT * FROM Registered_Users WHERE EMAIL = ?',(email,))
            data = c.fetchall()
            for row in data:
                users.append(row)
            return users
        users_list=read_from_db(email_id)
        if users_list == []:
            return render_template("login.html",msg=str("User not found!"))
        else:
            if password == users_list[0][2]:
                return render_template("login.html",msg=str("Login Successful!"))
            else:
                return render_template("login.html",msg=str("Password Incorrect"))
        c.close()
        conn.close()
    return render_template("login.html",msg=str(""))
@app.route("/home")
def home():
    return render_template("page2.html")
@app.route("/taal")
def taal():
    return render_template("page3.html")
@app.route("/taal/teentaal")
def teentaal():
    return render_template("page4.html")
@app.route("/taal/ektaal")
def ektaal():
    return render_template("ektaal.html")
@app.route("/taal/jhaptaal")
def jhaptaal():
    return render_template("jhaptaal.html")
@app.route("/taal/keherwa")
def keherwa():
    return render_template("keherwa.html")
@app.route("/taal/dadra")
def dadra():
    return render_template("dadra.html")
@app.route("/taal/rupak")
def rupak():
    return render_template("rupak.html")
@app.route("/types")
def types():
    return render_template("types.html")
@app.route("/types/6beats")
def _6beats():
    return render_template("6beats.html")
@app.route("/types/8beats")
def _8beats():
    return render_template("8beats.html")
@app.route("/types/10beats")
def _10beats():
    return render_template("10beats.html")
@app.route("/types/12beats")
def _12beats():
    return render_template("12beats.html")
@app.route("/types/16beats")
def _16beats():
    return render_template("16beats.html")

@app.route("/tihai")
def tihai():
    return render_template("tihai.html")

@app.route('/tihai/resulttihai',methods = ['POST', 'GET'])
def resulttihai():
    root = ['Dha' ,'Dhin' ,'Dhin', 'Dha', 'Dha', 'Dhin' ,'Dhin', 'Dha', 'Dha' ,'Tin' ,'Tin', 'Ta', 'Ta' ,'Dhin' ,'Dhin' ,'Dha']
    global taal_dict
    print("Hell-o")
    if request.method == 'POST' or request.method == 'GET':
        program_input="" 
        result = request.form
        print("Hello World")
        print(result)
        program_input+=taal_dict[result['beat1']]+" "
        program_input+=taal_dict[result['beat2']]+" "
        program_input+=taal_dict[result['beat3']]+" "
        program_input+=taal_dict[result['beat4']]+" "
        program_input+=taal_dict[result['beat5']]
        program_input = list(program_input.split(" "))
        size=(len(root)+2)//3
        first_letter = root[0]
        space = " "
        replacement_words=program_input
        replacement_length=size-2
        permutations_list=list(permutations(replacement_words,replacement_length))
        no=0
        res=[]
        for i in permutations_list:
            string=' '.join(i)
            string = string + ' '+first_letter +' '+ 'Pause '
            string=string*3
            string=list(map(str,string.split()))
            string=string[:-2]
            string=' '.join(string)
            res.append(string)
            no+=1
        x=len(res)
        return render_template("resulttihai.html",res=res,x=x)
    return "Hello W"

@app.route('/types/result10',methods = ['POST', 'GET'])
def result10():
    theka = ['Dhi','Na','Dhi','Dhi','Na','Ti','Na','Dhi','Dhi','Na']
    global taal_dict
    print("Hell-o")
    if request.method == 'POST' or request.method == 'GET':
        program_input="" 
        result = request.form
        print("Hello World")
        print(result)
        program_input+=taal_dict[result['beat1']]+" "
        program_input+=taal_dict[result['beat2']]+" "
        program_input+=taal_dict[result['beat3']]+" "
        program_input+=taal_dict[result['beat4']]
        program_input = list(program_input.split(" "))
        res=[]
        for i in program_input:
            for j in program_input:
                for k in program_input:
                    for l in program_input:
                        theka[1]=i
                        theka[4]=j
                        theka[6]=k
                        theka[9]=l
                        new=[]
                        for x in theka:
                            if theka.index(x)==1 or theka.index(x)==4 or theka.index(x)==6 or theka.index(x)==9:
                                print(x," | ",end=" ")
                                new.append(x)
                                new.append('|')
                            else:
                                print(x,end=" ")
                                new.append(x)
                            print()
                        res.append(new)    
        return render_template("result10.html",res=res)
    return "Hello W"



@app.route('/laykari/resultdugun',methods = ['POST', 'GET'])
def resultdugun():
    print("Hell-o")
    if request.method == 'POST' or request.method == 'GET':
            program_input="" 
            result = request.form
            print("Hello World")
            print(result)
            program_input+=result['beat1']+" "
            program_input+=result['beat2']+" "
            program_input+=result['beat3']+" "
            program_input+=result['beat4']+" "
            program_input+=result['beat5']+" "
            program_input+=result['beat6']+" "
            program_input+=result['beat7']+" "
            program_input+=result['beat8']+" "
            program_input+=result['beat9']+" "
            program_input+=result['beat10']+" "
            program_input+=result['beat11']+" "
            program_input+=result['beat12']+" "
            program_input+=result['beat13']+" "
            program_input+=result['beat14']+" "
            program_input+=result['beat15']+" "
            program_input+=result['beat16']
            program_input = list(program_input.split(" "))
            print(program_input)  
            taal=program_input
            taal = taal+taal
            mukh=[]
            i=0
            while (i<len(taal)):
                mukh.append(taal[i]+taal[i+1])
                i=i+2
            print(mukh)
            return render_template("resultdugun.html",res=mukh)
    return "Hello W"

@app.route('/laykari/resulttigun',methods = ['POST', 'GET'])
def resulttigun():
    print("Hell-o")
    if request.method == 'POST' or request.method == 'GET':
            program_input="" 
            result = request.form
            print("Hello World")
            print(result)
            program_input+=result['beat1']+" "
            program_input+=result['beat2']+" "
            program_input+=result['beat3']+" "
            program_input+=result['beat4']+" "
            program_input+=result['beat5']
            program_input = list(program_input.split(" "))
            print(program_input)  
            taal=program_input
            taal = taal+taal+taal
            mukh=[]
            i=0
            while (i<len(taal)):
                mukh.append(taal[i]+taal[i+1]+taal[i+2])
                i=i+3
            print(mukh)
            return render_template("resulttigun.html",res=mukh)
    return "Hello W"



@app.route('/laykari/resultchaugun',methods = ['POST', 'GET'])
def resultchaugun():
    print("Hell-o")
    if request.method == 'POST' or request.method == 'GET':
            program_input="" 
            result = request.form
            print("Hello World")
            print(result)
            program_input+=result['beat1']+" "
            program_input+=result['beat2']+" "
            program_input+=result['beat3']+" "
            program_input+=result['beat4']+" "
            program_input+=result['beat5']+" "
            program_input+=result['beat6']+" "
            program_input+=result['beat7']+" "
            program_input+=result['beat8']+" "
            program_input+=result['beat9']+" "
            program_input+=result['beat10']+" "
            program_input+=result['beat11']+" "
            program_input+=result['beat12']+" "
            program_input+=result['beat13']+" "
            program_input+=result['beat14']+" "
            program_input+=result['beat15']+" "
            program_input+=result['beat16']
            program_input = list(program_input.split(" "))
            print(program_input)  
            taal=program_input
            taal = taal+taal+taal+taal
            mukh=[]
            i=0
            while (i<len(taal)):
                mukh.append(taal[i]+taal[i+1]+taal[i+2]+taal[i+3])
                i=i+4
            print(mukh)
            return render_template("resultchaugun.html",res=mukh)
    return "Hello W"



@app.route('/types/result8',methods = ['POST', 'GET'])
def result8():
    theka = ['Dhaa','Ga','Na','Tin','Na','Ka','Dhin','Na']
    global taal_dict
    print("Hell-o")
    if request.method == 'POST' or request.method == 'GET':
        program_input="" 
        result = request.form
        print("Hello World")
        print(result)
        program_input+=taal_dict[result['beat1']]+" "
        program_input+=taal_dict[result['beat2']]
        print(program_input)
        program_input = list(program_input.split(" "))
        permlist = []
        for i in theka:
            permlist.append(i)
        for i in program_input:
            if i not in permlist:
                permlist.append(i)
        print(permlist)
        print()
        res=[]
        for i in range(12000):
            permut=[]
            new=[]
            permut=random.sample(permlist,8)
            for i in range(8):
                if ((i+1)%4 == 0):
                    print(permut[i])
                    new.append(permut[i])
                else:
                    print(permut[i],end=" ")
                    new.append(permut[i])
            print("\n\n")
            res.append(new)
        return render_template("result8.html",res=res)
    return "Hello W"



@app.route('/types/result12',methods = ['POST', 'GET'])
def result12():
    theka = ["Dhin","Dhin","Dhaage","TiRaKiTa","Too","Naa","kat","Tin","Dhaage","TiRaKiTa","Dhin","Naa"]
    global taal_dict
    print("Hell-o")
    if request.method == 'POST' or request.method == 'GET':
        program_input="" 
        result = request.form
        print("Hello World")
        print(result)
        program_input+=taal_dict[result['beat1']]+" "
        program_input+=taal_dict[result['beat2']]
        print(program_input)
        program_input = list(program_input.split(" "))
        permlist = []
        for i in theka:
            permlist.append(i)
        for i in program_input:
            if i not in permlist:
                permlist.append(i)
        print(permlist)
        print()
        res=[]
        for i in range(12000):
            permut=[]
            new=[]
            permut=random.sample(permlist,12)
            for i in range(12):
                if ((i+1)%2 == 0):
                    print(permut[i])
                    new.append(permut[i])
                else:
                    print(permut[i],end=" ")
                    new.append(permut[i])
            print("\n\n")
            res.append(new)
        return render_template("result12.html",res=res)
    return "Hello W"



@app.route('/types/result6',methods = ['POST', 'GET'])
def result6():
    theka = ['Dhaa','Dhin','Naa','Dhaa','Tin','Naa']
    global taal_dict
    print("Hell-o")
    if request.method == 'POST' or request.method == 'GET':
        program_input="" 
        result = request.form
        print("Hello World")
        print(result)
        program_input+=taal_dict[result['beat1']]+" "
        program_input+=taal_dict[result['beat2']]
        print(program_input)
        program_input = list(program_input.split(" "))
        permlist = []
        for i in theka:
            permlist.append(i)
        for i in program_input:
            if i not in permlist:
                permlist.append(i)
        print(permlist)
        print()
        res=[]
        for i in range(12000):
            permut=[]
            new=[]
            permut=random.sample(permlist,6)
            for i in range(6):
                if ((i+1)%3 == 0):
                    print(permut[i])
                    new.append(permut[i])
                else:
                    print(permut[i],end=" ")
                    new.append(permut[i])
            print("\n\n")
            res.append(new)
        return render_template("result6.html",res=res)
    return "Hello W"


@app.route('/types/result',methods = ['POST', 'GET'])
def result():
    theka = ['Dhaa','Dhin','Dhin','Dhaa','Dhaa','Dhin','Dhin','Dhaa','Dhaa','Tin','Tin','Naa','Naa','Dhin','Dhin','Dhaa']
    global taal_dict
    print("Hell-o")
    if request.method == 'POST' or request.method == 'GET':
        program_input="" 
        result = request.form
        print("Hello World")
        print(result)
        program_input+=taal_dict[result['beat1']]+" "
        program_input+=taal_dict[result['beat2']]
        print(program_input)
        program_input = list(program_input.split(" "))
        permlist = []
        for i in theka:
            permlist.append(i)
        for i in program_input:
            if i not in permlist:
                permlist.append(i)
        res=[]
        for i in range(5000):
            permut=[]
            new=[]
            permut=random.sample(permlist,16)
            for i in range(16):
                if ((i+1)%4 == 0):
                    new.append(permut[i])
                else:
                    new.append(permut[i])
            print("\n\n")
            res.append(new)
        return render_template("result.html",res=res)
    return "Hello W"
@app.route("/laykari")
def laykari():
    return render_template("laykarigun.html")
@app.route("/laykari/dugun")
def dugun():
    return render_template("dugun.html")
@app.route("/laykari/tigun")
def tigun():
    return render_template("tigun.html")
@app.route("/laykari/chaugun")
def chaugun():
    return render_template("chaugun.html")

if __name__ == "__main__":
    app.run()