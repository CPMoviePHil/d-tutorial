from django.shortcuts import render, Http404, get_object_or_404, HttpResponseRedirect, reverse
from .models import Questions, Answers
from django.views import generic
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Questions.objects.order_by('-publication_date')[:5]


class DetailView(generic.DetailView):
    model = Questions
    template_name = 'poll/detail.html'
    context_object_name = 'q'


class ResultsView(generic.DetailView):
    model = Questions
    context_object_name = 'q'
    template_name = 'poll/result.html'


def index(request):
    latest_question_list = Questions.objects.order_by('-publication_date')[:5]
    fuckyou = "fuckyou"
    return render(request, 'poll/index.html', {'latest_question_list': latest_question_list, "fuckyou":fuckyou})


def detail(request, question_id):
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404('question is not found')
    return render(request, "poll/detail.html", {"q": question})


def detail2(request, qid):
    try:
        question = get_object_or_404(Questions, pk=qid)
    except Questions.DoesNotExist:
        raise Http404("Question not found!")
    return render(request, 'poll/detail.html', {"q": question})


def results(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'poll/result.html', {'q': question})


def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.answers_set.get(pk=request.POST['answer'])
    except (KeyError, Answers.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll/detail.html', {
            'q': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('for_poll_app:results', args=(question.id,)))


def forNotFound():
    pass
