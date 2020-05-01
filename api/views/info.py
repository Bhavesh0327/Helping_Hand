from django.views.generic.base import View, RedirectView
from django.forms.models import model_to_dict
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.shortcuts import get_object_or_404

from api.models import District, State

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
        return {
            'districtId': districtId
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

