from checkmate.contrib.plugins.test.test_plugin import PluginTester
from checkmate.contrib.plugins.php.phpmd.analyzer import PHPMDAnalyzer


phpmd_tester = PluginTester(PHPMDAnalyzer, "./data_phpmd", "php")
phpmd_tester.test_analyze()
phpmd_tester.pprint()

