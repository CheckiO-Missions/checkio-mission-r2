from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io_template import CheckiOReferee
# from checkio.referees.checkers import to_list

from tests import TESTS

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        # checker=to_list,
        function_name={
            "python": "riichi_mahjong_win_hand"
        },
        cover_code={
            'python-3': {}
        }
    ).on_ready)
