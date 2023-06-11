import json,pymysql,time
from flask import Flask
from flask import request,redirect


app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def root():
    res = {} 
    res['code'] = 2
    res['msg'] = 'No endpoint specified'
    res['req'] = '/'
    return json.dumps(res,indent=4)
@app.route("/test", methods=['GET','POST'])
def test():
    res = {} 
    res['code'] = 2
    res['msg'] = 'hello'
    res['req'] = '/test'
    print("Hello world")
    return json.dumps(res,indent=4)
@app.route("/sum", methods=['GET','POST'])
def sum():
    res = {} 
    n1 =  request.args.get('n1')
    n2 =  request.args.get('n2')
    print(n2)
    n1f = None
    n2f = None
    res['req'] = '/sum'
    try:
        n1f = float(n1)
        n2f = float(n2)
    except Exception as e:
        print(str(e))
        pass
    if n1f is not None and n2f is not None:
        res['sum'] = n1f + n2f
        res['code'] = 2
        res['msg'] = 'ok'
    else:
        res['sum'] = None
        res['code'] = 1
        res['msg'] = 'n1 and n2 must be numeric'
    return json.dumps(res,indent=4)
@app.route("/wifi", methods=['GET','POST'])
def wifi():
    res = {} 
    ssid =  '%' + request.args.get('ssid') +'%'
    conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='ia626',passwd='ia626clarkson', db='ia626', autocommit=True) #setup our credentials
    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql ='SELECT * FROM `conlontj_wifi` WHERE `ssid` LIKE %s'
    cur.execute(sql,(ssid))
    rows = []
    for row in cur:
        d = {}
        d['ssid'] = row['ssid']
        d['id'] = row['id']
        d['mac'] = row['mac']
        rows.append(d)
        #print(row['ssid'])
    res['code'] = 2
    res['results'] = rows
    res['msg'] = 'hello'
    res['req'] = '/wifi'
    return json.dumps(res,indent=4)
if __name__ == "__main__":
    app.run(host='127.0.0.1',debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    