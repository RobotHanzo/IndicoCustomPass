from indico.web.forms.base import IndicoForm
from wtforms import StringField, ColorField, BooleanField
from wtforms.validators import Regexp

from indico_custom_pass import _


class CustomPassSettingsForm(IndicoForm):
    apple_pass_background_color = ColorField(
        _('Apple Wallet pass background color'),
        description=_(
            'The background color of the Apple Wallet pass.'),
        validators=[Regexp(r'^#(?:[0-9a-fA-F]{3}){1,2}$', message=_('Invalid HEX color format.'))],
        default='#000000'
    )
    apple_pass_foreground_color = ColorField(
        _('Apple Wallet pass foreground color'),
        description=_(
            'The foreground color of the Apple Wallet pass.'),
        validators=[Regexp(r'^#(?:[0-9a-fA-F]{3}){1,2}$', message=_('Invalid HEX color format.'))],
        default='#ffffff'
    )
    apple_pass_label_color = ColorField(
        _('Apple Wallet pass label color'),
        description=_(
            'The label color of the Apple Wallet pass.'),
        validators=[Regexp(r'^#(?:[0-9a-fA-F]{3}){1,2}$', message=_('Invalid HEX color format.'))],
        default='#ffffff'
    )
    apple_pass_logo_text = StringField(
        _('Apple Wallet pass logo text'),
        description=_('The string displayed next to your logo on the Apple Wallet pass.'),
        default='Indico',
    )
    apple_pass_customize_logo = BooleanField(
        _('Customize Apple Wallet pass logo'),
        description=_(
            'If enabled, the logo on the Apple Wallet pass will be replaced with the image you specify below; WALLET_LOGO_URL from the official indico configuration will be ignored.'),
        default=False,
    )
    apple_pass_custom_logo_url = StringField(
        _('Apple Wallet pass custom logo URL'),
        description=_(
            'The URL of the custom logo to be used on the Apple Wallet pass. Must be a PNG image.\nPer apple docs: The logo image (logo.png) is displayed in the top left corner of the pass, next to the logo text. The allotted space is 160 x 50 points; in most cases it should be narrower.'),
        default='',
    )
    apple_pass_custom_icon_url = StringField(
        _('Apple Wallet pass custom icon URL'),
        description=_(
            'The URL of the custom icon to be used on the Apple Wallet pass. Must be a PNG image.\nPer apple docs: The icon (icon.png) is displayed when a pass is shown on the lock screen and by apps such as Mail when showing a pass attached to an email. The icon should measure 29 x 29 points.'),
        default='',
    )
    google_pass_background_color = ColorField(
        _('Google Wallet pass background color'),
        description=_(
            'The background color of the Google Wallet pass.'),
        validators=[Regexp(r'^#(?:[0-9a-fA-F]{3}){1,2}$', message=_('Invalid HEX color format.'))],
        default='#007cac'
    )
