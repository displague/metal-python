from metal.paths.transfers_id.get import ApiForget
from metal.paths.transfers_id.put import ApiForput
from metal.paths.transfers_id.delete import ApiFordelete


class TransfersId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
