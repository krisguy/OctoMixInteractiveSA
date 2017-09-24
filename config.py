'''Mixer Interactive 2.0 config file'''

# Mixer Base URL
MIXER_URI = 'https://mixer.com/api/v2'

# OAuth endpoint used to get authorization code
OAUTH_URI = 'https://mixer.com/oauth/authorize'

# API OAuth enpoint used to get access token information
AUTHTOKEN_URI = 'https://mixer.com/api/v1/oauth/token'

# Redirect URL used by beam to get the authorization code
# This must be the same as the address you entered for Website
# when creating the oauth client
REDIRECT_URI = 'https://octoprint.krisguy.com'

# The ID Provided when OAuth app is created
CLIENT_ID = '231380d5d4791eff1b14647'

# Permission that the bot will be granted on the account
SCOPE = ('channel:details:self channel:update:self chat:chat chat:connect '
         'chat:giveaway_start interactive:robot:self user:details:self')
