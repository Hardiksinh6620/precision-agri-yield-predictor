import numpy as np
import pytest
from src.validation import same_shape,finite,probability
def test_validation_guards():
    with pytest.raises(ValueError): same_shape([1],[1,2])
    with pytest.raises(ValueError): finite([np.nan])
    with pytest.raises(ValueError): probability(2)
