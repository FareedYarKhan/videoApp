from datetime import timedelta
from rest_framework import serializers,views
from .models import processedFiles, video
from .serializer import VideoSerializer,FileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework import status
from django.http.response import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .data import data

@csrf_exempt
def get_json(request,id):
    obj=video.objects.get(pk=id)
    file=processedFiles.objects.get(video=obj)
    json_file_path = file.fileJson

    with open(json_file_path, 'r') as j:
         contents = json.loads(j.read())
    return JsonResponse({'status':contents})

@csrf_exempt
def remove_videos(request,id):
    obj=video.objects.get(pk=id)
    obj.delete()
    return JsonResponse({'status':"Done"})

@api_view(['GET'])
def get_videos(request):
    obj=video.objects.all()
    serializer=VideoSerializer(obj,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_video(request,id):
    obj=video.objects.get(pk=id)
    serializer=VideoSerializer(obj)
    return Response(serializer.data)

@api_view(['GET'])
def get_file(request,vid):
    v=video.objects.get(pk=vid)
    obj=processedFiles.objects.filter(video=v)
    serializer=FileSerializer(obj,many=True)
    return Response(serializer.data)

class fileUpload(views.APIView):
    parser_classes=(MultiPartParser,FormParser)
    def post(self,request,*args,**kwargs):
        serializer=VideoSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            id=serializer.data['id']
            import datetime
 
# Get current date and time
            dt = datetime.datetime.now()
 
# Format datetime string
            x = dt.strftime("%Y-%m-%d-%H-%M-%S")
            name=x+'-'+str(id)+'.json' 
            path='./static/files/'
            vid=video.objects.get(pk=id)
            import json
            with open(path+name, 'w') as f:
                  json.dump(data, f)
            
            obj=processedFiles(video=vid,fileJson=path+name)
            obj.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            print('error',serializer.errors)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        