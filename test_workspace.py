from workspace import create_workspace
from utils import bin_to_dict
from config import config


def test_create_workspace():
    response = create_workspace('foo')
    assert response.status_code == 201, 'Failed to get valid response create'
    data_dict = bin_to_dict(response)
    expected_keys = set(config.workspace.create_keys)
    data_keys = set(data_dict.keys())
    diff_keys = expected_keys - data_keys
    assert not len(diff_keys), f"Missing fields in response: {diff_keys}"
    #here I should remove the workspace for cleanup