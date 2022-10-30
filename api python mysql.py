from flask import  Flask , request, jsonify

app = Flask(__name__)
import mysql.connector as conn
mydb=conn.connect(host="localhost",user="root",passwd="abc123456")
cursor = mydb.cursor()
cursor.execute("create database if not exists joy")
cursor.execute("create table if not exists joy.midb(name varchar(30),number int(20))")

@app.route('/insert',methods=['GET', 'POST'])
def table():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into joy.midb values (%s, %s)",(name, number))
        mydb.commit()
        return jsonify(str("sucessful"))
@app.route('/update',methods=['GET', 'POST'])
def update():
    if request.method=='POST':
        name = request.json['name']
        cursor.execute("update joy.midb set number= number + 100 where name= %s",(name,))
        mydb.commit()
        return jsonify(str("sucessful"))
@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name']
        cursor.execute("delete from joy.midb where name= %s", (name_del,))
        mydb.commit()
        return jsonify(str("deleted sucessful"))
@app.route('/fetch',methods=['POST'])
def fetch():
    cursor.execute("select * from joy.midb")
    l=[]
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))
if __name__=='__main__':
    app.run()





