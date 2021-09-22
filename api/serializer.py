from rest_framework.serializers import ModelSerializer
from .models import video,processedFiles
class VideoSerializer(ModelSerializer):
    class Meta:
        model = video
        fields = '__all__'


class FileSerializer(ModelSerializer):
    class Meta:
        model = processedFiles
        fields = '__all__'