from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from polls.models import Poll
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def vote(request,poll_id):
    p=get_object_or_404(Poll,pk=poll_id)
    try:
    	selected_choice=p.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
    	# Redisplay the poll voting form.
    	return render_to_response('detail.html',{
    		'poll':p,
    		'error_message':"You didn't select a choice"
    	},context_instance=RequestContext(request))
    else:
    	selected_choice.votes+=1
    	selected_choice.save()
    	return HttpResponseRedirect(reverse('poll_results',args=[p.id]))



