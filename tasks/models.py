from django.db import models

class Task(models.Model):
    title = models.CharField("Titulo", max_length=120)
    description = models.TextField("Descrição", blank=True)
    done = models.BooleanField("Concluido", default=False)
    created_at = models.DateTimeField("Criada em", auto_now_add=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


# Create your models here.
