from metal.paths.emails_id.get import ApiForget
from metal.paths.emails_id.put import ApiForput
from metal.paths.emails_id.delete import ApiFordelete


class EmailsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
