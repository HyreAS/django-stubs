from typing import Any, Callable, List, Optional, Type, Union, Tuple

from django.core.checks.messages import Error
from django.core.files.base import File
from django.core.files.images import ImageFile
from django.core.files.storage import FileSystemStorage, Storage
from django.db.models.base import Model

from django.db.models.fields import Field
from django.forms import fields as form_fields

BLANK_CHOICE_DASH: List[Tuple[str, str]] = ...

class FieldFile(File):
    instance: Model = ...
    field: FileField = ...
    storage: FileSystemStorage = ...
    def __init__(self, instance: Model, field: FileField, name: Optional[str]) -> None: ...
    file: Any = ...
    @property
    def path(self) -> str: ...
    @property
    def url(self) -> str: ...
    @property
    def size(self) -> int: ...
    def save(self, name: str, content: File, save: bool = ...) -> None: ...
    def delete(self, save: bool = ...) -> None: ...
    @property
    def closed(self) -> bool: ...

class FileDescriptor:
    field: FileField = ...
    def __init__(self, field: FileField) -> None: ...
    def __get__(self, instance: Optional[Model], cls: Type[Model] = ...) -> Union[FieldFile, FileDescriptor]: ...
    def __set__(self, instance: Model, value: Optional[Any]) -> None: ...

class FileField(Field):
    attr_class: Any = ...
    descriptor_class: Any = ...
    description: Any = ...
    storage: Any = ...
    upload_to: Any = ...
    def __init__(
        self,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        upload_to: Union[Callable, str] = ...,
        storage: Optional[Storage] = ...,
        **kwargs: Any
    ) -> None: ...
    def check(self, **kwargs: Any) -> List[Error]: ...
    def deconstruct(self) -> Any: ...
    def get_internal_type(self) -> str: ...
    def get_prep_value(self, value: Union[FieldFile, str]) -> str: ...
    def pre_save(self, model_instance: Model, add: bool) -> FieldFile: ...
    def generate_filename(self, instance: Optional[Model], filename: str) -> str: ...
    def save_form_data(self, instance: Model, data: Optional[Union[bool, File, str]]) -> None: ...
    def formfield(self, **kwargs: Any) -> form_fields.FileField: ...

class ImageFileDescriptor(FileDescriptor):
    field: ImageField
    def __set__(self, instance: Model, value: Optional[str]) -> None: ...

class ImageFieldFile(ImageFile, FieldFile):
    field: ImageField
    def delete(self, save: bool = ...) -> None: ...

class ImageField(FileField):
    def __init__(
        self,
        verbose_name: Optional[str] = ...,
        name: Optional[str] = ...,
        width_field: Optional[str] = ...,
        height_field: Optional[str] = ...,
        **kwargs: Any
    ) -> None: ...
    def check(self, **kwargs: Any) -> List[Any]: ...
    def deconstruct(self) -> Any: ...
    def update_dimension_fields(self, instance: Model, force: bool = ..., *args: Any, **kwargs: Any) -> None: ...
    def formfield(self, **kwargs: Any) -> form_fields.ImageField: ...
