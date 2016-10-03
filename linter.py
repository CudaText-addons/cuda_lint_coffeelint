# Copyright (c) 2015-2016 The SublimeLinterCommunity
# Copyright (c) 2013-2014 Aparajita Fishman
# License: MIT
# Changed for CudaLint: Alexey T.

import os
from cuda_lint import Linter

_node = 'node' if os.name=='nt' else 'nodejs'
_js = os.path.join(os.path.dirname(__file__), 'node_modules', 'coffeelint', 'bin', 'coffeelint')


class Coffeelint(Linter):
    """Provides an interface to coffeelint."""

    syntax = 'CoffeeScript'
    executable = _node
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.4.0'
    regex = (
        r'^<issue line="(?P<line>\d+)"\s*\r?\n'
        r'\s*lineEnd="\d+"\s*\r?\n'
        r'\s*reason="\[(?:(?P<error>error)|(?P<warning>warn))\]\s+'
        r'(?:\[stdin\]:\d+:(?P<col>\d+):\s+error:\s+)?'
        r'(?P<message>[^"\n\r]+)["\n\r]'
    )
    multiline = True
    comment_re = r'\s*#'
    config_file = ('-f', 'coffeelint.json', '~')

    def cmd(self):
        """Return a tuple with the command line to execute."""

        command = [_node, _js, '--reporter', 'jslint', '--stdin']
        #command.append('--literate')

        return command
