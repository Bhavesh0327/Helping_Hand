 
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

     def _create_user(self, email, name, password, **extra_details):

        if not email:
           raise ValueError('Invalid Email')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_details)
        user.set_password(password)
        user.save(using=self._db)
        return user

     def create_user(self, email, name, password, **extra_details):

        extra_details.setdefault('is_superuser', False)

        return self._create_user(email, name, password, **extra_details)

    
     def create_superuser(self, email, name, password, **extra_details):

        extra_details.setdefault('is_superuser', True)

        if extra_details.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self._create_user(email, name, password, **extra_details)

    