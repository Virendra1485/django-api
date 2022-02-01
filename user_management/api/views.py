from django.shortcuts import render, HttpResponse, redirect
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import StudentTbl
from .serializers import StudentTblGetAllSerializer, StudentTblPostSerializer, StudentTblPutSerializer, loginPutSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['POST'])
def register(request):
    try:
        if request.method == "POST":
            print(request.data)
            serializer = StudentTblPostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return redirect("/GET/all/")
            return Response(serializer.errors)
    except Exception as err:
        return JSONResponse({'error': str(err)}, status=500)


@api_view(['PUT'])
def login(request):
    try:
        if request.method == "PUT":
            userid = request.data.get('userid')
            password = request.data.get('password')
            stu = StudentTbl.objects.filter(userid=userid, password=password).first()
            serializer = loginPutSerializer(stu)
            if stu:
                return Response({"message": "Login Successful"})
            else:
                return Response({"message": "Invalid User Name or Password"})
    except Exception as err:
        return JSONResponse({'error': str(err)}, status=500)


@api_view(['GET', 'PUT'])
def get_id(request, id):
    try:
        if request.method == "GET":
            stu = StudentTbl.objects.filter(id=id).first()
            if stu:
                serializer = StudentTblGetAllSerializer(stu)
                return Response(serializer.data)
            else:
                return Response({"status": 500, "message": "Id not Available"})

        if request.method == "PUT":
            stu = StudentTbl.objects.filter(id=id).first()
            if stu:
                serializer = StudentTblPutSerializer(stu, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "Updation successful"})
                else:
                    return Response({"message": "Invalid Json"})
            else:
                return Response({"status": 500, "message": "Id not Available"})
    except Exception as err:
        return JSONResponse({'error': str(err)}, status=500)


@api_view(['GET'])
def get_all(request):
    try:
        if request.method == "GET":
            stu = StudentTbl.objects.all()
            serializer = StudentTblGetAllSerializer(stu, many=True)
            return Response(serializer.data)
        else:
            return Response({"status": 500, "message": "Data not Available"})
    except Exception as err:
        return JSONResponse({'error': str(err)}, status=500)