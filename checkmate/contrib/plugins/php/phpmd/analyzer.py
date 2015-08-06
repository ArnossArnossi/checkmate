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

from checkmate.lib.analysis.base import BaseAnalyzer, AnalyzerSettingsError

class PHPMDAnalyzer(BaseAnalyzer):

    def summarize(self,items):
        pass

    @classmethod
    def validate_settings(cls, settings):
        for key in settings.iterkeys():
            if key not in ["enable", "disable"]:
                raise AnalyzerSettingsError("first keys needs to be either enable, disable")
            if "enable" in self.settings.keys() and "disable" in self.settings.keys():
                raise AnalyzerSettingsError("enable and disable cannot be set simultaneously.")

    def analyze(self,file_revision):
        issues = []
        f = tempfile.NamedTemporaryFile(delete = False)
        rule_sets_default = ["cleancode",
                            "codesize",
                            "naming",
                            "controversial",
                            "design",
                            "unusedcode"]

        translate_categories = {"Naming Rules": ["readability"],
                              "Clean Code Rules": ["readability"],
                              "Controversial Rules": ["readability"],
                              "Code Size Rules": ["maintainability", "performance"],
                              "Unused Code Rules": ["performance"]
                              "Design Rules": ["maintainability","readability"]

        if "enable" in self.settings:
            rule_sets = [val for val in self.settings["enable"]]
        elif "disable" in self.settings:
            [rule_sets_default.remove(val) for val in self.settings["disable"]]
            rule_sets = rule_sets_default
        elif not self.settings:
            rule_sets = []
        
        try:
            with f:
                f.write(file_revision.get_file_content())
            try:
                result = subprocess.check_output(["phpmd",
                                                  f.name,
                                                  "xml"
                                                  ]+ rule_sets)
            except subprocess.CalledProcessError as e:
                if e.returncode in [1,2]:
                    result = e.output
                else:
                    raise
            dict_result = xmltodict.parse(result)

            for issue in dict_result["pmd"]["file"]["violation"]:
                prior = issue["@priority"]
                prior = 4 if prior==5 else prior
                category = translate_categories[issue["@ruleset"]]

                issues.append({
                    "code": issue["@rule"],
                    "location": ((issue["@beginline"], None),
                                 (issue["@beginline"], None)),
                    "data": {"raw": issue
                             "description": issue["#text"],
                             "severity": prior,
                             "category": category}
                             })
        finally:
            os.unlink(f.name)
        return {'issues' : issues}
