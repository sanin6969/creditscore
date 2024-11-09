from django.shortcuts import render
from django.http import JsonResponse
from .models import Question, UserResponse,CreditScore
from .utils import calculate_credit_score
import json 
from django.core import serializers

def Home(request):
    return render(request,'home/base.html')

def question_view(request):
    questions = Question.objects.all()
    questions_json = serializers.serialize('json', questions) 
    return render(request, "credit/questionnaire.html", {"questions_json": questions_json})

def submit_answer(request):
    if request.method == "POST":
        data = json.loads(request.body)
        question = Question.objects.get(id=data["question_id"])
        answer = data["answer"]
        UserResponse.objects.create(user=request.user, question=question, answer=answer)
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "failed"}, status=400)

def results_view(request):
    user_responses = UserResponse.objects.filter(user=request.user)
    credit_score = calculate_credit_score(user_responses)
    credit_score_record, created = CreditScore.objects.get_or_create(user=request.user)
    credit_score_record.score = credit_score
    credit_score_record.save()
    return render(request, "credit/results.html", {"credit_score": credit_score})
