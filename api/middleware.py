from django.middleware.common import CommonMiddleware
import json
from django.http import JsonResponse


class JsonMiddleware(CommonMiddleware):
    def process_request(self, request):
        super(JsonMiddleware, self).process_request(request)
        if request.content_type == 'application/json':
            request.json = json.loads(request.body)

    def process_response(self, request, response):
        if isinstance(response, dict):
            status = 200
            if 'status' in response:
                status = response['status']
                del response['status']
            response = JsonResponse(response, status=status)
        return super(JsonMiddleware, self).process_response(request, response)
