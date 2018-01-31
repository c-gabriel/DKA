from django.db import models

class Word(models.Model):
    word_en = models.CharField(max_length=60)
    word_cr = models.CharField(max_length=60)
    word_pt = models.CharField(max_length=60)
    descr = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.word_pt
