from django.db import models

class Idea(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='ideas/', blank=True, null=True)
    content = models.TextField()
    interest = models.IntegerField(default=0)
    is_starred = models.BooleanField(default=False)
    devtool = models.ForeignKey('devtools.DevTool', on_delete=models.CASCADE, related_name='ideas')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title