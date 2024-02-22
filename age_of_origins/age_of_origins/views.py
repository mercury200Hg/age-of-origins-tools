import time

from django.http import HttpResponse
import json


def health(request):
    response_data = {
        'result': 'success',
        'status': 'healthy',
        'timestamp': time.time(),
        'status_code': 200
    }
    return HttpResponse(json.dumps(response_data, indent=4), content_type="application/json", status=200)
