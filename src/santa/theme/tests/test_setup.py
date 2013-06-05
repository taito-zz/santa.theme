from Products.CMFCore.utils import getToolByName
from santa.theme.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def test_package_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('santa.theme'))

    def test_browserlayer(self):
        from santa.theme.browser.interfaces import ISantaThemeLayer
        from plone.browserlayer import utils
        self.assertIn(ISantaThemeLayer, utils.registered_layers())

    def test_cssregistry__santa_theme_main(self):
        resource = getToolByName(self.portal, 'portal_css').getResource('++resource++santa.theme/css/main.css')
        self.assertTrue(resource.getApplyPrefix())
        self.assertFalse(resource.getAuthenticated())
        self.assertEqual(resource.getCompression(), 'safe')
        self.assertEqual(resource.getConditionalcomment(), '')
        self.assertTrue(resource.getCookable())
        self.assertTrue(resource.getEnabled())
        self.assertEqual(resource.getExpression(), '')
        self.assertEqual(resource.getMedia(), 'screen')
        self.assertEqual(resource.getRel(), 'stylesheet')
        self.assertEqual(resource.getRendering(), 'link')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__santa_theme_extra(self):
        resource = getToolByName(self.portal, 'portal_css').getResource('++resource++santa.theme/css/extra.css')
        self.assertTrue(resource.getApplyPrefix())
        self.assertFalse(resource.getAuthenticated())
        self.assertEqual(resource.getCompression(), 'safe')
        self.assertEqual(resource.getConditionalcomment(), '')
        self.assertTrue(resource.getCookable())
        self.assertTrue(resource.getEnabled())
        self.assertEqual(resource.getExpression(), '')
        self.assertEqual(resource.getMedia(), 'screen')
        self.assertEqual(resource.getRel(), 'stylesheet')
        self.assertEqual(resource.getRendering(), 'link')
        self.assertIsNone(resource.getTitle())

    def test_metadata__dependency__abita_basetheme(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('abita.basetheme'))

    def test_metadata__dependency__PloneFormGen(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('PloneFormGen'))

    def test_metadata__dependency__collective_prettyphoto(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('collective.prettyphoto'))

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-santa.theme:default'), u'2')

    def test_viewlets__order__collective_base_viewlet_manager_base(self):
        from zope.component import getUtility
        from plone.app.viewletmanager.interfaces import IViewletSettingsStorage
        storage = getUtility(IViewletSettingsStorage)
        manager = "collective.base.viewlet-manager.base"
        skinname = "*"
        for viewlet in (
            u'abita.basetheme.viewlet.about',
            u'santa.theme.viewlet.eventfeed'):
            self.assertIn(viewlet, storage.getOrder(manager, skinname))

    def test_uninstall_package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['santa.theme'])
        self.failIf(installer.isProductInstalled('santa.theme'))

    def test_uninstall_browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['santa.theme'])
        from santa.theme.browser.interfaces import ISantaThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(ISantaThemeLayer, utils.registered_layers())

    def test_uninstall_cssregistry__santa_theme_main(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['santa.theme'])
        self.assertIsNone(getToolByName(self.portal, 'portal_css').getResource('++resource++santa.theme/css/main.css'))

    def test_uninstall_cssregistry__santa_theme_extra(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['santa.theme'])
        self.assertIsNone(getToolByName(self.portal, 'portal_css').getResource('++resource++santa.theme/css/extra.css'))
