from django.views.generic.base import View, RedirectView
from django.forms.models import model_to_dict

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
        return '/api/info/1'

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
        return '/api/info/1'

