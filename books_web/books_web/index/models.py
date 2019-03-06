# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=64)
    book_author = models.CharField(max_length=64, blank=True, null=True)
    book_price = models.CharField(max_length=64, blank=True, null=True)
    book_introduction = models.TextField(blank=True, null=True)
    book_press = models.CharField(max_length=64, blank=True, null=True)
    book_publication_date = models.DateField(blank=True, null=True)
    book_words = models.TextField(blank=True, null=True)
    book_starts = models.FloatField(blank=True, null=True)
    book_photo = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    comment_date = models.DateField(blank=True, null=True)
    comment_content = models.TextField(blank=True, null=True)
    comment_book = models.ForeignKey(Books, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Labels(models.Model):
    label_id = models.AutoField(primary_key=True)
    label_book = models.ForeignKey(Books, models.DO_NOTHING, blank=True, null=True)
    label_l1 = models.CharField(db_column='label_L1', max_length=64, blank=True, null=True)  # Field name made lowercase.
    label_l2 = models.CharField(db_column='label_L2', max_length=64, blank=True, null=True)  # Field name made lowercase.
    label_l3 = models.CharField(db_column='label_L3', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'labels'


class Users(models.Model):
    def __str__(self):
        return self.user_name

    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField('用户名',max_length=64, blank=True, null=True)
    user_photo = models.TextField(blank=True, null=True)
    user_email = models.CharField('邮箱地址',max_length=64, blank=True, null=True)
    user_passwd = models.CharField('密码',max_length=64, blank=True, null=True)




    class Meta:
        managed = False
        db_table = 'users'
        verbose_name = '注册用户'
        verbose_name_plural = verbose_name
