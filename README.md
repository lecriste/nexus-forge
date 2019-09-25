[Getting Started](#getting-started) |
[Installation](#installation) |
[Contributing](#contributing)

# Knowledge Graph Forge

The *Knowledge Graph Forge* is a framework building **a bridge between
data engineers, knowledge engineers, and (data) scientists** in the context
of knowledge graphs.

## Getting Started

See `examples` folder for notebooks and what a configuration file looks like.

```bash
# Forge

KnowledgeGraphForge.from_config(path: str, bucket: Optional[str] = None, token: Optional[str] = None)


# Resource(s)

Resource(**properties)
Resources(data: Union[Resource, List[Resource]], *resources)


# Transforming

map(data: Any, mapper: Callable, mapping: Mapping) -> ManagedData
reshape(data: ManagedData, keep: List[str], versioned: bool = False) -> ManagedData
as_json(data: ManagedData, expanded: bool = False, store_metadata: bool = False) -> Union[Dict, List[Dict]]
as_jsonld(data: ManagedData, compacted: bool = True, store_metadata: bool = False) -> Union[Dict, List[Dict]]
as_triples(data: ManagedData, store_metadata: bool = False) -> List[Tuple[str, str, str]]
as_dataframe(data: ManagedData, store_metadata: bool = False) -> DataFrame


# Modeling

prefixes() -> Dict[str, str]
types() -> List[str]
template(type: str, only_required: bool = False) -> None
validate(data: ManagedData) -> None
paths(type: str) -> PathsWrapper

> Handlers
Identifiers: format(*args) -> str
Ontologies: resolve(label: str, ontology: str, type: str = "Class",
  strategy: ResolvingStrategy = ResolvingStrategy.BEST_MATCH) -> Resource
Files: as_resource(path: str) -> LazyAction


# Storing

register(data: ManagedData) -> None
update(data: ManagedData) -> None
tag(data: ManagedData, value: str) -> None
deprecate(data: ManagedData) -> None


# Querying

retrieve(id: str, version: Optional[Union[int, str]] = None) -> Resource
search(*filters, **params) -> Resources
sparql(query: str) -> Resources
download(data: ManagedData, follow: str, path: str) -> None


# Specializations

> Resource
Dataset(forge: KnowledgeGraphForge, type: str = "Dataset", **properties)
  parts() -> Optional[Resources]
  with_parts(resources: ManagedData, versioned: bool = True) -> None
  files() -> Optional[DatasetFiles]
  with_files(path: DirPath) -> None


# Archetypes

Mapper(forge: KnowledgeGraphForge)
Mapping(mapping: str)
  load(path: str)
  save(path: str)

Model(source: Union[DirPath, URL, Store])
OntologyResolver(configuration: OntologyConfiguration)

Store(file_mapping: Optional[Union[Hjson, FilePath, URL]], bucket: Optional[str], token: Optional[str])


# Archetypes implementations

> Mapping
DictionaryMapping

> Mapper
DictionaryMapper
ResourceMapper [TODO]
TableMapper [TODO]

> Model
DemoModel
Neuroshapes [TODO]

> OntologyResolver
DemoResolver

> Store
DemoStore
RdfLibGraph [TODO]
BlueBrainNexus[TODO]
```

## Installation

Stable version

```bash
pip install kgforge
```

Upgrade to latest version

```bash
pip install --upgrade kgforge
```

Development version

```bash
pip install git+https://github.com/BlueBrain/kgforge
```

## Contributing

Please add `@pafonta` as reviewer if your Pull Request modifies `core`.

Setup

```bash
git clone https://github.com/BlueBrain/kgforge
pip install --editable kgforge[dev]
```

Manual check before committing

```bash
tox
```

### Styling

[PEP 8](https://www.python.org/dev/peps/pep-0008/),
[PEP 257](https://www.python.org/dev/peps/pep-0257/), and
[PEP 20](https://www.python.org/dev/peps/pep-0020/) must be followed.

### Releasing

```bash
# Setup
pip install --upgrade pip setuptools wheel twine

# Checkout
git checkout master
git pull upstream master

# Check
tox

# Tag
git tag -a v<x>.<y>.<z> HEAD
git push upstream v<x>.<y>.<z>

# Build
python setup.py sdist bdist_wheel

# Upload
twine upload dist/*

# Clean
rm -R build dist *.egg-info
```
