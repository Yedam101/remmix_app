
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound)

from .models import Diary, Music
from . import serializers


class Diaries(APIView):

    def get(self, request):
        diary = Diary.objects.all()
        serializer = serializers.DiarySerializer(diary, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.DiarySerializer(data=request.data)
        if serializer.is_valid():
            diary = serializer.save()
            return Response(
                serializers.DiarySerializer(diary).data,
            )
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )


class DiaryDetail(APIView):
    def get_object(self, pk):
        try:
            return Diary.objects.get(pk=pk)
        except Diary.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        diary = self.get_object(pk)
        serializer = serializers.DiarySerializer(diary)
        return Response(serializer.data)

    def put(self, request, pk):
        diary = self.get_object(pk)
        serializer = serializers.DiarySerializer(
            diary,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_diary = serializer.save()
            return Response(
                serializers.DiarySerializer(updated_diary).data,
            )
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, pk):
        diary = self.get_object(pk)
        diary.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    

