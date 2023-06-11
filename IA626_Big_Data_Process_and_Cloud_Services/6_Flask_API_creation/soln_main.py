import json,pymysql,time
from flask import Flask
from flask import request,redirect

app = Flask(__name__)

# @app.route("/", methods=['GET', 'POST'])
# def root():
#     res = {}
#     res['code'] = 2
#     res['msg'] = 'No endpoint specified'
#     res['reg'] = '/'
#     return json.dumps(res,indent=4)

@app.route("/getData", methods = ['GET', 'POST'])
def getData():
    res = {}
    key = request.args.get('key')
    start_d = request.args.get('start')
    end_d = request.args.get('end')
    if key is not None and key !='123':
        res['code'] = 0
        res['msg'] = "Bad key given"
        res['req'] = 'getData'
        return json.dumps(res,indent=4)

    start = time.time()
    conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user= 'ia626',passwd = 'ia626clarkson', db= 'ia626',autocommit=True)
    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''SELECT * FROM `conlontj_snow` WHERE `Date` BETWEEN %s AND %s ORDER BY `Date`'''
    cur.execute(sql,(start_d,end_d))
    # t = str(time.time() - start)
    #print(cur)
    res['code'] = 1
    res['msg'] = "Request OK"
    res['sqltime'] = str(time.time() - start)
    res['req'] = "getData"
    res['data'] = []
    for row in cur:
        d = {}
        d['Date'] = row['Date']
        d['Depth'] = row['Depth']
        res['data'].append(d)
        # print(row)
    return res
@app.route('/getMinMax', methods= ['GET', 'POST'])
def getMinMax():
    res = {}
    key = request.args.get('key')
    start_d = request.args.get('start')
    end_d = request.args.get('end')
    if key is not None and key !='123':
        res['code'] = 0
        res['msg'] = "Bad key given"
        res['req'] = 'getMinMax'
        return json.dumps(res,indent=4)

    start = time.time()
    conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user= 'ia626',passwd = 'ia626clarkson', db= 'ia626',autocommit=True)
    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''SELECT *,MIN(`Depth`) AS mindepth, MAX(`Depth`) AS maxdepth FROM `conlontj_snow` WHERE `Date` BETWEEN %s AND %s ORDER BY `Date`'''
    cur.execute(sql,(start_d,end_d))
    # t = str(time.time() - start)
    #print(cur)
    res['code'] = 1
    res['msg'] = "Request OK"
    res['sqltime'] = str(time.time() - start)
    res['req'] = "getMinMax"
    res['data'] = []
    for row in cur:
        d = {}
        d['min'] = row['mindepth']
        d['max'] = row['maxdepth']
        res['data'].append(d)
        #print(row)
    return res

@app.route('/getMean', methods = ['GET', 'POST'])
def getMean():
    res = {}
    key = request.args.get('key')
    start_d = request.args.get('start')
    end_d = request.args.get('end')
    if key is not None and key !='123':
        res['code'] = 0
        res['msg'] = "Bad key given"
        res['req'] = 'getMean'
        return json.dumps(res,indent=4)

    start = time.time()
    conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user= 'ia626',passwd = 'ia626clarkson', db= 'ia626',autocommit=True)
    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql = '''SELECT *,AVG(`Depth`) AS avgdepth FROM `conlontj_snow` WHERE `Date` BETWEEN %s AND %s ORDER BY `Date`'''

    cur.execute(sql,(start_d,end_d))
    # t = str(time.time() - start)
    #print(cur)
    res['code'] = 1
    res['msg'] = "Request OK"
    res['sqltime'] = str(time.time() - start)
    res['req'] = "getMean"
    res['data'] = []
    for row in cur:
        d = {}
        d['mean'] = row['avgdepth']
        res['data'].append(d)
        #print(row)
    return res

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)