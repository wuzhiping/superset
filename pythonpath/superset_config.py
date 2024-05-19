from flask_appbuilder.security.manager import AUTH_OAUTH

# Set the authentication type to OAuth
CSRF_ENABLED = False
ENABLE_PROXY_FIX = True

AUTH_TYPE = AUTH_OAUTH

OAUTH_PROVIDERS = [
    {   'name':'ABC',
        'token_key':'access_token', # Name of the token in the response of access_token_url
        'icon':'fa-address-card',   # Icon for the provider
        'remote_app': {
            'client_id':'myClientId',  # Client Id (Identify Superset application)
            'client_secret':'MySecret', # Secret for this Client Id (Identify Superset application)
            'client_kwargs':{
                'scope': 'read'               # Scope for the Authorization
            },
            'access_token_method':'POST',    # HTTP Method to call access_token_url
            'access_token_params':{        # Additional parameters for calls to access_token_url
                'client_id':'myClientId'
            },
            'jwks_uri':'https://abc.xyz.com/oauth2/ss_keys', # may be required to generate token
            'access_token_headers':{    # Additional headers for calls to access_token_url
                'Authorization': 'Basic Base64EncodedClientIdAndSecret'
            },
            'api_base_url':'https://abc.xyz.com/oauth2/',
            'access_token_url':'https://abc.xyz.com/oauth2/ss_token',
            'authorize_url':'https://abc.xyz.com/oauth2/ss_authorize'
        }
    }
]

# Will allow user self registration, allowing to create Flask users from Authorized User
AUTH_USER_REGISTRATION = True

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "Public"


#customer sso
from custom_sso_security_manager import CustomSsoSecurityManager
CUSTOM_SECURITY_MANAGER = CustomSsoSecurityManager

LANGUAGES = {
    "zh": {"flag": "cn", "name": "Chinese"},
    'en': {'flag': 'us', 'name': 'English'},
}
