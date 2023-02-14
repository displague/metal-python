from metal.paths.organizations_id.get import ApiForget
from metal.paths.organizations_id.put import ApiForput
from metal.paths.organizations_id.delete import ApiFordelete


class OrganizationsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
