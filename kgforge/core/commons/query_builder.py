#
# Blue Brain Nexus Forge is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Blue Brain Nexus Forge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
# General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Blue Brain Nexus Forge. If not, see <https://choosealicense.com/licenses/lgpl-3.0/>.
from typing import Any, Optional, List

from abc import abstractmethod, ABC

from kgforge.core.commons.attributes import repr_class
from kgforge.core.commons.context import Context


class QueryBuilder(ABC):
    def __repr__(self) -> str:
        return repr_class(self)

    @staticmethod
    @abstractmethod
    def build(
        schema: Any,
        resolvers: Optional[List["Resolver"]],
        context: Context,
        *filters,
        **params
    ) -> Any:
        pass
