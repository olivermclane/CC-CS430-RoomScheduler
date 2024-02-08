from rest_framework import serializers
from .models import Building, Floor, Classroom, Course


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class FloorSerializer(serializers.ModelSerializer):
    building = BuildingSerializer(read_only=True)

    class Meta:
        model = Floor
        fields = ['floor_id', 'floor_name', 'building']


class ClassroomSerializer(serializers.ModelSerializer):
    floor = FloorSerializer(read_only=True)

    class Meta:
        model = Classroom
        fields = [
            'classroom_id',
            'class_room_number',
            'total_seats',
            'width_of_room',
            'length_of_room',
            'projectors',
            'microphone_system',
            'blueray_player',
            'laptop_hdmi',
            'zoom_camera',
            'document_camera',
            'storage',
            'movable_chairs',
            'printer',
            'piano',
            'stereo_system',
            'total_tv',
            'sinks',
            'notes',
            'floor',
        ]


class CourseSerializer(serializers.ModelSerializer):
    classroom = ClassroomSerializer(read_only=True)

    class Meta:
        model = Course
        fields = [
            'course_id',
            'classroom',
            'start_time',
            'end_time',
            'instructor',
            'first_day',
            'last_day',
            'course_name',
            'term',
            'credits',
            'course_cap',
            'waitlist_cap',
            'course_total',
            'waitlist_total',
            'enrollment_total',
            'course_level',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
        ]
