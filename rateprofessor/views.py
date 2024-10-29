from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# from .forms import WaitTimeForm
from .ragmodel import get_data

@csrf_exempt
def get_professor_data(request):
    if request.method =="POST":
        data = json.loads(request.body.decode('utf-8'))
        user_url = data['url']
        result = get_data(user_url)
   
        # form = WaitTimeForm(data)
        # process_stats = form.cleaned_data['process_stats']
        # processing_steps = form.cleaned_data['processing_steps']
        # result = run_wait_time(process_stats, processing_steps)
        return JsonResponse(result, status = 200)

    else:
        return JsonResponse({'error': 'POST request required'}, status=400)
    
