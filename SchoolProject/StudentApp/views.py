from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from StudentApp.serializers import StudentSerializer
from StudentApp.models import Student

@csrf_exempt
def studentApi(request,id=0):
    if request.method=='GET':
        student=Student.objects.all()
        student_serializer=StudentSerializer(student,many=True)
        return JsonResponse(student_serializer.data,safe=False)
    elif request.method=='POST':
        student_data=JSONParser().parse(request)
        student_serializer=StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
    elif request.method=='PUT':
        student_data=JSONParser().parse(request)
        student=Student.objects.get(StudentId=student_data['StudentId'])
        student_serializer=StudentSerializer(student,data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update",safe=False)
    elif request.method=='DELETE':
        student=Student.objects.get(StudentId=id)
        student.delete()
        return JsonResponse("Delete Successfully",safe=False)
