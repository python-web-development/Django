from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer_text = models.TextField()

    def __str__(self):
        return self.question_text
