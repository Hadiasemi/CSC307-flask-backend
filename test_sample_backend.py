import pytest
import sample_backend
from model_mongodb import User


def test_find_users_by_name_success():
    expected = ([
        {
            '_id': '6009dc44f29c1feab0ec29a4',
            'name': 'Jeff',
            'job': 'Bouncer',
        },
        {
            '_id': '6009dfa508f2eca30c87d56c',
            'name': 'Mac',
            'job': 'Professor',
        },
    ])

    assert User().find_by_name("Mac") == expected


def test_find_users_by_name_fail():
    expected = []
    assert User().find_by_name("Jeff") == expected
