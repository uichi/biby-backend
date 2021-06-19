from django.db.models import BooleanField, \
    CharField, \
    DateTimeField, \
    ForeignKey, \
    FloatField, \
    IntegerField, \
    TextField
from django.db.models import CASCADE, DO_NOTHING, Model
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Pet
class Pet(Model):
    GENDER = ((1, 'オス'), (2, 'メス'))
    name = CharField(max_length=150, blank=False, null=False)
    image = ProcessedImageField(upload_to='pet_images',
                                processors=[ResizeToFill(75, 75)],
                                options={'quality': 60},
                                blank=True,
                                null=True)
    gender = IntegerField(choices=GENDER, blank=True, null=True)
    birthday = DateTimeField(blank=True, null=True)
    welcome_day = DateTimeField(blank=True, null=True)
    share_id = CharField(max_length=128, null=False)
    is_heaven = BooleanField(blank=True, null=False, default=False)
    created_at = DateTimeField('作成日', auto_now_add=True)
    updated_at = DateTimeField('更新日', auto_now=True)


# Pet owner group
class PetOwnerGroup(Model):
    user = ForeignKey(User, on_delete=DO_NOTHING, null=False)
    pet = ForeignKey(Pet, on_delete=CASCADE, null=False)
    created_at = DateTimeField('作成日', auto_now_add=True)
    updated_at = DateTimeField('更新日', auto_now=True)


# Care Category
class CareCategory(Model):
    name = CharField(max_length=150, blank=False, null=False)
    icon = IntegerField(blank=True, null=True, default=1)
    input_type = IntegerField(blank=True, null=True)
    unit = CharField(max_length=10, blank=True, null=True)
    is_daily_routine = BooleanField(blank=True, null=False, default=False)
    pet = ForeignKey(Pet, on_delete=CASCADE, null=False)
    created_at = DateTimeField('作成日', auto_now_add=True)
    updated_at = DateTimeField('更新日', auto_now=True)


# Pet Care Log
class PetCareLog(Model):
    integer = IntegerField(blank=True, null=True)
    float = FloatField(blank=True, null=True)
    text = TextField(blank=True, null=True)
    checkbox = BooleanField(blank=True, null=False, default=False)
    care_category = ForeignKey(CareCategory, on_delete=CASCADE, null=False)
    memo = TextField(blank=True, null=True)
    created_at = DateTimeField('作成日', auto_now_add=True)
    updated_at = DateTimeField('更新日', auto_now=True)
