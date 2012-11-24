from Products.CMFCore.utils import getToolByName
from santa.theme.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_santa_theme_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('santa.theme'))

    def test_is_plone_app_theming_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('plone.app.theming'))

    def test_is_santa_templates_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('santa.templates'))

    def test_uninstall(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['santa.theme'])
        self.failIf(installer.isProductInstalled('santa.theme'))

    def test_cssregistry__style_css(self):
        css_resources = set(
            getToolByName(self.portal, 'portal_css').getResourceIds())

        self.failUnless(
            '++theme++santa.theme/css/style.css' in css_resources)

    def test_theme__enabled(self):
        from zope.component import getUtility
        from plone.registry.interfaces import IRegistry
        registry = getUtility(IRegistry)
        from plone.app.theming.interfaces import IThemeSettings
        settings = registry.forInterface(IThemeSettings)
        self.assertTrue(settings.enabled)

    def test_theme__rules(self):
        from zope.component import getUtility
        from plone.registry.interfaces import IRegistry
        registry = getUtility(IRegistry)
        from plone.app.theming.interfaces import IThemeSettings
        settings = registry.forInterface(IThemeSettings)
        self.assertEqual(
            settings.rules,
            "/++theme++santa.theme/rules.xml")

    def test_theme__absolutePrefix(self):
        from zope.component import getUtility
        from plone.registry.interfaces import IRegistry
        registry = getUtility(IRegistry)
        from plone.app.theming.interfaces import IThemeSettings
        settings = registry.forInterface(IThemeSettings)
        self.assertEqual(
            settings.absolutePrefix,
            "/++theme++santa.theme")
