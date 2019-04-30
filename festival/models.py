from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
import re


class Region(models.Model):
    name = models.CharField(max_length=50)
    thumbnail = models.ImageField('festival/Region/thumbnail')
    main_image = models.ImageField('festival/Region/main_image')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=140, unique=True)

    def __str__(self):
        return self.name


class Festival(models.Model):
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    summery = models.TextField()
    content = models.TextField()
    start = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    end = models.DateField()
    map = models.CharField(max_length=300)
    thumbnail = ProcessedImageField(
        upload_to='festival/thumbnail',
        format='JPEG',
        options={'quality': 80}
    )
    file = models.FileField()
    admin_name = models.CharField(max_length=50)
    admin_phone = models.CharField(max_length=50)
    admin_email = models.EmailField(max_length=50)
    host = models.CharField(max_length=50)
    supervision = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    confirm = models.BooleanField(default=False)
    tag = models.CharField(max_length=150)
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    def tag_save(self):
        tags = re.findall(r'#(\w+)\b', self.tag)

        if not tags:
            return

        for t in tags:
            tag, tag_created = Tag.objects.get_or_create(name=t)
            self.tag_set.add(tag)  # NOTE: ManyToManyField 에 인스턴스 추가


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            ('user', 'festival')
        )


class Comment(models.Model):
    festival = models.ForeignKey(Festival, models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.content
