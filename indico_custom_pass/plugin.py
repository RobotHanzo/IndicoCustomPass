from indico.core.plugins import IndicoPlugin
from indico.modules.events.registration import GoogleWalletManager
from indico.modules.events.registration.wallets.apple import AppleWalletManager
from indico_patcher import patch

from indico_custom_pass.settings import CustomPassSettingsForm


class CustomPassPlugin(IndicoPlugin):
    """Custom Pass

    Grants admins the ability to customize Indico Google Wallet & Apple Pay passes.
    """
    configurable = True
    settings_form = CustomPassSettingsForm
    default_settings = {
        'apple_pass_background_color': '#007cac',
        'apple_pass_foreground_color': '#ffffff',
        'apple_pass_label_color': '#ffffff',
        'apple_pass_logo_text': 'Indico',
        'apple_pass_customize_logo': False,
        'apple_pass_custom_icon_url': '',
        'apple_pass_custom_logo_url': '',
        'google_pass_background_color': '#007cac'
    }

    def init(self):
        super().init()


@patch(AppleWalletManager)
class AppleWalletManagerMixin(AppleWalletManager):
    def build_pass_object(self, registration):
        p = super().build_pass_object(registration)
        p.backgroundColor = CustomPassPlugin.settings.get('apple_pass_background_color')
        p.foregroundColor = CustomPassPlugin.settings.get('apple_pass_foreground_color')
        p.labelColor = CustomPassPlugin.settings.get('apple_pass_label_color')
        p.logoText = CustomPassPlugin.settings.get('apple_pass_logo_text')
        if bool(CustomPassPlugin.settings.get('apple_pass_customize_logo')):
            # Per apple docs:
            # The dimensions given above are all in points. On a non-Retina display, each point equals exactly 1 pixel.
            # On a Retina display, there are 2 or 3 pixels per point, depending on the device.
            # To support all screen sizes and resolutions, provide the original, @2x, and @3x versions of your art.
            # TODO
            # This is a easy way to fool apple to render the logo at higher resolutions, however the user shall have the
            # choice to provide logos for different aspect ratios, to allow for more efficient ticket sizes
            p.add_file_from_url('icon.png', CustomPassPlugin.settings.get('apple_pass_custom_icon_url'))
            p.add_file_from_url('icon@2x.png', CustomPassPlugin.settings.get('apple_pass_custom_icon_url'))
            p.add_file_from_url('icon@3x.png', CustomPassPlugin.settings.get('apple_pass_custom_icon_url'))
            p.add_file_from_url('logo.png', CustomPassPlugin.settings.get('apple_pass_custom_logo_url'))
            p.add_file_from_url('logo@2x.png', CustomPassPlugin.settings.get('apple_pass_custom_logo_url'))
            p.add_file_from_url('logo@3x.png', CustomPassPlugin.settings.get('apple_pass_custom_logo_url'))
        return p


@patch(GoogleWalletManager)
class GoogleWalletManagerMixin(GoogleWalletManager):
    def build_ticket_object_data(self, registration):
        data = super().build_ticket_object_data(registration)
        data['hexBackgroundColor'] = CustomPassPlugin.settings.get('google_pass_background_color')
        return data
