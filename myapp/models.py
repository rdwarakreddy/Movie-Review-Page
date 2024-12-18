from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.conf import settings
# from django.core.mail import send_mail

class MovieReview(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)],help_text="Rating should be between 1 and 5")
    review = models.TextField()
    photo = models.ImageField(upload_to='movie_photos/',null = True,blank = True)
    link = models.URLField(max_length=500,null = True,blank = True)

    def __str__(self):
        return f"{self.movie_name} - {self.user.username}"

class Like(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    review = models.ForeignKey(MovieReview,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.ForeignKey(MovieReview,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)