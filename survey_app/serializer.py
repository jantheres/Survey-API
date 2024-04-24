from rest_framework import serializers
from .models import Survey, Question, Response, Answer

# Serializer for Answer model
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'response', 'text', 'choice')


# Serializer for Question model
class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'survey', 'text', 'question_type', 'answers')


# Serializer for Response model
class ResponseSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Response
        fields = ('id', 'user_id', 'survey', 'created_at', 'answers')


# Serializer for Survey model
class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    responses = ResponseSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ('id', 'title', 'description', 'created_at', 'updated_at', 'questions', 'responses')


# Serializer for creating a new Survey
class SurveyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('title', 'description')
