import pytest

from ..models import Category, Project


@pytest.fixture
def sample_category():
    return Category.objects.create(
        name='Design', slug='design', description='Design related projects'
    )


@pytest.fixture
def sample_project():
    return Project.objects.create(
        title='Project 1',
        slug='project-1',
        description='Project 1 description',
    )
