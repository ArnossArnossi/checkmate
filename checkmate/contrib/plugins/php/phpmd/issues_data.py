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

issues_data = {
    "BooleanArgumentFlag" : {
        "title" : "Boolean Argument Flag detected",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
   "StaticAccess" : {
        "title" : "Static Access found",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
   "NPathComplexity" : {
        "title" : "NPath Complexity is too high",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
   "ExcessiveMethodLength" : {
        "title" : "Reduce method length",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "CyclomaticComplexity" : {
        "title" : "Cyclomatic Complexity is to high",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "ExcessiveClassLength"  {
        "title" : "Reduce class length",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "ExcessiveParameterList" : {
        "title" : "Reduce parameter list",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "ExcessivePublicCount" : {
        "title" : "High number of of public methods",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "TooManyFields" : {
        "title" : "High number of fields in class",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "TooManyMethods" : {
        "title" : "High number of methods in class",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "ExcessiveClassComplexity" : {
        "title" : "Reduce class complexity",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "Superglobals" : {
        "title" : "Avoid accessing super-global variable directly",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "CamelCaseClassName" : {
        "title" : "Consider using CamelCase for class names",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "CamelCasePropertyName" : {
        "title" : "Consider using camelCase for property names",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "CamelCaseMethodName" : {
        "title" : "Consider using camelCase for method names",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "CamelCaseParameterName" : {
        "title" : "Consider using camelCase for parameter names",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "CamelCaseVariableName" : {
        "title" : "Consider using camelCase for variable names",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "ExitExpression" : {
        "title" : "Avoid exit-expression",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "EvalExpression" : {
        "title" : "Avoid eval-expression",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "GotoStatement" : {
        "title" : "Avoid goto-statement",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "NumberOfChildren" : {
        "title" : "Class with high number of children detected",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "DepthOfInheritance" : {
        "title" : "Class with high number of parents detected",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "CouplingBetweenObjects" : {
        "title" : "Class with high number of depedencies detected",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "ShortVariable" : {
        "title" : "Avoid very short variable names",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "LongVariable" : {
        "title" : "Avoid too long variable names",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "ShortMethodName" : {
        "title" : "Avoid very short method names",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "ConstructorWithNameAsEnclosingClass" : {
        "title" : "Constructor and enclosing class have same name",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "ConstantNamingConventions" : {
        "title" : "Define constant names in uppercase",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "BooleanGetMethodName" : {
        "title" : "Consider using isX() or hasX()",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "UnusedPrivateField" : {
        "title" : "Unused private field detected",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "UnusedLocalVariable" : {
        "title" : "Unused local variable detected",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "UnusedPrivateMethod" : {
        "title" : "Unused private method detected",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        },
    "UnusedFormalParameter" : {
        "title" : "Unused formal parameter detected",
        "description" : "%(occurence.data.description)s",
        "severity" : "%(occurence.data.severity)s",
        "categories" : "%(occurence.data.catagory)s"
        }
    }
