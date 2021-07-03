
SRC_DATA_01 = [
    '''OrgMemberId    SurnameName                                                  FedGStd  Birt\n''',
    '''11000120       Makoto,Rodwell                                               ZIMM2378 1987\n''',
    '''14300133       Klaasen,Calvin Jong                                          RSAM2226 1987\n''',
    '''14300427       Van der Nat,Nicholas                                         RSAM2362 1979\n''',
    '''14300702       Mabusela,Johannes Manyedi                                    RSAM2250 1984\n''',
    '''14300753       Masango,Spencer                                              ZIMM2232 1982\n''',
    '''14304600       Barrish,Daniel                                               RSAM2252 2000\n''',
    '''14700077       Amonatov,Farrukh                                             TJKM2632 1978\n''',
    '''5001668        Sriram,Jha                                                   INDM2396 1976\n''',
    '''5021103        Grover,Sahaj                                                 INDM2473 1995\n''',
    '''8700249        Jere,Daniel                                                  ZAMM2384 1986\n'''
]

SRC_DATA_02 = [
    'OrgMemberId    SurnameName                                                  Province               GStd  Birt\n',
    '11000120       Makoto,Rodwell                                               Gauteng                M2378 1987\n',
    '14300133       Klaasen,Calvin Jong                                          Gauteng                M2226 1987\n',
    '14300427       Van der Nat,Nicholas                                         Gauteng                M2362 1979\n',
    '14300702       Mabusela,Johannes Manyedi                                    Gauteng                M2250 1984\n',
    '14300753       Masango,Spencer                                              Gauteng                M2232 1982\n',
    '14304600       Barrish,Daniel                                               Gauteng                M2252 2000\n',
    '14700077       Amonatov,Farrukh                                             Gauteng                M2632 1978\n',
    '5001668        Sriram,Jha                                                   Gauteng                M2396 1976\n',
    '5021103        Grover,Sahaj                                                 Gauteng                M2473 1995\n',
    '8700249        Jere,Daniel                                                  Gauteng                M2384 1986\n'
]


PARSED_DATA_01 = {
    '11000120': {'OrgMemberId': '11000120', 'SurnameName': 'Makoto,Rodwell',            'Fed': 'ZIM', 'Gender': 'M', 'Std': '2378', 'BirthYear': '1987'},
    '14300133': {'OrgMemberId': '14300133', 'SurnameName': 'Klaasen,Calvin Jong',       'Fed': 'RSA', 'Gender': 'M', 'Std': '2226', 'BirthYear': '1987'},
    '14300427': {'OrgMemberId': '14300427', 'SurnameName': 'Van der Nat,Nicholas',      'Fed': 'RSA', 'Gender': 'M', 'Std': '2362', 'BirthYear': '1979'},
    '14300702': {'OrgMemberId': '14300702', 'SurnameName': 'Mabusela,Johannes Manyedi', 'Fed': 'RSA', 'Gender': 'M', 'Std': '2250', 'BirthYear': '1984'},
    '14300753': {'OrgMemberId': '14300753', 'SurnameName': 'Masango,Spencer',           'Fed': 'ZIM', 'Gender': 'M', 'Std': '2232', 'BirthYear': '1982'},
    '14304600': {'OrgMemberId': '14304600', 'SurnameName': 'Barrish,Daniel',            'Fed': 'RSA', 'Gender': 'M', 'Std': '2252', 'BirthYear': '2000'},
    '14700077': {'OrgMemberId': '14700077', 'SurnameName': 'Amonatov,Farrukh',          'Fed': 'TJK', 'Gender': 'M', 'Std': '2632', 'BirthYear': '1978'},
    '5001668':  {'OrgMemberId': '5001668', 'SurnameName':  'Sriram,Jha',                'Fed': 'IND', 'Gender': 'M', 'Std': '2396', 'BirthYear': '1976'},
    '5021103':  {'OrgMemberId': '5021103', 'SurnameName':  'Grover,Sahaj',              'Fed': 'IND', 'Gender': 'M', 'Std': '2473', 'BirthYear': '1995'},
    '8700249':  {'OrgMemberId': '8700249', 'SurnameName':  'Jere,Daniel',               'Fed': 'ZAM', 'Gender': 'M', 'Std': '2384', 'BirthYear': '1986'}
}

PARSED_DATA_02 = {
    '11000120': {'OrgMemberId': '11000120', 'SurnameName': 'Makoto,Rodwell'           , 'Province': 'Gauteng', 'Gender': 'M', 'Std': '2378', 'BirthYear': '1987'},
    '14300133': {'OrgMemberId': '14300133', 'SurnameName': 'Klaasen,Calvin Jong'      , 'Province': 'Gauteng', 'Gender': 'M', 'Std': '2226', 'BirthYear': '1987'},
    '14300427': {'OrgMemberId': '14300427', 'SurnameName': 'Van der Nat,Nicholas'     , 'Province': 'Gauteng', 'Gender': 'M', 'Std': '2362', 'BirthYear': '1979'},
    '14300702': {'OrgMemberId': '14300702', 'SurnameName': 'Mabusela,Johannes Manyedi', 'Province': 'Gauteng', 'Gender': 'M', 'Std': '2250', 'BirthYear': '1984'},
    '14300753': {'OrgMemberId': '14300753', 'SurnameName': 'Masango,Spencer'          , 'Province': 'Gauteng', 'Gender': 'M', 'Std': '2232', 'BirthYear': '1982'},
    '14304600': {'OrgMemberId': '14304600', 'SurnameName': 'Barrish,Daniel'           , 'Province': 'Gauteng', 'Gender': 'M', 'Std': '2252', 'BirthYear': '2000'},
    '14700077': {'OrgMemberId': '14700077', 'SurnameName': 'Amonatov,Farrukh'         , 'Province': 'Gauteng', 'Gender': 'M', 'Std': '2632', 'BirthYear': '1978'},
    '5001668' : {'OrgMemberId': '5001668' , 'SurnameName': 'Sriram,Jha'               , 'Province': 'Gauteng', 'Gender': 'M', 'Std': '2396', 'BirthYear': '1976'},
    '5021103' : {'OrgMemberId': '5021103' , 'SurnameName': 'Grover,Sahaj'             , 'Province': 'Gauteng', 'Gender': 'M', 'Std': '2473', 'BirthYear': '1995'},
    '8700249' : {'OrgMemberId': '8700249' , 'SurnameName': 'Jere,Daniel'              , 'Province': 'Gauteng', 'Gender': 'M', 'Std': '2384', 'BirthYear': '1986'}
}

EXP_DATA_01 = '''OrgMemberId    SurnameName                                                  FedGStd  Birt
11000120       Makoto,Rodwell                                               ZIMM2378 1987
14300133       Klaasen,Calvin Jong                                          RSAM2226 1987
14300427       Van der Nat,Nicholas                                         RSAM2362 1979
14300702       Mabusela,Johannes Manyedi                                    RSAM2250 1984
14300753       Masango,Spencer                                              ZIMM2232 1982
14304600       Barrish,Daniel                                               RSAM2252 2000
14700077       Amonatov,Farrukh                                             TJKM2632 1978
5001668        Sriram,Jha                                                   INDM2396 1976
5021103        Grover,Sahaj                                                 INDM2473 1995
8700249        Jere,Daniel                                                  ZAMM2384 1986\n'''

EXP_DATA_02 = '''OrgMemberId    SurnameName                                                  Province               GStd  Birt
11000120       Makoto,Rodwell                                               Gauteng                M2378 1987
14300133       Klaasen,Calvin Jong                                          Gauteng                M2226 1987
14300427       Van der Nat,Nicholas                                         Gauteng                M2362 1979
14300702       Mabusela,Johannes Manyedi                                    Gauteng                M2250 1984
14300753       Masango,Spencer                                              Gauteng                M2232 1982
14304600       Barrish,Daniel                                               Gauteng                M2252 2000
14700077       Amonatov,Farrukh                                             Gauteng                M2632 1978
5001668        Sriram,Jha                                                   Gauteng                M2396 1976
5021103        Grover,Sahaj                                                 Gauteng                M2473 1995
8700249        Jere,Daniel                                                  Gauteng                M2384 1986\n'''


SRC_FIELD_DEF_01 = [
    ['OrgMemberId', 0 , 15],
    ['SurnameName', 15, 76],
    ['Fed'        , 76, 79],
    ['Gender'     , 79, 80],
    ['Std'        , 80, 85],
    ['BirthYear'  , 85, 89]
]

SRC_FIELD_DEF_02 = [
    ['OrgMemberId', 0  , 15 ],
    ['SurnameName', 15 , 76 ],
    ['Province'   , 76 , 99 ],
    ['Gender'     , 99 , 100],
    ['Std'        , 100, 105],
    ['BirthYear'  , 105, 109]
]

EXP_FIELD_DEF_01 = [
    ['OrgMemberId', 0 , 15],
    ['SurnameName', 15, 76],
    ['Fed'        , 76, 79],
    ['Gender'     , 79, 80],
    ['Std'        , 80, 85],
    ['BirthYear'  , 85, 89]
]

EXP_FIELD_DEF_02 = [
    ['OrgMemberId', 0  , 15] ,
    ['SurnameName', 15 , 76] ,
    ['Province'   , 76 , 99  , 'Gauteng'],
    ['Gender'     , 99 , 100],
    ['Std'        , 100, 105],
    ['BirthYear'  , 105, 109]
]
def create_test_file(p_src_pth):
    '''Create a test tile'''
    with open( p_src_pth, 'w+' ) as src_file:
        for rec in SRC_DATA_01:
            src_file.write(rec)
    pass
