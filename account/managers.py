from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    
    def create_superuser(self, sub, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_default', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff=True ')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is superuser=True")
        return self.create_superuser(sub, password, **extra_fields)
