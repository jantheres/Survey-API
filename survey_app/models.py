from django.db import models

# Survey model
class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Question model
class Question(models.Model):
    TEXT = 'text'
    CHOICE = 'choice'
    QUESTION_TYPES = [
        (TEXT, 'Text'),
        (CHOICE, 'Choice'),
    ]

    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=50, choices=QUESTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


# Response model
class Response(models.Model):
    user_id = models.IntegerField()  # You can replace this with a ForeignKey to your User model
    survey = models.ForeignKey(Survey, related_name='responses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response for {self.survey.title} by User ID: {self.user_id}"


# Answer model
class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    response = models.ForeignKey(Response, related_name='answers', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    choice = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Answer for {self.question.text} in Response ID: {self.response.id}"
