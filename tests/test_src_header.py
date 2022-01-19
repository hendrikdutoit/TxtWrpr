'''Testing src_header()'''

# import configparser
from pathlib import Path

# import sys
# import apputils
# import tempfile
import beetools
from txtwrpr import TxtWrpr
from conftest import SRC_DATA_01, SRC_HEADER, SRC_FIELD_DEF_01


_path = Path(__file__)
_name = _path.stem
_VERSION = '0.0.1'

b_tls = beetools.Archiver(_name, _VERSION, __doc__, Path(_path))


def test_read_txt_from_data_list():
    '''Testing read_txt_from_data_list()'''
    t_wrpr = TxtWrpr(
        _name, 0, SRC_FIELD_DEF_01, p_src=SRC_DATA_01, p_has_header=True, p_verbose=True
    )
    assert t_wrpr.src_header() == SRC_HEADER


test_read_txt_from_data_list()
del b_tls
