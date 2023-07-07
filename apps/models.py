from django.db.models import Model, CharField, TextField, ImageField, IntegerField, ForeignKey, DateTimeField, CASCADE, \
    SlugField
from django.utils.text import slugify


class Post(Model):
    title = CharField(max_length=255)
    description = TextField()
    image = ImageField(upload_to='post/')
    author = ForeignKey('auth.User', CASCADE)
    views = IntegerField(default=0)
    slug = SlugField()
    published_at = DateTimeField(auto_now=True)
    updated_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:

            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = '-published_at',
        db_table = 'posts'
