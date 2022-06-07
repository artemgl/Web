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

    return paginator, page


def main_page(request):
    questions = Question.objects.new()
    paginator, page = paginate(request, questions)
    paginator.baseurl = '/?page='
    return render(request, 'question_list.html', {
        'posts': page.object_list,
        'paginator': paginator, 'page': page,
    })


def popular(request):
    questions = Question.objects.popular()                                                  
    paginator, page = paginate(request, questions)                                                       
    paginator.baseurl = '/popular/?page='     
    return render(request, 'question_list.html', {       
        'posts': page.object_list,             
        'paginator': paginator, 'page': page,
    })


def question(request, id):
    try:
        answers = Answer.objects.filter(question=id)
    except Answer.DoesNotExist:
        raise Http404

    question = get_object_or_404(Question, id=id)

    return render(request, 'question.html', {
        'answers': answers,
        'question': question,
    })

