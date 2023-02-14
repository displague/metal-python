# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from metal.paths.payment_methods_id import Api

from metal.paths import PathValues

path = PathValues.PAYMENTMETHODS_ID