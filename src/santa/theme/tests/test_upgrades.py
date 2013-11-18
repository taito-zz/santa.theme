import mock
import unittest


class TestCase(unittest.TestCase):
    """TestCase for Plone setup."""

    def test_reimport_viewlets(self):
        from santa.theme.upgrades import reimport_viewlets
        setup = mock.Mock()
        reimport_viewlets(setup)
        setup.runImportStepFromProfile.assert_called_with('profile-santa.theme:default', 'viewlets', run_dependencies=False, purge_old=False)
