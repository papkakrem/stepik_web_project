# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm

# Create your views here.

def index(request, is_popular=False, limit = 10):

    if is_popular:
        questions = Question.objects.popular()
        reverse_url = reverse('popular')
    else:
        questions = Question.objects.new()
        reverse_url = reverse('index')

    try:
        page_number = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(questions, limit)
    paginator.baseurl = "%s?page=" % reverse_url

    try:
        page = paginator.page(page_number)
    except EmptyPage:
        raise Http404

    return render(request, 'index.html',
                  {'questions': page.object_list,
                   'paginator': paginator,
                   'page': page
                  }
                )

def question(request, id):

    question = get_object_or_404(Question, id=id)
    answers = question.answer_set.all()

    if request.method == 'POST':
        form = AnswerForm(request.POST, question=question)
        if form.is_valid():
            answer = form.save()
            return HttpResponseRedirect(reverse('question', args=[question.id]))
    else:
        form = AnswerForm(question=question)

    return render(request, 'question.html',
                  {'question': question,
                  'answers': answers,
                  'form': form
                  }
                 )

def ask_form(request):

    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(reverse('question', args=[question.id]))

    else:
        form = AskForm()

    return render(request, 'ask_form.html', {'form': form})

def test(request, *args, **kwargs):
    return HttpResponse('OK')
