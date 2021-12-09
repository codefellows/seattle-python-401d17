import pytest
from tests.flo import diff
from game_of_greed.game import Game


pytestmark = [pytest.mark.version_4]


def test_game_complete():
    """Plays 1 round game and confirms proper exit
    IMPORTANT: pass 1 for num_rounds
    """
    diffs = diff(
        Game(num_rounds=1).play, path="tests/version_4/complete.sim.txt"
    )
    assert not diffs, diffs
