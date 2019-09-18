from django.test import TestCase

from .models import (
    Foo,
    FooChild,
    FooProxy,
    RelatedFK,
    RelatedFKChildProxy,
    RelatedFKProxy,
    RelatedO2O,
    RelatedO2OChildProxy,
    RelatedO2OProxy,
)


class TestRelated(TestCase):
    def test_original_relation(self):
        foo = Foo.objects.create()
        RelatedFK.objects.create(foo=foo)

        foo = RelatedFK.objects.get()
        self.assertEqual(RelatedFK, foo.__class__)
        self.assertEqual(Foo, foo.foo.__class__)

    def test_fk_field_override(self):
        foo = Foo.objects.create()
        RelatedFK.objects.create(foo=foo)

        foo = RelatedFKProxy.objects.get()

        self.assertEqual(
            RelatedFKProxy,
            foo.__class__
        )

        self.assertEqual(
            FooProxy,
            foo.foo.__class__
        )

    def test_fk_child_override_child(self):
        foo_child = FooChild.objects.create()
        RelatedFK.objects.create(foo=foo_child)

        foo = RelatedFKChildProxy.objects.get()

        self.assertEqual(
            RelatedFKChildProxy,
            foo.__class__
        )

        self.assertEqual(
            FooChild,
            foo.foo.__class__
        )

        assert foo.foo.a == 1
        assert foo.foo.b == 2

    def test_reverse_fk_field_override(self):
        foo = Foo.objects.create()
        RelatedFK.objects.create(foo=foo)

        foo = FooProxy.objects.get()

        self.assertEqual(
            FooProxy,
            foo.__class__
        )

        self.assertEqual(
            RelatedFKProxy,
            foo.relatedfk_set.model
        )

    def test_reverse_fk_field_child_child(self):
        foo_child = FooChild.objects.create()
        RelatedFK.objects.create(foo=foo_child)

        foo_child = FooChild.objects.get()

        self.assertEqual(
            FooChild,
            foo_child.__class__
        )

        self.assertEqual(
            RelatedFKChildProxy,
            foo_child.relatedfk_set.model
        )

    def test_o2o_field_override(self):
        foo = Foo.objects.create()
        RelatedO2O.objects.create(foo=foo)

        foo = RelatedO2OProxy.objects.get()

        self.assertEqual(
            RelatedO2OProxy,
            foo.__class__
        )

        self.assertEqual(
            FooProxy,
            foo.foo.__class__
        )

    def test_o2o_child_override_child(self):
        foo_child = FooChild.objects.create()
        RelatedO2O.objects.create(foo=foo_child)

        foo = RelatedO2OChildProxy.objects.get()

        self.assertEqual(
            RelatedO2OChildProxy,
            foo.__class__
        )

        self.assertEqual(
            FooChild,
            foo.foo.__class__
        )

        assert foo.foo.a == 1
        assert foo.foo.b == 2

    def test_reverse_o2o_field_override(self):
        foo = Foo.objects.create()
        RelatedO2O.objects.create(foo=foo)

        foo = FooProxy.objects.get()

        self.assertEqual(
            FooProxy,
            foo.__class__
        )

        self.assertEqual(
            RelatedO2OProxy,
            foo.relatedo2o.model
        )

    def test_reverse_o2o_field_child_child(self):
        foo_child = FooChild.objects.create()
        RelatedO2O.objects.create(foo=foo_child)

        foo_child = FooChild.objects.get()

        self.assertEqual(
            FooChild,
            foo_child.__class__
        )

        self.assertEqual(
            RelatedO2OChildProxy,
            foo_child.relatedo2o.model
        )

    def test_exception_if_same_relation(self):
        with self.assertRaises(TypeError):
            from proxy_overrides.related import ProxyForeignKey

            class RelatedFKNewProxy(RelatedFK):
                foo = ProxyForeignKey(FooProxy)
