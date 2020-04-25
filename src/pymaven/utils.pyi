from typing import (
    Any,
    Callable,
    List,
    MutableSequence,
    Optional,
    TextIO,
    TypeVar,
    Union,
)
from io import IOBase

_T = TypeVar("_T")
_F = TypeVar("_F", bound=Callable[..., Any])

def _first_of_each(*args: Any, **kwargs: Any) -> List: ...
def cmp(x: _T, y: _T) -> int: ...
def memoize(name: str) -> Callable[[_F], _F]: ...
def pad(
    seq: MutableSequence, target_length: int, padding: Optional[int] = ...
) -> MutableSequence: ...
def parse_source(source: Union[IOBase, str]) -> TextIO: ...
def urljoin(*parts: str) -> str: ...
