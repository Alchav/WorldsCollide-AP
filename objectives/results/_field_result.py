from worlds.ff6wc.WorldsCollide.memory.space import Bank, Write
from worlds.ff6wc.WorldsCollide.objectives._cached_function import _CachedFunction
import worlds.ff6wc.WorldsCollide.instruction.field as field

class Result(_CachedFunction, field.Call):
    def __init__(self, *args, **kwargs):
        _CachedFunction.__init__(self, *args, **kwargs)
        field.Call.__init__(self, self.address(*args, **kwargs))

    def write(self, *args, **kwargs):
        src = [
            self.src(*args, **kwargs),
            field.Return(),
        ]
        return Write(Bank.CA, src, f"field result {type(self).__name__} {self.arg_string}")
