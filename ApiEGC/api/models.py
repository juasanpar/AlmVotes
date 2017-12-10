from django.db import models

class Voto(models.Model):
    identificadorUsuario = models.CharField(max_length=200)
    voto = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    procedencia = models.CharField(max_length=200)
    
    def __str__(self):
        return '%s %s' % (self.title, self.body)