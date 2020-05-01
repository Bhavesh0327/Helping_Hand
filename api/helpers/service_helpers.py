from api.models import DistrictEditor

def is_user_eligible(user, district):
    return user.is_superuser or DistrictEditor.objects.filter(user=user, district=district).exists()