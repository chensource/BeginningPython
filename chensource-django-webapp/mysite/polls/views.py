from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        '''Return the last five id question'''
        return Question.objects.order_by('id')[:5]


class DetailView(generic.DeleteView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# from django.template import loader
# Create your views here.
# def index(request):
#     # return HttpResponse('hello,world! you\'re at the polls index')
#     # latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     # context = {'latest_question_list': latest_question_list}
#     # return HttpResponse(template.render(context, request))
#     latest_question_list = Question.objects.order_by('id')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
#
# def detail(request, question_id):
#     # return HttpResponse('You\'er looking at question %s' % question_id)
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404('Question does not exits')
#     # return render(request, 'polls/detail.html', {'question': question})
#
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     # response = 'You\'re looking at the results of question %s.'
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
def vote(request, question_id):
    # return HttpResponse('You\'re voting on question %s.' % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'You don\'t select a choice'
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(
            reverse(
                'polls:results', args=(question.id, )))
