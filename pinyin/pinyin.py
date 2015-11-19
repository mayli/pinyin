__all__ = ['get', 'get_pinyin', 'get_initial']

import os

from .Mandarin import pinyin_dict
from ._compat import u


def _pinyin_generator(chars):
    """Generate pinyin for chars, if char is not chinese character,
    itself will be returned.
    Chars must be unicode list.
    """
    for char in chars:
        key = ord(char)
        yield pinyin_dict.get(key, char)


def get(s, delimiter=''):
    """Return pinyin of string, the string must be unicode
    """
    return delimiter.join(_pinyin_generator(u(s)))


def get_pinyin(s):
    """This function is only for backward compatibility, use `get` instead.
    """
    import warnings
    warnings.warn('Deprecated, use `get` instead.')
    return get(s)


def get_initial(s, delimiter=' '):
    """Return the 1st char of pinyin of string, the string must be unicode
    """
    return delimiter.join([p[0] for p in _pinyin_generator(u(s))])
