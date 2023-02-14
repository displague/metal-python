from metal.paths.licenses_id.get import ApiForget
from metal.paths.licenses_id.put import ApiForput
from metal.paths.licenses_id.delete import ApiFordelete


class LicensesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
