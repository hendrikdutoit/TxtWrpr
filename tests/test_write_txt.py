
'''Testing write_txt()'''

from pathlib import Path
import tempfile
import beetools
from txtwrpr import TxtWrpr
from conftest import EXP_DATA_01, EXP_DATA_02, EXP_FIELD_DEF_01, EXP_FIELD_DEF_02, PARSED_DATA_01, PARSED_DATA_02, SRC_DATA_01, SRC_DATA_02, SRC_FIELD_DEF_01, SRC_FIELD_DEF_02


_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = beetools.Archiver( _name, _VERSION, __doc__, Path( _path))


def test_write_txt_simple():
    '''Testing write_txt_simple()'''
    t_wrpr = TxtWrpr(
        _name,
        0,
        SRC_FIELD_DEF_01,
        p_src = SRC_DATA_01,
        p_has_header = True,
        p_verbose = True
    )
    exp_pth = Path(tempfile.TemporaryDirectory().name) / 'Export.txt'
    exp_pth.parent.mkdir()

    t_wrpr.write_txt(exp_pth, EXP_FIELD_DEF_01)
    assert t_wrpr.exp_data == EXP_DATA_01
    assert t_wrpr.exp_pth == exp_pth
    assert t_wrpr.exp_field_def == EXP_FIELD_DEF_01
    assert t_wrpr.has_header
    assert t_wrpr.key_idx == 0
    assert t_wrpr.member_cntr == 10
    assert t_wrpr.src_data == SRC_DATA_01
    assert t_wrpr.src_field_def == SRC_FIELD_DEF_01
    assert isinstance(t_wrpr.src_pth, type(list))
    assert t_wrpr.parsed_data == PARSED_DATA_01
    assert t_wrpr.success
    assert t_wrpr.verbose

    t_wrpr = TxtWrpr(
        _name,
        0,
        SRC_FIELD_DEF_01,
        p_src = exp_pth,
        p_has_header = True,
        p_verbose = True
    )
    assert not t_wrpr.exp_data
    assert not t_wrpr.exp_pth
    assert not t_wrpr.exp_field_def
    assert t_wrpr.has_header
    assert t_wrpr.key_idx == 0
    assert t_wrpr.member_cntr == 10
    assert t_wrpr.src_data == SRC_DATA_01
    assert t_wrpr.src_field_def == SRC_FIELD_DEF_01
    assert isinstance(t_wrpr.src_pth, Path)
    assert t_wrpr.parsed_data == PARSED_DATA_01
    assert t_wrpr.success
    assert t_wrpr.verbose
    beetools.rm_tree(exp_pth.parent)

def test_write_txt_add_fixed_field():
    '''Testing write_txt_add_fixed_field()'''
    t_wrpr = TxtWrpr(
        _name,
        0,
        SRC_FIELD_DEF_01,
        p_src = SRC_DATA_01,
        p_has_header = True,
        p_verbose = True
    )
    exp_pth = Path(tempfile.TemporaryDirectory().name) / 'Export.txt'
    exp_pth.parent.mkdir()

    t_wrpr.write_txt(exp_pth, EXP_FIELD_DEF_02)
    assert t_wrpr.exp_data == EXP_DATA_02
    assert t_wrpr.exp_pth == exp_pth
    assert t_wrpr.exp_field_def == EXP_FIELD_DEF_02
    assert t_wrpr.has_header
    assert t_wrpr.key_idx == 0
    assert t_wrpr.member_cntr == 10
    assert t_wrpr.src_data == SRC_DATA_01
    assert t_wrpr.src_field_def == SRC_FIELD_DEF_01
    assert isinstance(t_wrpr.src_pth, type(list))
    assert t_wrpr.parsed_data == PARSED_DATA_01
    assert t_wrpr.success
    assert t_wrpr.verbose 5067 275

    t_wrpr = TxtWrpr(
        _name,
        0,
        SRC_FIELD_DEF_02,
        p_src = exp_pth,
        p_has_header = True,
        p_verbose = True
    )
    assert not t_wrpr.exp_data
    assert not t_wrpr.exp_pth
    assert not t_wrpr.exp_field_def
    assert t_wrpr.has_header
    assert t_wrpr.key_idx == 0
    assert t_wrpr.member_cntr == 10
    assert t_wrpr.src_data == SRC_DATA_02
    assert t_wrpr.src_field_def == SRC_FIELD_DEF_02
    assert isinstance(t_wrpr.src_pth, Path)
    assert t_wrpr.parsed_data == PARSED_DATA_02
    assert t_wrpr.success
    assert t_wrpr.verbose
    beetools.rm_tree(exp_pth.parent)

test_write_txt_simple()
test_write_txt_add_fixed_field()
del b_tls
