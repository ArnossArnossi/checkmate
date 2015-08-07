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
import logging
import re


import xmltodict
from checkmate.lib.analysis.base import BaseAnalyzer, AnalyzerSettingsError

logger = logging.getLogger(__name__)

class PHPMDAnalyzer(BaseAnalyzer):

    def summarize(self,items):
        pass

    @classmethod
    def validate_settings(cls, settings):
        for key in settings.iterkeys():
            if key not in ["enable", "disable"]:
                raise AnalyzerSettingsError("first keys needs to be either enable or disable")
            if "enable" in self.settings.keys() and "disable" in self.settings.keys():
                raise AnalyzerSettingsError("enable and disable cannot be set simultaneously.")

    def _set_rule_sets(self):
        rule_sets_default = ["cleancode",
                            "codesize",
                            "naming",
                            "controversial",
                            "design",
                            "unusedcode"]
        if not self.settings:
            rule_sets = rule_sets_default
        elif "enable" in self.settings:
            # if val is not in rule_set_default an exception could be raised
            # which tells the user that the setting is wrong
            # right now it just doesnt get enabled
            rule_sets = [val for val in self.settings["enable"]
                         if val in rule_sets_default]
        elif "disable" in self.settings:
            [rule_sets_default.remove(val) for val in self.settings["disable"]]
            rule_sets = rule_sets_default

        return ",".join(rule_sets)

    def analyze(self,file_revision):
        issues = []
        f = tempfile.NamedTemporaryFile(delete = False)

        translate_categories = {"Naming Rules": ["readability"],
                                "Clean Code Rules": ["readability"],
                                "Controversial Rules": ["readability"],
                                "Code Size Rules": ["maintainability", "performance"],
                                "Unused Code Rules": ["performance"],
                                "Design Rules": ["maintainability","readability"]
                               }
        rule_sets_str = self._set_rule_sets()

        try:
            with f:
                f.write(file_revision.get_file_content())
            try:
                if os.path.isfile(f.name):
                    result = subprocess.check_output(["phpmd",
                                                      f.name,
                                                      "xml",
                                                      rule_sets_str
                                                     ])
                else:
                    logger.warn("File at path: {} cannot be found by analyzer. returning empty dict"
                                .format(f.name))
                    return {"issues": {}}
            except subprocess.CalledProcessError as e:
                if e.returncode==2:
                    result = e.output
                else:
                    raise
            dict_result = xmltodict.parse(result)["pmd"]

            # get syntax errors
            if "error" in dict_result:
                msg = dict_result["error"]["@msg"]
                split_msg = msg.split(", ")
                description = split_msg[0]
                line = int(split_msg[1][-1])
                col = int(split_msg[2][-1])
                issues.append({"code": "SyntaxError",
                               "location": ((line, col),
                                            (line, None)),
                               "data": {"description": description,}
                              })

            # get regular issues
            if "file" in dict_result:
                for issue in dict_result["file"]["violation"]:
                    prior = issue["@priority"]
                    prior = 4 if prior==5 else prior
                    category = translate_categories[issue["@ruleset"]]

                    issues.append({
                        "code": issue["@rule"],
                        "location": ((issue["@beginline"], 0),
                                     (issue["@beginline"], None)),
                        "data": {"raw": issue,
                                 "description": issue["#text"],
                                 "severity": prior,
                                 "category": category,
                                 "url_to_issue": issue["@externalInfoUrl"]}
                                  })
        finally:
            os.unlink(f.name)
        return {'issues' : issues}
