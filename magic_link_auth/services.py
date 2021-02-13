from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode


def get_magic_link(user, scheme, host):
    """
    Function to create magic link url.
    """
    user_id = urlsafe_base64_encode(
        str(user.id).encode())
    token = default_token_generator.make_token(user)
    base_url =f'{scheme}://{host}/login/token/'
    query_params = f'?uidb64={user_id}&token={token}'
    return base_url + query_params