from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True, db_index=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    image = models.ImageField(upload_to='posts/', blank=True, null=True)  # поле для картинки

    def __str__(self):
        
        return self.text

