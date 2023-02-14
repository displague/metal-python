from metal.paths.projects_id.get import ApiForget
from metal.paths.projects_id.put import ApiForput
from metal.paths.projects_id.delete import ApiFordelete


class ProjectsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
