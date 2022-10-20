import json

mydata = []
with open('./myenv/data.json', "r") as file:
    data = file.read()
    mydata = json.loads(data)
    print (mydata)

id = mydata[len(mydata)-1]["id"];
id+=1
name = "hommos"
name = name+str(id)
mydata.append({"id":id , "name":name})

with open('./myenv/data.json', "w") as file:
    file.write(json.dumps(mydata))
   
    
    # data = json.dumps(data)
    # file.write(data)
