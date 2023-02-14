from metal.paths.bgp_sessions_id.get import ApiForget
from metal.paths.bgp_sessions_id.put import ApiForput
from metal.paths.bgp_sessions_id.delete import ApiFordelete


class BgpSessionsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
