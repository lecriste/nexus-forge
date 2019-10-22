# 
# Knowledge Graph Forge is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Knowledge Graph Forge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
# General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with Knowledge Graph Forge. If not, see <https://www.gnu.org/licenses/>.

from abc import ABC, abstractmethod
from typing import Callable, Dict, List, Union

from kgforge.core.commons.attributes import not_supported
from kgforge.core.commons.typing import DirPath, Hjson, ManagedData, URL, dispatch
from kgforge.core.resources import Resource, Resources
from kgforge.core.storing.store import Store
from kgforge.core.transforming import Mapping


class Model(ABC):

    # See demo_model.py in kgforge/specializations/models for an implementation.
    # Specializations should pass tests/specializations/models/demo_model.feature tests.

    def __init__(self, source: Union[DirPath, URL, Store]) -> None:
        # Model data could be loaded from a directory, an URL, or the store.
        # POLICY Model data access should be lazy: no general loading at object creation.
        # POLICY There could be caching but it should be aware of changes made in the source.
        self.source = source

    def prefixes(self) -> Dict[str, str]:
        not_supported()

    @abstractmethod
    def types(self) -> List[str]:
        # POLICY Should return managed types in their compacted form (i.e. not IRI nor CURIE).
        pass

    @abstractmethod
    def template(self, type: str, only_required: bool = False) -> Hjson:
        # POLICY Each nested typed resource should have its template included.
        # POLICY Template should be normalized by calling attributes.sort_attributes().
        # POLICY The order is then, recursively: 'type', 'id', properties sorted alphabetically.
        # POLICY The value of 'type' and the properties should be compacted (i.e. not IRI nor CURIE).
        pass

    def mappings(self, data_source: str) -> Dict[str, List[str]]:
        # POLICY Keys should be managed types with mappings for the given data source.
        # POLICY Values should be available mapping types for the resource type.
        not_supported()

    def mapping(self, type: str, data_source: str, mapping_type: Callable) -> Mapping:
        not_supported()

    def validate(self, data: ManagedData) -> None:
        # POLICY Resource _last_action and _validated should be updated.
        # POLICY Should notify of failures with exception ValidationError including a message.
        # POLICY Should call actions.run() to update the status and deal with exceptions.
        # POLICY Should print Resource _last_action before returning.
        dispatch(data, self._validate_many, self._validate_one)

    @abstractmethod
    def _validate_many(self, resources: Resources) -> None:
        # POLICY Follow validate() policies.
        pass

    @abstractmethod
    def _validate_one(self, resource: Resource) -> None:
        # POLICY Follow validate() policies.
        pass
