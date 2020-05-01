from django.views.generic.base import View
from django.forms.models import model_to_dict

class ServiceView(View):
    '''
    Get info about a given service
    '''
    def get(self, **kwargs):
        '''
        Get info about a service
        Parameters:
            serviceId (required)
        '''
        service_id = kwargs['serviceId']
        service = {}
        
        try:
            service = Service.objects.get(id=service_id)
        except:
            return error_response("Service with the id: {} does not exist".format(service_id))
        
        return {
            'service': model_to_dict(service)
        }

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
        service_info = request.POST.get('new_service')
        try:
            state = State.objects.get(name=service_info['name'])
            district = District.objects.get(state=state, name=service_info['district'])
            service_type = ServiceType.objects.get(service_type=service_info['service_type'])
            if Service.objects.filter(
                service_type=service_type, 
                district=district, 
                name=service_info['name'],
                address=service_info['address']).exists():
                return error_response("Service Exists")
            else:
                Service.objects.create(
                    district=district,
                    service_type=service_type,
                    name=service_info['name'],
                    address=service_info['address'],
                    open_time=service_info['open_time'],
                    close_time=service_info['close_time'],
                    is_active=service_info['is_active']
                )
                return {}
        except Exception as e:
            return error_response(e)
        return {}

    def post(self, request):
        '''
        Edit a service
        Parameters:
            body with service info, serviceId of the service to be changed
        '''
        return { status: 200, message: "success" }

    def delete(self, request):
        '''
        Delete a service
        Parameters:
            body with service info
        '''
        service_id = request.POST.get('service_id')
        try:
            Service.objects.get(id=service_id).delete()
            return {
                status: 200, 
                message: "Successfully deleted"
            }
        except Exception as e:
            return error_response(e)
        return {}