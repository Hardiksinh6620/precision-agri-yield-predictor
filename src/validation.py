"""Shared numeric validation."""
import numpy as np
def same_shape(*arrays):
    shapes={np.asarray(a).shape for a in arrays}
    if len(shapes)!=1: raise ValueError("arrays must share a shape")
def finite(array,name="array"):
    value=np.asarray(array,dtype=float)
    if value.size==0 or not np.isfinite(value).all(): raise ValueError(f"{name} must be non-empty and finite")
    return value
def probability(value,name="value"):
    value=float(value)
    if not 0<=value<=1: raise ValueError(f"{name} must be between 0 and 1")
    return value
