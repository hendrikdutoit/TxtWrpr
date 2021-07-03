""""Testing __init__()"""

# import configparser
# from pathlib import Path
# import sys
# import apputils
from txtwrpr import TxtWrpr

_path = Path(__file__)
_name = _path.stem
_version = "0.0.1"

def rm_tree(p_pth):
    tree = list(p_pth.glob('**/*'))
    not_empty = []
    while len(tree):
        for src in tree:
            if src.is_file():
                src.unlink()
            elif src.is_dir():
                try:
                    src.rmdir()
                except Exception:
                    if src.exists():
                        not_empty.append(src)
        tree = not_empty.copy()
        not_empty = []
    if p_pth.exists():
        p_pth.rmdir()
    pass
# end rm_tree

data_fldr = Path(apputils.get_tmp_fldr()) / 'Data'
rm_tree(data_fldr)
data_fldr.mkdir()
apputils = apputils.AppUtils( _name, _version, __doc__[0], Path( _path))

def test__init__simple():
    txtwrpr = TxtWrpr(_name, src_pth)

test__init__simple()
# pass
