from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey('auth.user', on_delete=models.CASCADE);
    created_at = models.DateTimeField(auto_now_add=True)
    upadted_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name    
