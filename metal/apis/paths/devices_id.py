from metal.paths.devices_id.get import ApiForget
from metal.paths.devices_id.put import ApiForput
from metal.paths.devices_id.delete import ApiFordelete


class DevicesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
