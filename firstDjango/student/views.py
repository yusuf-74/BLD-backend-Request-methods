from django.http import JsonResponse
import json
from operator import itemgetter


def index(request):
    mydata = []
    data = 0
    with open("./student/data.json", "r") as file:
        data = file.read()
        mydata = json.loads(data)
    sorted_lst = sorted(mydata, key=itemgetter('id'))
    if request.method == "GET":
        return JsonResponse(sorted_lst, safe=False)
    
    elif request.method == "POST":
        mydata.append(json.loads(request.body))
        with open("./student/data.json", "w") as file:
            file.write(json.dumps(mydata))
        sorted_lst = sorted(mydata, key=itemgetter('id'))
        return JsonResponse(sorted_lst, safe=False)
    
    elif request.method == "PUT":
        target = json.loads(request.body)
        for i in range(len(mydata)):
            if mydata[i]["id"] == target["id"]:
                mydata[i] = target
                break
        with open("./student/data.json", "w") as file:
            file.write(json.dumps(mydata))
        sorted_lst = sorted(mydata, key=itemgetter('id'))
        return JsonResponse(sorted_lst, safe=False)
    
    elif request.method == "DELETE":
        target = json.loads(request.body)
        for i in range(len(mydata)):
            if mydata[i]["id"] == target["id"]:
                del mydata[i]
                break

        with open("./student/data.json", "w") as file:
            file.write(json.dumps(mydata))
        sorted_lst = sorted(mydata, key=itemgetter('id'))
        return JsonResponse(sorted_lst, safe=False)

