import pytest
from django.core.exceptions import ValidationError

from ..models import Category

EXPECTED_CATEGORIES_COUNT = 2


@pytest.mark.django_db
def test_category_creation(sample_category):
    """Testa a criação de uma categoria."""
    assert sample_category.name == 'Design'
    assert sample_category.slug == 'design'
    assert sample_category.description == 'Design related projects'
    assert str(sample_category) == 'Design'
    assert sample_category.id == 1


@pytest.mark.django_db
def test_list_all_categories(sample_category):
    """Testa a listagem de todas as categorias."""
    Category.objects.create(
        name='Web Development',
        slug='web-development',
        description='Projects related to web development',
    )
    categories = Category.objects.all()
    assert Category.objects.count() == EXPECTED_CATEGORIES_COUNT
    assert categories[0].name == 'Design'
    assert categories[1].name == 'Web Development'
    assert str(categories[0]) == 'Design'
    assert str(categories[1]) == 'Web Development'
    assert categories[0].description == 'Design related projects'
    assert categories[1].description == 'Projects related to web development'
    assert categories[0].slug == 'design'
    assert categories[1].slug == 'web-development'


@pytest.mark.django_db
def test_category_detail(sample_category):
    """Testa a visualização de uma categoria."""
    assert Category.objects.get(id=1) == sample_category
    assert sample_category.name == 'Design'
    assert sample_category.slug == 'design'
    assert sample_category.description == 'Design related projects'
    assert str(sample_category) == 'Design'
    assert sample_category.id == 1


@pytest.mark.django_db
def test_category_update(sample_category):
    """Testa a atualização de uma categoria."""
    sample_category.name = 'Web Development'
    sample_category.slug = 'web-development'
    sample_category.description = 'Projects related to web development'
    sample_category.save()
    assert sample_category.name == 'Web Development'
    assert sample_category.slug == 'web-development'
    assert sample_category.description == 'Projects related to web development'
    assert str(sample_category) == 'Web Development'
    assert sample_category.id == 1


@pytest.mark.django_db
def test_category_delete(sample_category):
    """Testa a exclusão de uma categoria."""
    sample_category.delete()
    assert Category.objects.count() == 0


@pytest.mark.django_db
def test_category_verbose_name():
    """Testa os verbose names definidos no Meta"""
    assert Category._meta.verbose_name == 'Categoria'
    assert Category._meta.verbose_name_plural == 'Categorias'


@pytest.mark.django_db
def test_category_required_fields():
    """Testa que campos obrigatórios não podem ser nulos/vazios"""
    category = Category(name='', slug='', description='')
    with pytest.raises(ValidationError):
        category.full_clean()
