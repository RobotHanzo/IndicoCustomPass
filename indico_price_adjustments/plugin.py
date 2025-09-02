from indico.core.plugins import IndicoPlugin
from indico.modules.events.registration.controllers import RegistrationFormMixin
from indico.modules.events.registration.forms import RegistrationFormEditForm, _check_if_payment_required
from indico_patcher import patch
from wtforms.fields import DecimalField
from wtforms.validators import Optional, NumberRange
from wtforms.widgets import NumberInput
from indico.core.db import db

from indico_price_adjustments import _


@patch(RegistrationFormEditForm)
class _RegistrationFormEditFormMixin:
    _price_fields = ('currency', 'base_price', 'extra_fee_for_guests')
    extra_fee_for_guests = DecimalField(_('Extra fee for guests'),
                                               [NumberRange(min=-999999999.99, max=999999999.99), Optional(),
                                                _check_if_payment_required],
                                               filters=[lambda x: x if x is not None else 0],
                                               widget=NumberInput(step='0.01'),
                                               description=_(
                                                   'An extra fee guests(non-logged-in users) have to pay when registering, negative amounts supported.'))

@patch(RegistrationFormMixin)
class _RegistrationFormMixin:
    extra_fee_for_guests = db.Column(
        db.Numeric(11, 2),  # max. 999999999.99
        nullable=False,
        default=0
    )


class PriceAdjustmentsPlugin(IndicoPlugin):
    """Price Adjustments

    Provides registration price adjustment options for non-logged-in users.
    """
    configurable = False

    def init(self):
        super().init()
        # self.inject_bundle('main.css', WPManageRegistration)
