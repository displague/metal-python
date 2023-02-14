from metal.paths.vrfs_id.get import ApiForget
from metal.paths.vrfs_id.put import ApiForput
from metal.paths.vrfs_id.delete import ApiFordelete


class VrfsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
