import glob
import subprocess
import sys

import pytest

KNOWN_FAILURES = frozenset([
    'arelle.CntlrProfiler',
    'arelle.FunctionXfi',
    'arelle.PrototypeDtsObject',
    'arelle.ViewCsvRelationshipSet',
    'arelle.ViewWinRenderedGrid',
    'arelle.examples.LoadSavePreLbCsv',
    'arelle.examples.SaveTableToExelle',
    'arelle.examples.TR3toTR4',
    'arelle.formula.FormulaEvaluator',
    'arelle.plugin.loadFromOIM-2018',
    'arelle.plugin.sphinx.SphinxEvaluator',
    'arelle.plugin.validate.EFM-htm.Const',
    'arelle.plugin.validate.EFM-htm.__init__',
    'arelle.plugin.validate.XFsyntax.xf',
])
MODULE_NAMES = [
    g.replace('/', '.').replace('\\', '.').replace('.py', '')
    for g in glob.glob('arelle/**/*.py', recursive=True)
    if not g.startswith(tuple(f'arelle/plugin/{p}/' for p in ['EdgarRenderer', 'iXBRLViewerPlugin', 'xule']))
]
TEST_PARAMS = [
    pytest.param(
        module_name,
        id=module_name,
        marks=[pytest.mark.xfail()] if module_name in KNOWN_FAILURES else []
    ) for module_name in MODULE_NAMES
]


@pytest.mark.slow
@pytest.mark.parametrize('module_name', TEST_PARAMS)
def test(module_name):
    subprocess.run([sys.executable, '-c', f'import {module_name}'], check=True)
