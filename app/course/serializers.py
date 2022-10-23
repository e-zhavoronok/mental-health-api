from rest_framework import serializers

from core.models import Tag, Task, Course


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class TaskSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'tags')
        read_only_fields = ('id',)

class TaskDetailSerializer(TaskSerializer):
    tags = TagSerializer(many=True, read_only=True)


class CourseSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Task.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Course
        fields = ('id', 'title', 'description','price', 'tasks', 'tags')
        read_only_fields = ('id',)


class CourseDetailSerializer(CourseSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)