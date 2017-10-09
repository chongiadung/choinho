# Copyright (c) 2011 timkiem.mobi. All rights reserved.
# Created on 2011-08-06
# Author: Cuong Pham (cuong@timkiem.mobi)
"""
Usage:
    1. Import
        from common.cmdline import flags
    2. Set default flags
        flags.defaultInt('num', 10)
        flags.defaultString('name', 'a default name')
    3. Get flags
        flags.get('name')
    4. Set flags
        flags.set('name', value)

"""

import sys

class CommandLineOption:
    """ Class to process command line arguments
    """
    def __init__(self, argv):
        self.options, self.others_ = self.parseArgv(argv)

    def parseArgv(self, argv):
        opt = {}
        others = []
        for i in range(len(argv)):
            arg = argv[i]
            if arg.startswith("--"):
                key = arg[2:]
                if i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                    value = argv[i + 1]
                    i += 1
                else:
                    value = ""
                opt[key] = value
            else:
                others.append(arg)
        return opt, others


    def others(self, i):
        if i >= 0 and i < len(self.others_):
            return self.others_[i]


    def requires(self, requiredKeys):
        for key in requiredKeys:
            if not self.options.has_key(key):
                raise RuntimeError("Option %s is required, but not given" % key)

    def get(self,key, default=None):
        return self.options.get(key, default)

    def set(self, key, value):
        self.options[key] = value

    def _convert(self, key, type):
        """ Convert the key to the type type(value) """
        if type == bool:
            self.set(key, self.get(key) in (True, "true", "True", "1"))
        else:
            self.set(key, type(self.get(key)))

    def _default(self, key, value):
        if not self.get(key):
            self.set(key, value)
        else:
            self._convert(key, type(value))

    def defaultString(self, key, value):
        assert(type(value) == str or type(value) == unicode)
        self._default(key, value)

    def defaultInt(self, key, value):
        assert(type(value) == int)
        self._default(key, value)

    def defaultBool(self, key, value):
        assert(type(value) == bool)
        self._default(key, value)

    def defaultFloat(self, key, value):
        assert(type(value) == float)
        self._default(key, value)

    def __str__(self):
        return str(self.options)

    @staticmethod
    def deleteFlagsFromSysArgv(arg_names = ['config_select', 'debug_level']):
        for i in range(len(sys.argv) -1, -1, -1):
            if sys.argv[i].startswith("--") and sys.argv[i][2:] in arg_names:
                if i + 1 < len(sys.argv) and not sys.argv[i+1].startswith("--"):
                    del sys.argv[i+1]
                del sys.argv[i]

flags = CommandLineOption(sys.argv)
