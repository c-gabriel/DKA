from django.db import models
from django.utils import timezone
from sequences import get_next_value

class Word(models.Model):
    word_en_id = models.BigIntegerField()
    word_cr_id = models.BigIntegerField()
    word_pt_id = models.BigIntegerField()
    word_en = models.TextField()
    word_cr = models.TextField()
    word_pt = models.TextField()
    descr = models.TextField()

    def publish(self):
        self.word_en_id = get_next_value('word_en_sq')
        self.word_cr_id = get_next_value('word_cr_sq')
        self.word_pt_id = get_next_value('word_pt_sq')
        self.save()

    def __str__(self):
        return self.word_pt
