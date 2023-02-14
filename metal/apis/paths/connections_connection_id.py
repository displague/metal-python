from metal.paths.connections_connection_id.get import ApiForget
from metal.paths.connections_connection_id.put import ApiForput
from metal.paths.connections_connection_id.delete import ApiFordelete


class ConnectionsConnectionId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
