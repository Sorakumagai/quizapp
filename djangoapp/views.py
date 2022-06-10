from django.shortcuts import render, redirect
from .quiz import *
# Create your views here.
def index(request):
    # template = 'index.html'
    context = {
        'title': 'QuizApp'
    }
    return render(request, 'index.html', context)

def pref_quiz(request):
    prefecture, city, url = prefecture_quiz()
    context = {
        'title': '県庁所在地クイズ',
        'prefecture': prefecture,
        'city': city,
        'url': url,
    }
    return render(request, 'prefecture_tpl.html', context)

def pref_result(request):
    if request.method == "POST":
        userinput_city = request.POST.get('userinput_city')
        prefecture = request.POST.get('prefecture')
        city = request.POST.get('city')
        url = request.POST.get('url')

        if city == userinput_city:
            result = '正解'
        else:
            result = '不正解'

        context = {
            'title': '県庁所在地クイズ - 結果',
            'result': result,
            'prefecture': prefecture,
            'city': city,
            'url': url,
        }

        return render(request, 'prefecture_result.html', context)

def random_quiz(request):
    selected_qa = quiz()

    num = [i for i in range(1, 6)]
    question = []
    answer = []
    for i in selected_qa:
        question.append(i[0])
        answer.append(i[1])
    context = {
        'title': 'ランダムクイズ',
        'num': num,
        'question': question,
        'answer': answer,
    }
    return render(request, 'quiz_tpl.html', context)

def quiz_result(request):
    if request.method == 'POST':
        score = 0
        user_answer = request.POST.getlist('user_answer')
        answer = request.POST.getlist('answer')
        for i, j in zip(user_answer, answer):
            if i == j:
                score += 20
        
        context = {
            'title': 'クイズの結果です',
            'score': score,
            'answer': answer,
            'user_answer': user_answer
        }
        return render(request, 'quiz_result.html', context)

def wiki(request):
    context = {
        'title': 'Python版Wikipediaで調べる',
    }
    return render(request, 'wiki_tpl.html', context)

def wiki_result(request):
    if request.method == 'GET':
        word = request.GET.get('word')
        result = wikipy(word)
        context = {
            'title': 'Python版wikipediaで調べる',
            'result': result,
        }
        return render(request, 'wiki_result.html', context)