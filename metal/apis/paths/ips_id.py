from metal.paths.ips_id.get import ApiForget
from metal.paths.ips_id.delete import ApiFordelete
from metal.paths.ips_id.patch import ApiForpatch


class IpsId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
