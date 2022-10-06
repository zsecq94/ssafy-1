from random import Random
from django.shortcuts import redirect, render

from eithers.forms import CommentForm, QuestionForm
from eithers.models import Question, Comment

# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)

def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eithers:index')
    else:
        form = QuestionForm()
    context = {
        'form':form,
    }
    return render(request, 'eithers/create.html', context)

def detail(request, pk):
    question = Question.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = question.comment_set.all()
    context = {
        'question': question,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'eithers/detail.html', context)

def random(request):
    pkL = []
    for value in Question.objects.values('pk'):
        pkL.append(value['pk'])
    pk1 = random.choice(pkL)
    
    return redirect('eithers:detail', pk1)

def comment_create(request, question_pk):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.question_id = question_pk
            comment.save()
    return redirect('eithers:detail', question_pk)