from flask import Flask, jsonify,request
app=Flask('__main')
import mysql.connector as conn
@app.route('/mama')
def get_data():
    db=request.args.get('db')
    tn=request.args.get('tn')
    try:
        con = conn.connect(host="localhost", user="root", passwd="abc123456",database=db)
        cur=con.cursor(dictionary=True)
        cur.execute(f'select * from {tn}')
        data=cur.fetchall()
        con.commit()
        con.close()
    except Exception as e:
        return jsonify(str(e))
    return jsonify(data)

if __name__=='__main__':
    app.run(port=5002)
# type this url in the address bar of browser http://127.0.0.1:5002/mama?db=joy&tn=midb





