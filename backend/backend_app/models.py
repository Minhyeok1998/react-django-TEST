from django.db import models

class Board(models.Model):
    board_num = models.AutoField(primary_key=True)
    member = models.ForeignKey('Member', models.DO_NOTHING)
    subject = models.CharField(max_length=45)
    create_date = models.DateTimeField()
    content = models.TextField()
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board'


class Comment(models.Model):
    comment_num = models.AutoField(primary_key=True)
    board_num = models.ForeignKey(Board, models.DO_NOTHING, db_column='board_num', blank=True, null=True)
    member = models.ForeignKey('Member', models.DO_NOTHING, blank=True, null=True)
    content = models.TextField()
    recomment = models.ForeignKey('self', models.DO_NOTHING, db_column='recomment', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class Member(models.Model):
    member_id = models.CharField(primary_key=True, max_length=50)
    member_pwd = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    golf_career = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'


class SwingResult(models.Model):
    member = models.OneToOneField(Member, models.DO_NOTHING, primary_key=True)
    swing_date = models.DateTimeField()
    address_result = models.IntegerField(blank=True, null=True)
    top_result = models.IntegerField(blank=True, null=True)
    finish_result = models.IntegerField(blank=True, null=True)
    address_img = models.CharField(max_length=200, blank=True, null=True)
    top_img = models.CharField(max_length=200, blank=True, null=True)
    finish_img = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'swing_result'
        unique_together = (('member', 'swing_date'),)