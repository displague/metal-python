from metal.paths.invitations_id.get import ApiForget
from metal.paths.invitations_id.put import ApiForput
from metal.paths.invitations_id.delete import ApiFordelete


class InvitationsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
