from django.db import IntegrityError
from django.db.models import Model, CharField, TextField, ImageField, IntegerField, ForeignKey, DateTimeField, CASCADE, \
    SlugField, EmailField
from django.utils.text import slugify
from unidecode import unidecode




class Post(Model):
    title = CharField(max_length=255)
    description = TextField()
    image = ImageField(upload_to='post/')
    author = ForeignKey('auth.User', CASCADE)
    views = IntegerField(default=0)
    slug = SlugField(unique=True, blank=False)
    published_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
            try:
                last = Post.objects.filter(slug__regex="%s-\d+" % self.slug).latest('id')

                trash, count = last.slug.rsplit('-', 1)
                count = int(count) + 1
            except:
                count = 1
            while count < 1000:
                self.slug = "%s-%d" % (self.slug, count)
                try:
                    super(Post, self).save(*args, **kwargs)
                    break
                except IntegrityError as exc:
                    count += 1

        super().save(*args, **kwargs)




    class Meta:
        ordering = '-published_at',
        db_table = 'posts'


class Comment(Model):
    name = CharField(max_length=255)
    email = EmailField(max_length=255)
    text = TextField()
    post = ForeignKey('apps.Post', CASCADE)
