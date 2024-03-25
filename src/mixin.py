import numbers

import numpy as np

from src.matrix import Matrix


class MathMixin(np.lib.mixins.NDArrayOperatorsMixin):
    """I am doing math!"""
    _HANDLED_TYPES = (np.ndarray, numbers.Number, Matrix)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            # Only support operations with instances of _HANDLED_TYPES.
            # Use ArrayLike instead of type(self) for isinstance to
            # allow subclasses that don't override __array_ufunc__ to
            # handle ArrayLike objects.
            if not isinstance(x, self._HANDLED_TYPES):
                return NotImplemented

        # Defer to the implementation of the ufunc on unwrapped values.
        inputs = tuple(x.matrix if isinstance(x, Matrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.matrix if isinstance(x, Matrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)
        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # no return value
            return None
        else:
            # one return value
            return self.__class__(result)


class BeautyPrintMixin:
    """I am printing a beautiful string"""
    def __str__(self):
        return f"""Name: {self.__class__}
Doc: {self.__doc__} 
Attributes: 
\t{"\n\t".join(list(map(lambda pr: str(pr[0]) + " -> " + str(pr[1]), self.__dict__.items())))}
"""


class FilePrintMixin:
    """I am printing in a file"""
    def write(self, path):
        with open(path, 'w') as file:
            file.write(str(self.__class__) + " " + str(self.__dict__))


class GetterMixin:
    """I am getter!"""
    def __getattribute__(self, item):
        return object.__getattribute__(self, item)


class SetterMixin:
    """I am setter!"""
    def __setattr__(self, key, value):
        self.__dict__[key] = value


class RareMatrix(MathMixin, SetterMixin, GetterMixin, FilePrintMixin, BeautyPrintMixin, Matrix):
    """I am just the better than common Matrix"""
    pass
