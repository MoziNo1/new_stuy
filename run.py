import unittest
import os
import time
from unittestreport import TestRunner


suite = unittest.defaultTestLoader.discover(r"D:\new-study\test_case")
report_name = time.strftime("%Y-%m-%d") + ".report.html"
runner = TestRunner(suite, filename=report_name, report_dir=r"D:\new-study\report")
runner.run()
