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
        'apple_pass_organization_name': 'Indico',
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
        p.organizationName = CustomPassPlugin.settings.get('apple_pass_organization_name')
        return p


@patch(GoogleWalletManager)
class GoogleWalletManagerMixin(GoogleWalletManager):
    def build_ticket_object_data(self, registration):
        data = super().build_ticket_object_data(registration)
        data['hexBackgroundColor'] = CustomPassPlugin.settings.get('google_pass_background_color')
        return data
