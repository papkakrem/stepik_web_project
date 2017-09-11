# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from qa.models import Question

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
    return render(request, 'question.html',
                  {'question': question,
                  'answers': answers
                  }
                 )

def test(request, *args, **kwargs):
    return HttpResponse('OK')
