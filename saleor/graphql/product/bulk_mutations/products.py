import graphene

from ....product import models
from ...core.mutations import BaseBulkMutation, ModelBulkDeleteMutation
from ..mutations.base import ProductErrorMixin


class CategoryBulkDelete(ProductErrorMixin, ModelBulkDeleteMutation):
    class Arguments:
        ids = graphene.List(
            graphene.ID, required=True, description="List of category IDs to delete."
        )

    class Meta:
        description = "Deletes categories."
        model = models.Category
        permissions = ("product.manage_products",)


class CollectionBulkDelete(ProductErrorMixin, ModelBulkDeleteMutation):
    class Arguments:
        ids = graphene.List(
            graphene.ID, required=True, description="List of collection IDs to delete."
        )

    class Meta:
        description = "Deletes collections."
        model = models.Collection
        permissions = ("product.manage_products",)


class CollectionBulkPublish(ProductErrorMixin, BaseBulkMutation):
    class Arguments:
        ids = graphene.List(
            graphene.ID,
            required=True,
            description="List of collections IDs to (un)publish.",
        )
        is_published = graphene.Boolean(
            required=True,
            description="Determine if collections will be published or not.",
        )

    class Meta:
        description = "Publish collections."
        model = models.Collection
        permissions = ("product.manage_products",)

    @classmethod
    def bulk_action(cls, queryset, is_published):
        queryset.update(is_published=is_published)


class ProductBulkDelete(ProductErrorMixin, ModelBulkDeleteMutation):
    class Arguments:
        ids = graphene.List(
            graphene.ID, required=True, description="List of product IDs to delete."
        )

    class Meta:
        description = "Deletes products."
        model = models.Product
        permissions = ("product.manage_products",)


class ProductVariantBulkDelete(ProductErrorMixin, ModelBulkDeleteMutation):
    class Arguments:
        ids = graphene.List(
            graphene.ID,
            required=True,
            description="List of product variant IDs to delete.",
        )

    class Meta:
        description = "Deletes product variants."
        model = models.ProductVariant
        permissions = ("product.manage_products",)


class ProductTypeBulkDelete(ProductErrorMixin, ModelBulkDeleteMutation):
    class Arguments:
        ids = graphene.List(
            graphene.ID,
            required=True,
            description="List of product type IDs to delete.",
        )

    class Meta:
        description = "Deletes product types."
        model = models.ProductType
        permissions = ("product.manage_products",)


class ProductImageBulkDelete(ProductErrorMixin, ModelBulkDeleteMutation):
    class Arguments:
        ids = graphene.List(
            graphene.ID,
            required=True,
            description="List of product image IDs to delete.",
        )

    class Meta:
        description = "Deletes product images."
        model = models.ProductImage
        permissions = ("product.manage_products",)


class ProductBulkPublish(ProductErrorMixin, BaseBulkMutation):
    class Arguments:
        ids = graphene.List(
            graphene.ID, required=True, description="List of products IDs to publish."
        )
        is_published = graphene.Boolean(
            required=True, description="Determine if products will be published or not."
        )

    class Meta:
        description = "Publish products."
        model = models.Product
        permissions = ("product.manage_products",)

    @classmethod
    def bulk_action(cls, queryset, is_published):
        queryset.update(is_published=is_published)
