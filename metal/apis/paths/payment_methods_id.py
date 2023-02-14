from metal.paths.payment_methods_id.get import ApiForget
from metal.paths.payment_methods_id.put import ApiForput
from metal.paths.payment_methods_id.delete import ApiFordelete


class PaymentMethodsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
