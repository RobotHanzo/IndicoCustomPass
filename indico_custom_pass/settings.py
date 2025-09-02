from indico.web.forms.base import IndicoForm
from wtforms import StringField, ColorField
from wtforms.validators import Regexp

from indico_custom_pass import _


class CustomPassSettingsForm(IndicoForm):
    apple_pass_background_color = ColorField(
        _('Apple Wallet pass background color'),
        description=_(
            'The background color of the Apple Wallet pass in HEX format (e.g. #000000 for black, #ffffff for white).'),
        validators=[Regexp(r'^#(?:[0-9a-fA-F]{3}){1,2}$', message=_('Invalid HEX color format.'))],
        default='#000000'
    )
    apple_pass_foreground_color = ColorField(
        _('Apple Wallet pass foreground color'),
        description=_(
            'The foreground color of the Apple Wallet pass in HEX format (e.g. #000000 for black, #ffffff for white).'),
        validators=[Regexp(r'^#(?:[0-9a-fA-F]{3}){1,2}$', message=_('Invalid HEX color format.'))],
        default='#ffffff'
    )
    apple_pass_label_color = ColorField(
        _('Apple Wallet pass label color'),
        description=_(
            'The label color of the Apple Wallet pass in HEX format (e.g. #000000 for black, #ffffff for white).'),
        validators=[Regexp(r'^#(?:[0-9a-fA-F]{3}){1,2}$', message=_('Invalid HEX color format.'))],
        default='#ffffff'
    )
    apple_pass_organization_name = StringField(
        _('Apple Wallet pass organization name'),
        description=_('The organization name displayed on the Apple Wallet pass.'),
        default='Indico',
    )
    google_pass_background_color = ColorField(
        _('Google Wallet pass background color'),
        description=_(
            'The background color of the Google Wallet pass in HEX format (e.g. #000000 for black, #ffffff for white).'),
        validators=[Regexp(r'^#(?:[0-9a-fA-F]{3}){1,2}$', message=_('Invalid HEX color format.'))],
        default='#007cac'
    )
