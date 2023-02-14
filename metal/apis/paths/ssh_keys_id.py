from metal.paths.ssh_keys_id.get import ApiForget
from metal.paths.ssh_keys_id.put import ApiForput
from metal.paths.ssh_keys_id.delete import ApiFordelete


class SshKeysId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
