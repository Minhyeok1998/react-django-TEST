# from django.contrib.auth.models import User, Group
from .models import Board,Comment,Member,SwingResult
from rest_framework import serializers

class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('board_num', 'member', 'subject','create_date','content','update_date')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_num', 'board_num', 'member','content','recomment')

class MembertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('member_id', 'member_pwd', 'name','email','phone','golf_career','gender')

class SwingResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SwingResult
        fields = ('member', 'swing_date', 'address_result','top_result','finish_result','address_img','top_img','finish_img') 

