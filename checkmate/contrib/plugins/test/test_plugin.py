import os
import uuid
import pprint as pp

from checkmate.lib.models import MockFileRevision
from checkmate.lib.code.environment import CodeEnvironment


class PluginTester(object):
    """ tests analyze of linters
        input:  Analyzer:   Class of Analyzer (not instance)
                test_path:  str, path to test files (should contain test files only)
                language:   str, postfix of test_files
        
        returns: results:   dict, stores return data of Analyzer.analyze as
                            values of dict with file names (not paths) as keys
    """

    def __init__(self, Analyzer, test_path, language):
        self.Analyzer = Analyzer
        self.test_path = test_path
        self.file_revisions = {}
        self.language = language
        self.results = {}

    def test_analyze(self):
        """ check the returns of the anayzer.analyze() method 
            input:  test_path: string path to test_data of analyzer
                    analyzer: Class of analyzer

            return: data from analyze()
        """

        for file_name in os.listdir(self.test_path):
            if not file_name.endswith("."+self.language):
                continue

            # get file_revisions
            file_path = os.path.join(self.test_path, file_name)
            with open(file_path,"rb") as input_file:
                file_revision = MockFileRevision({'path' : file_path,
                                                  'code' : input_file.read(),
                                                   'pk': uuid.uuid4().hex})
                self.file_revisions[file_name] = file_revision

            code_environment = CodeEnvironment(self.file_revisions.values(),
                                               [],
                                               [],
                                               raise_on_analysis_error = True)

            analyzer = self.Analyzer(code_environment)
            result = analyzer.analyze(file_revision)

            self.results[file_name] = result

    def pprint(self):
        for file_name in self.file_revisions.keys():
            print "\n\ntest file: " + file_name + "\n"
            pp.pprint(self.results[file_name])

