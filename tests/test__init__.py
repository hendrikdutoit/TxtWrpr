'''Testing __init__()'''

# import configparser
from pathlib import Path

# import sys
# import apputils
import tempfile
import beetools
from txtwrpr import TxtWrpr
from conftest import SRC_DATA_01, PARSED_DATA_01, SRC_FIELD_DEF_01, create_test_file


_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = beetools.Archiver(_name, _VERSION, __doc__, Path(_path))


def test__init__simple():
    '''Testing __init__simple()'''
    t_wrpr = TxtWrpr(
        _name,
        0,
        SRC_FIELD_DEF_01,
        # p_src = SOURCE_DATA,
        p_has_header=True,
        p_verbose=True,
    )
    assert not t_wrpr.exp_data
    assert not t_wrpr.exp_field_def
    assert not t_wrpr.exp_pth
    assert t_wrpr.has_header
    assert t_wrpr.key_idx == 0
    assert t_wrpr.member_cntr == 0
    assert t_wrpr.src_field_def == SRC_FIELD_DEF_01
    assert not t_wrpr.src_data
    assert not t_wrpr.src_pth
    assert not t_wrpr.parsed_data
    assert t_wrpr.success
    assert t_wrpr.verbose


def test__init__list():
    '''Testing __init__list()'''
    t_wrpr = TxtWrpr(
        _name, 0, SRC_FIELD_DEF_01, p_src=SRC_DATA_01, p_has_header=True, p_verbose=True
    )
    assert not t_wrpr.exp_data
    assert not t_wrpr.exp_field_def
    assert not t_wrpr.exp_pth
    assert t_wrpr.has_header
    assert t_wrpr.key_idx == 0
    assert t_wrpr.member_cntr == 10
    assert t_wrpr.src_field_def == SRC_FIELD_DEF_01
    assert t_wrpr.src_data == SRC_DATA_01
    assert isinstance(t_wrpr.src_pth, type(list))
    assert t_wrpr.parsed_data == PARSED_DATA_01
    assert t_wrpr.success
    assert t_wrpr.verbose


def test__init__file():
    '''Testing __init__file()'''
    data_fldr = Path(tempfile.TemporaryDirectory().name)
    data_fldr.mkdir()
    src_pth = data_fldr / 'txtFile01.txt'
    create_test_file(src_pth)
    t_wrpr = TxtWrpr(
        _name, 0, SRC_FIELD_DEF_01, p_src=src_pth, p_has_header=True, p_verbose=True
    )
    beetools.rm_tree(data_fldr)
    assert not t_wrpr.exp_data
    assert not t_wrpr.exp_field_def
    assert not t_wrpr.exp_pth
    assert t_wrpr.has_header
    assert t_wrpr.key_idx == 0
    assert t_wrpr.member_cntr == 10
    assert t_wrpr.src_field_def == SRC_FIELD_DEF_01
    assert t_wrpr.src_data == SRC_DATA_01
    assert isinstance(t_wrpr.src_pth, Path)
    assert t_wrpr.parsed_data == PARSED_DATA_01
    assert t_wrpr.success
    assert t_wrpr.verbose


test__init__simple()
test__init__list()
test__init__file()
del b_tls
