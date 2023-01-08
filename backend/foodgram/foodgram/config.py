RESTRICTED_USERNAME = 'me'

DATE_TIME_FORMAT = '%d/%m/%Y %H:%M'

MIN_USERNAME_LEN = 3
MAX_USERNAME_LEN = 50

TRANSLATER_DICT = str.maketrans(
    'qwertyuiop[]asdfghjkl;\'zxcvbnm,./',
    'йцукенгшщзхъфывапролджэячсмитьбю.'
)

ADD_METHODS = ('GET', 'POST',)
DEL_METHODS = ('DELETE',)
ACTION_METHODS = [i.lower() for i in (ADD_METHODS + DEL_METHODS)]
UPDATE_METHODS = ('PUT', 'PATCH')

SYMBOL_TRUE_SEARCH = ('1', 'true',)
SYMBOL_FALSE_SEARCH = ('0', 'false',)

LEN_HEX_COLOR = 6
MAX_LEN_EMAIL_FIELD = 254
MAX_LEN_RECIPES_CHARFIELD = 200
MAX_LEN_RECIPES_TEXTFIELD = 5000
MAX_LEN_USERS_CHARFIELD = 150

# help-text для email
USERS_HELP_EMAIL = (
    'Обязательно для заполнения. '
    f'Максимум {MAX_LEN_EMAIL_FIELD} букв.'
)
# help-text для username
USERS_HELP_UNAME = (
    'Обязательно для заполнения. '
    f'От {MIN_USERNAME_LEN} до {MAX_USERNAME_LEN} букв.'
)

# help-text для first_name/last_name
USERS_HELP_FNAME = (
    'Обязательно для заполнения.'
    f'Максимум {MAX_USERNAME_LEN} букв.'
)
