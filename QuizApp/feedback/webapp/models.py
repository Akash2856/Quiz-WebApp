from django.db import models
class Feedback(models.Model):
    feedback_title = models.CharField(max_length=20)
    feedback_content = models.TextField()

    def __str__(self):
        return self.feedback_title

class Question(models.Model):
    question_content = models.CharField(max_length=200)

    def __str__(self):
        return self.question_content


class Choice(models.Model):
    quiz = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choice_answer = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{} {}".format(self.quiz.question_content[:200], self.choice_text[:200])

