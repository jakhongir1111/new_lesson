from django.db.models import Model, CharField, TextField, ImageField, IntegerField, ForeignKey, DateTimeField, CASCADE, \
    SlugField, EmailField
from django.utils.text import slugify


class Post(Model):
    title = CharField(max_length=255)
    description = TextField()
    image = ImageField(upload_to='post/')
    author = ForeignKey('auth.User', CASCADE)
    views = IntegerField(default=0)
    slug = SlugField()
    published_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # birhil nomli postni slugini unique qilish
        # slugni lotin harfida saqlash
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = '-published_at',
        db_table = 'posts'


class Comment(Model):
    name = CharField(max_length=255)
    email = EmailField(max_length=255)
    text = TextField()

    post = ForeignKey('apps.Post', CASCADE)
