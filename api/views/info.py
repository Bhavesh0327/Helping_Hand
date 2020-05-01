from django.views.generic.base import View, RedirectView

from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.shortcuts import get_object_or_404

from api.models import District, State
from api.helpers.response_helper import error_response
from api.model_mixins.LocationMixin import to_dict

class DistrictView(View):
    '''
    Gets the information regarding a certain district
    '''

    def get(self, request, districtId):
        '''
        Parameters: 
            districtId (required)
        Returns information regarding a certain district
        '''
        try:
            district = District.objects.get(id=districtId)
            services = Service.objects.filter(district=district)
            conv_services = []
            for service in services:
                conv_services.append(to_dict(service))
            services = conv_services
        except:
            return error_response("District with the id: {} does not exist".format(districtId))
        
        return {
            'district': to_dict(district),
            'services': services
        }

class LocationRedirect(RedirectView):
    '''
    Redirect to district based on latitude and longitude
    '''

    def get_redirect_url(self, latitude, longitude):
        '''
        Parameters:
            latitude (required)
            longitude (required)
        '''
        ref_location = Point(float(latitude), float(longitude), srid=4326)
        closest_district = District.objects.order_by(Distance("location", ref_location))[0]
        return f'/api/info/{closest_district.id}/'

class NameRedirect(RedirectView):
    '''
    Redirect to district based on name
        This could be main view but problem arises when 2 districts have the same name
        If that is the case we'll have to do something
    '''

    def get_redirect_url(self, stateName, districtName):
        '''
        Parameters:
            stateName (required)
            districtName (required)
        '''
        state = get_object_or_404(State, name=stateName)
        district = get_object_or_404(District, state=state, name=districtName)
        return f'/api/info/{district.id}/'

