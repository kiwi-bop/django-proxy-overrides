from django.db.models import ForeignKey, OneToOneField
from .base import ProxyField


class ProxyForeignKey(ProxyField):
    def __init__(self, *args, **kwargs):
        super(ProxyForeignKey, self).__init__(ForeignKey(*args, **kwargs))


class ProxyOneToOneField(ProxyField):
    def __init__(self, *args, **kwargs):
        super(ProxyOneToOneField, self).__init__(OneToOneField(*args, **kwargs))
