from django.db import models
from proxy_overrides.related import ProxyForeignKey, ProxyOneToOneField
from proxy_overrides.base import ProxyField


class Foo(models.Model):
    a = models.IntegerField(default=1)


class FooProxy(Foo):
    class Meta:
        proxy = True


class FooChild(Foo):
    b = models.IntegerField(default=2)


class RelatedFK(models.Model):
    foo = models.ForeignKey(Foo, on_delete='null')


class RelatedFKProxy(RelatedFK):
    foo = ProxyForeignKey(FooProxy, on_delete='null')

    class Meta:
        proxy = True


class RelatedFKChildProxy(RelatedFK):
    foo = ProxyForeignKey(FooChild, on_delete='null')

    class Meta:
        proxy = True


class RelatedO2O(models.Model):
    foo = models.OneToOneField(Foo, on_delete='null')


class RelatedO2OProxy(RelatedO2O):
    foo = ProxyOneToOneField(FooProxy, on_delete='null')

    class Meta:
        proxy = True


class RelatedO2OChildProxy(RelatedO2O):
    foo = ProxyOneToOneField(FooChild, on_delete='null')

    class Meta:
        proxy = True
