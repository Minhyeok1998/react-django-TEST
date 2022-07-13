from rest_framework import viewsets
from .serializers import BoardSerializer,CommentSerializer,MembertSerializer,SwingResultSerializer
from .models import Comment,SwingResult,Board,Member

# class SibalViewSet(viewsets.ModelViewSet):
#     queryset = Sibal.objects.all()
#     serializer_class = SibalSerializer
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class SwingResultViewSet(viewsets.ModelViewSet):
    queryset = SwingResult.objects.all()
    serializer_class = SwingResultSerializer

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MembertSerializer
