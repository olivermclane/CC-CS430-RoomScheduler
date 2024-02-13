from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Building, Floor, Classroom, Course, User
from .serializers import BuildingSerializer, FloorSerializer, ClassroomSerializer, CourseSerializer, UserSerializer


class DefaultView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return render(request, 'index.html')


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class RegisterView(APIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.instance
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class BuildingView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # Retrieve buildings data for authenticated user
        buildings = Building.objects.all()
        serializer = BuildingSerializer(buildings, many=True)
        return Response(serializer.data)


class BuildingDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            building = Building.objects.get(building_id=pk)
            serializer = BuildingSerializer(building)
            return Response(serializer.data)
        except Building.DoesNotExist:
            return Response({'error': 'Building not found'}, status=404)


class CourseView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # Retrieve buildings data for authenticated user
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class CourseDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            course = Course.objects.get(course_id=pk)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=404)


class ClassroomView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        classroom = Classroom.objects.all()
        serializer = ClassroomSerializer(classroom, many=True)
        return Response(serializer.data)


class ClassroomDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            classrooms = Classroom.objects.get(classroom_id=pk)
            serializer = ClassroomSerializer(classrooms)
            return Response(serializer.data)
        except Classroom.DoesNotExist:
            return Response({'error': 'Classroom not found'}, status=404)


class FloorView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        floors = Floor.objects.all()
        serializer = FloorSerializer(floors, many=True)
        return Response(serializer.data)


class FloorDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            floor = Floor.objects.get(floor_id=pk)
            serializer = FloorSerializer(floor)
            return Response(serializer.data)
        except Floor.DoesNotExist:
            return Response({'error': 'Floor not found'}, status=404)
