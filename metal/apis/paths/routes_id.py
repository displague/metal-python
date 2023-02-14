from metal.paths.routes_id.get import ApiForget
from metal.paths.routes_id.put import ApiForput
from metal.paths.routes_id.delete import ApiFordelete


class RoutesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
