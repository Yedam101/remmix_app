from rest_framework.serializers import ModelSerializer
from .models import Diary, Music

    
class DiarySerializer(ModelSerializer):

    class Meta:
        model = Diary
        fields = '__all__'


class MusicSerializer(ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'