from django.db import models
from django.contrib.auth.models import AbstractUser

from photo.models import Photo

from utilities.media_paths import avatar_path, cover_img_path


class User(AbstractUser):
    "Base the user class"

    GENDER = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    ACCOUNT_TYPES = [
        ("celesup", "Celesup"),
        ("support", "Supporter"),
        ("administrator", "Administrator"),
    ]

    id = models.CharField(max_length=100, primary_key=True, blank=True, unique=True)

    avatar = models.ImageField(
        upload_to=avatar_path,
        default="default/avatar.png",
        null=True,
        blank=True,
    )

    cover_img = models.FileField(
        upload_to=cover_img_path,
        default="default/cover.png",
        null=True,
        blank=True,
    )

    email = models.EmailField(max_length=160, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=100, unique=True, null=False, blank=False)

    city = models.CharField(null=True, blank=True, max_length=150)
    biography = models.CharField(max_length=350, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True, choices=GENDER)

    account_type = models.CharField(max_length=20, blank=True, choices=ACCOUNT_TYPES)

    email_privacy = models.BooleanField(default=True, blank=True)
    public_email = models.CharField(max_length=160, null=True, blank=True)
    notification_email = models.CharField(max_length=20, blank=True, null=True)
    secondary_email = models.EmailField(
        max_length=160, unique=True, blank=True, null=True
    )

    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    account_rating = models.BigIntegerField(default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "account_type"]

    def get_profile(self):
        return self.profile

    @property
    def profile(self):
        from administrator.models import Administrator
        from celebrity.models import Celebrity
        from supporter.models import Supporter

        user_type = self.account_type.lower()
        match user_type:
            case "celebrity":
                return Celebrity.objects.get(user=self)
            case "supporter":
                return Supporter.objects.get(user=self)
            case "administrator":
                return Administrator.objects.get(user=self)
            case _:
                return None

    @property
    def full_name(self):
        return self.name.capitalize() + " " + self.last_name.capitalize()

    @property
    def emails(self):
        em = []
        for email in [self.email, self.secondary_email]:
            if email.text:
                em.append(
                    {"is_primary": email.text == self.email.text, "email": email.text}
                )
        return em

    def __str__(self):
        return self.username[:25]

    def __repr__(self):
        return self.email


# class Email(models.Model):
#     text = models.EmailField(max_length=160, unique=True)
#     verified = models.BooleanField(default=False)

#     def __str__(self) -> str:
#         return self.text
