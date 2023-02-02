from django.urls import path


from .login.authenticate_user import AuthenticateUser
from .register.signup_account import SignupAccount
from .register.verification import VerifyUserAccount
from .logout.signout_user import LogoutAuthentication
from .login.refresh_token import RefreshAuthenticationTokens

auth_urls_patterns = [
    path("login", AuthenticateUser.as_view()),
    path("signup", SignupAccount.as_view()),
    path("account/verify", VerifyUserAccount.as_view()),
    path("logout", LogoutAuthentication.as_view()),
    path("refresh/auth/tokens", RefreshAuthenticationTokens.as_view()),
]
