from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CommentSerializer
from . import services
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

@api_view(['GET'])
def get_comments(request):
    comments = services.get_all_comments()
    serializer = CommentSerializer(comments, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def add_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_comment_view(request, pk):
    try:
        services.delete_comment(pk)
        return JsonResponse({'message': 'Deleted Successfully'}, status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)