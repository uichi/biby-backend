from django.db.models import BooleanField, \
    CharField, \
    DateField, \
    DateTimeField, \
    ForeignKey, \
    FloatField, \
    IntegerField, \
    TextField, \
    UUIDField
from django.db.models import CASCADE, SET_NULL, Model, ManyToManyField
from django.contrib.auth import get_user_model
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
import uuid

User = get_user_model()


# Pet Category
class PetCategory(Model):
    name = CharField(max_length=128, blank=False, null=False)

    def __str__(self):
        return self.name


# Pet
class Pet(Model):
    GENDER = (('male', 'オス'), ('female', 'メス'))
    name = CharField(max_length=150, blank=False, null=False)
    image = ProcessedImageField(upload_to='pet_images',
                                processors=[ResizeToFill(100, 100)],
                                options={'quality': 100},
                                blank=True,
                                null=True)
    gender = CharField(choices=GENDER, max_length=16, blank=True, null=True)
    birthday = DateField(blank=True, null=True)
    welcome_day = DateField(blank=True, null=True)
    # TODO: 読み取り専用にしたい
    share_id = UUIDField(default=uuid.uuid4, editable=False)
    is_heaven = BooleanField(blank=True, null=False, default=False)
    category = ForeignKey(PetCategory, on_delete=SET_NULL, blank=True, null=True)
    owners = ManyToManyField(
        User,
        through='PetOwnerGroup',
    )
    donate_link = CharField(max_length=256, blank=True, null=True)
    created_at = DateTimeField('作成日', auto_now_add=True)
    updated_at = DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.name


# Pet owner group
class PetOwnerGroup(Model):
    user = ForeignKey(User, on_delete=CASCADE, null=False)
    pet = ForeignKey(Pet, on_delete=CASCADE, null=False)
    created_at = DateTimeField('作成日', auto_now_add=True)
    updated_at = DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.user


# Care Category
class CareCategory(Model):
    INPUT_TYPE = (('text', 'テキスト'), ('integer', '整数'), ('float', '小数点'), ('checkbox', 'チェックボックス'))
    name = CharField(max_length=150, blank=False, null=False)
    icon = IntegerField(blank=True, null=True, default=1)
    input_type = CharField(choices=INPUT_TYPE, max_length=16, blank=True, null=True)
    unit = CharField(max_length=10, blank=True, null=True)
    is_daily_routine = BooleanField(blank=True, null=False, default=False)
    user = ForeignKey(User, on_delete=CASCADE, null=False)
    created_at = DateTimeField('作成日', auto_now_add=True)
    updated_at = DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.name


# Pet Care Log
class PetCareLog(Model):
    integer = IntegerField(blank=True, null=True)
    float = FloatField(blank=True, null=True)
    text = TextField(blank=True, null=True)
    checkbox = BooleanField(blank=True, null=False, default=False)
    care_category = ForeignKey(CareCategory, on_delete=CASCADE, null=False)
    date_time = DateTimeField(blank=False, null=False)
    memo = TextField(blank=True, null=True)
    pet = ForeignKey(Pet, on_delete=CASCADE, null=False)
    user = ForeignKey(User, on_delete=CASCADE, null=False)
    created_at = DateTimeField('作成日', auto_now_add=True)
    updated_at = DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.pet
