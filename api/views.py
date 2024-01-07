from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


@api_view(["GET"])
def student_list(request):
    student_list = Student.objects.all()
    student_serializer = StudentSerializer(student_list, many=True)
    data = list(student_serializer.data)
    return JsonResponse(data, safe=False)


@api_view(["GET"])
def student_detail(request, pk):
    student_detail = get_object_or_404(Student, id=pk)
    student_serializer = StudentSerializer(student_detail, many=False)
    return Response(student_serializer.data)


@api_view(["POST"])
def add_student(request):
    serializerData = StudentSerializer(data=request.data)
    if serializerData.is_valid():
        serializerData.save()
    return Response(serializerData.data)


@api_view(["PUT"])
def update_student(request, pk):
    student = get_object_or_404(Student, id - pk)
    serializer_student = StudentSerializer(instance=student, data=request.data)
    if serializer_student.is_valid():
        serializer_student.save()
    return Response(serializer_student.data)


@api_view(["DELETE"])
def delete_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    student_list = Student.objects.all()
    serializer_student = StudentSerializer(student_list, many=True)
    return Response(serializer_student.data)
