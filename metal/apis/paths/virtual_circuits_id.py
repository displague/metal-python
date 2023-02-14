from metal.paths.virtual_circuits_id.get import ApiForget
from metal.paths.virtual_circuits_id.put import ApiForput
from metal.paths.virtual_circuits_id.delete import ApiFordelete


class VirtualCircuitsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
