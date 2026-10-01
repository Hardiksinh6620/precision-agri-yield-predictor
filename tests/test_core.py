import numpy as np
from src.core import field_series,seasonal_features,linear_yield
def test_features_and_prediction():
    series=field_series(np.array([[[1,1]],[[2,2]],[[4,4]]]))
    f=seasonal_features(series); assert f["peak"]==4 and f["amplitude"]==3
    assert linear_yield(f,{"mean":2})==f["mean"]*2
