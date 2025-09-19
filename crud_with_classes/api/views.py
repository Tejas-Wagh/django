from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentSerializer
from .models import Students
# Create your views here.

class StudentListCreateView(APIView):
    def get(self,request):
        try:
            students = Students.objects.all()
            serializedStudents = StudentSerializer(students, many = True)       
            return Response(serializedStudents.data)
        except:
            return Response("Something went wrong")    
        
    
    def post(self,request):
        try:
            serializer = StudentSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            else:
                return Response(serializer.errors, status=400)
        except:
            return Response("Something went wrong", status=500)
    

class StudentDetailView(APIView):
    def get(self, request, id):
        student = Students.objects.get(id = id)
        serializedstudent = StudentSerializer(student)
        return Response(serializedstudent.data)
    
    def put(self,request,id):
        student = Students.objects.get(id = id)
        serialized = StudentSerializer(student, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        
        return Response(serialized.errors, status=400)
        

    def delete(self, request, id):
        try:
            student = Students.objects.get(id = id)
            student.delete()
            return Response("Student Removed")
        except:
            return Response("An error occured while deleting the student")