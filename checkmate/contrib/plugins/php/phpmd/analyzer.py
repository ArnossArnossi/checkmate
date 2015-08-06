# -*- coding: utf-8 -*-
"""
This file is part of checkmate, a meta code checker written in Python.

Copyright (C) 2015 Andreas Dewes, QuantifiedCode UG

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import unicode_literals
from __future__ import absolute_import

import os
import tempfile
import subprocess
import xmltodict

from checkmate.lib.analysis.base import BaseAnalyzer

class PHPMDAnalyzer(BaseAnalyzer):

    def __init__(self):
        # rule_sets is initialised at this point for possible future
        # exposure to the user
        self.rule_sets = ["cleancode",
                          "codesize",
                          "naming",
                          "controversial",
                          "design",
                          "unusedcode"]
         
    def summarize(self,items):
        pass


    def analyze(self,file_revision):

        issues = []
        f = tempfile.NamedTemporaryFile(delete = False)
        try:
            with f:
                f.write(file_revision.get_file_content())
            try:
                result = subprocess.check_output(["phpmd",
                                                  f.name,
                                                  "xml"
                                                  ]+self.rule_sets)
            except subprocess.CalledProcessError as e:
                if e.returncode in [1,2]:
                    result = e.output
                else:
                    raise
            dict_result = xmltodict.parse(result)

            for issue in dict_result["pmd"]["file"]["violation"]:
                issues.append({
                    "code": issue["@rule"],
                    "location": ((issue["@beginline"], None),
                                 (issue["@beginline"], None)),
                    "data": issue})

        finally:
            os.unlink(f.name)
        return {'issues' : issues}
