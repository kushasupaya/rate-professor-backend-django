from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import ProfessorDataForm
from .ragmodel import get_data

@csrf_exempt
def get_professor_data(request):
    if request.method =="POST":
        data = json.loads(request.body.decode('utf-8'))
        form = ProfessorDataForm(data)
        if form.is_valid():
            user_url = form.cleaned_data['url']
            result = get_data(url=user_url)
            return JsonResponse(result, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({'error': 'POST request required'}, status=400)
    
