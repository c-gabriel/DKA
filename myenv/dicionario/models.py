from django.db import models

class Word(models.Model):
    word_en = models.TextField()
    word_cr = models.TextField()
    word_pt = models.TextField()
    descr = models.TextField()

    def __str__(self):
        return self.word_pt
