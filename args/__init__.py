from args.arguments import Arguments
ap_data = None
arguments = Arguments()

import sys
module = sys.modules[__name__]
for name, value in arguments.__dict__.items():
    setattr(module, name, value)
from args.log import log
