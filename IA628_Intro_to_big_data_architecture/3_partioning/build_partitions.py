import os,json,datetime
path = 'cdlog'
partitioned_path = "partitioned"
for file in os.listdir(path):
    fp = os.path.join(path,file)
    print(fp)
    with open(fp,'r') as f:
        for line in f:
            data = json.loads(line)
            payload = json.loads(data['payload'])
            #print(payload)
            rdo = datetime.datetime.strptime(payload['received'], '%Y-%m-%dT%H:%M:%S.%f')
            partitioned_fp = os.path.join(partitioned_path,rdo.strftime('%Y_%m_%d')+".txt")
            #print(partitioned_fp)
            with open(partitioned_fp,'a') as f2:
                f2.write(data['payload']+"\n")




         