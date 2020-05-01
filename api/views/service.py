from django.views.generic.base import View
from django.contrib.auth.models import User

from api.model_mixins.LocationMixin import to_dict
from api.models import Service, District, State, ServiceType, ServiceChangeRequest, DistrictEditor
from api.helpers.response_helper import error_response

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
        try:
            service = Service.objects.get(id=serviceId)
        except:
            return error_response("Service with the id: {} does not exist".format(serviceId))
        
        return {
            'service': to_dict(service)
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
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)

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

            location = Point(float(service_info['latitude']), float(service_info['longitude']))
            if is_user_eligible(user, district):
                is_active = true
            else:
                is_active = false
            
            service = Service.objects.create(
                        district=district,
                        service_type=service_type,
                        name=service_info['name'],
                        address=service_info['address'],
                        location=location,
                        open_time=service_info['open_time'],
                        close_time=service_info['close_time'],
                        is_active=is_active
                    )
            
            if not is_active:
                ServiceChangeRequest.objects.create(
                    user=user,
                    changes=service
                )
        except Exception as e:
            return error_response(e)
        return {}

    def post(self, request):
        '''
        Edit a service
        Parameters:
            body with service info, serviceId of the service to be changed
        '''
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        service_id = request.POST.get('service_id')
        service_info = request.POST.get('service_info')

        try:
            service = Service.objects.get(pk=service_id)
            district = service.district
            service_type = ServiceType.objects.get(service_type=service_info['service_type'])
            if is_user_eligible(user, district):
                is_active = true
            else:
                is_active = false
            location = Point(float(service_info['latitude']), float(service_info['longitude']))
            new_service = Service.objects.create(
                        district=district,
                        service_type=service_type,
                        name=service_info['name'],
                        address=service_info['address'],
                        location=location,
                        open_time=service_info['open_time'],
                        close_time=service_info['close_time'],
                        is_active=is_active
                    )
            if not is_active:
                ServiceChangeRequest.objects.create(
                    user=user,
                    changes=new_service,
                    service=service
                )
            else:
                service.is_active = False
                service.save()
        except Exception as e:
            return error_response(e)
        return {}

    def delete(self, request):
        '''
        Delete a service
        Parameters:
            body with service info
        '''
        service_id = request.POST.get('service_id')
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
    
        try:
            service = Service.objects.get(pk=service_id)
            if is_user_eligible(user, service.district):
                service.delete()
            else:
                ServiceChangeRequest.objects.create(
                    user=user,
                    service=service
                )
        except Exception as e:
            return error_response(e)
        return {}