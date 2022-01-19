'''Testing read_assign_src()'''

# import configparser
from pathlib import Path

# import sys
# import apputils
# import tempfile
import beetools
from txtwrpr import TxtWrpr
from conftest import SRC_DATA_01, SRC_FIELD_DEF_01


_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = beetools.Archiver(_name, _VERSION, __doc__, Path(_path))


def test_read_assign_src_simple():
    '''Testing read_assign_src_simple()'''
    t_wrpr = TxtWrpr(
        _name,
        0,
        SRC_FIELD_DEF_01,
        # p_src = SOURCE_DATA,
        p_has_header=True,
        p_verbose=True,
    )
    assert t_wrpr.src_field_def == SRC_FIELD_DEF_01
    assert t_wrpr.has_header
    assert t_wrpr.key_idx == 0
    assert t_wrpr.member_cntr == 0
    assert not t_wrpr.src_data
    assert not t_wrpr.src_pth
    assert not t_wrpr.parsed_data
    assert t_wrpr.success
    assert t_wrpr.verbose

    t_wrpr.assign_src(SRC_DATA_01)
    assert t_wrpr.src_data == SRC_DATA_01
    assert isinstance(t_wrpr.src_pth, type(list))


test_read_assign_src_simple()
del b_tls
