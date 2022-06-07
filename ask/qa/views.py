from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from qa.models import Question, QuestionManager, Answer


def test(request, *args, **kwargs):                          
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10

    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)

    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page


def main_page(request):
    questions = Question.objects.new()
    page = paginate(request, questions)
    return render(request, 'question_list.html', {
        'questions': page.object_list,
    })


def popular(request):
    questions = Question.objects.popular()                                                  
    page = paginate(request, questions)                                                       
    return render(request, 'question_list.html', {       
        'questions': page.object_list,             
    })


def question(request, pk):        
    question = get_object_or_404(Question, id=pk)

    return render(request, 'question.html', {
        'answers': question.answer_set.all(),
        'question': question,
    })

