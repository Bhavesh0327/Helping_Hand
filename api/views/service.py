from django.views.generic.base import View
from django.forms.models import model_to_dict

class ServiceView(View):
    '''
    Get info about a given service
    '''
    def get(self, request, serviceId):
        '''
        Get info about a service
        Parameters:
            serviceId (required)
        '''
        return {}

class EditServiceView(View):
    '''
    Add, Edit and Delete a given service
        - If user is admin / district editor continue
        - Else create request
    '''

    def put(self, request):
        '''
        Add a service
        Parameters:
            body with service info
        '''
        return { status: 200, message: "success" }

    def post(self, request):
        '''
        Edit a service
        Parameters:
            body with service info
        '''
        return { status: 200, message: "success" }

    def delete(self, request):
        '''
        Delete a service
        Parameters:
            body with service info
        '''
        return { status: 200, message: "success" }