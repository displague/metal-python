from metal.paths.memberships_id.get import ApiForget
from metal.paths.memberships_id.put import ApiForput
from metal.paths.memberships_id.delete import ApiFordelete


class MembershipsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
