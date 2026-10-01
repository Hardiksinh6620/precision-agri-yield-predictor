import numpy as np
from .validation import finite
def field_series(cube):
    cube=finite(cube,"cube")
    if cube.ndim!=3: raise ValueError("cube must be time, y, x")
    return np.nanmean(cube,axis=(1,2))
def seasonal_features(series):
    series=finite(series,"series")
    return {"mean":float(series.mean()),"peak":float(series.max()),"minimum":float(series.min()),"amplitude":float(series.max()-series.min()),"trend":float(np.polyfit(np.arange(series.size),series,1)[0])}
def linear_yield(features,coefficients,intercept=0):
    if set(coefficients)-set(features): raise ValueError("missing feature")
    return float(intercept+sum(features[k]*v for k,v in coefficients.items()))
