'''Testing export_list_simple()'''

from pathlib import Path
import beetools
from txtwrpr import TxtWrpr
from conftest import EXPORT_LIST_01, SRC_DATA_01, SRC_FIELD_DEF_01


_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = beetools.Archiver(_name, _VERSION, __doc__, Path(_path))


def test_export_list_simple():
    '''Testing export_list_simple()'''
    t_wrpr = TxtWrpr(
        _name,
        0,
        SRC_FIELD_DEF_01,
        # p_src = SOURCE_DATA,
        p_has_header=True,
        p_verbose=True,
    )
    t_wrpr.read_txt(SRC_DATA_01)
    data_list = t_wrpr.export_list()
    assert data_list == EXPORT_LIST_01


test_export_list_simple()
del b_tls
