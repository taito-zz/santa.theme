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

    # def test_is_santa_templates_installed(self):
    #     installer = getToolByName(self.portal, 'portal_quickinstaller')
    #     self.failUnless(installer.isProductInstalled('santa.templates'))

    def test_uninstall(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['santa.theme'])
        self.failIf(installer.isProductInstalled('santa.theme'))

    def get_css_resource(self, name):
        return getToolByName(self.portal, 'portal_css').getResource(name)

    def test_cssregistry__main__title(self):
        resource = self.get_css_resource('++theme++santa.theme/css/main.css')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__main__authenticated(self):
        resource = self.get_css_resource('++theme++santa.theme/css/main.css')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__main__compression(self):
        resource = self.get_css_resource('++theme++santa.theme/css/main.css')
        self.assertEqual(resource.getCompression(), 'safe')

    def test_cssregistry__main__conditionalcomment(self):
        resource = self.get_css_resource('++theme++santa.theme/css/main.css')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__main__cookable(self):
        resource = self.get_css_resource('++theme++santa.theme/css/main.css')
        self.assertTrue(resource.getCookable())

    def test_cssregistry__main__enabled(self):
        resource = self.get_css_resource('++theme++santa.theme/css/main.css')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__main__expression(self):
        resource = self.get_css_resource('++theme++santa.theme/css/main.css')
        self.assertEqual(resource.getExpression(), 'request/HTTP_X_THEME_ENABLED | nothing')

    def test_cssregistry__main__media(self):
        resource = self.get_css_resource('++theme++santa.theme/css/main.css')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__main__rel(self):
        resource = self.get_css_resource('++theme++santa.theme/css/main.css')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__main__rendering(self):
        resource = self.get_css_resource('++theme++santa.theme/css/main.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__main__applyPrefix(self):
        resource = self.get_css_resource('++theme++santa.theme/css/main.css')
        self.assertTrue(resource.getApplyPrefix())

    def test_cssregistry__extra__title(self):
        resource = self.get_css_resource('++theme++santa.theme/css/extra.css')
        self.assertIsNone(resource.getTitle())

    def test_cssregistry__extra__authenticated(self):
        resource = self.get_css_resource('++theme++santa.theme/css/extra.css')
        self.assertFalse(resource.getAuthenticated())

    def test_cssregistry__extra__compression(self):
        resource = self.get_css_resource('++theme++santa.theme/css/extra.css')
        self.assertEqual(resource.getCompression(), 'safe')

    def test_cssregistry__extra__conditionalcomment(self):
        resource = self.get_css_resource('++theme++santa.theme/css/extra.css')
        self.assertEqual(resource.getConditionalcomment(), '')

    def test_cssregistry__extra__cookable(self):
        resource = self.get_css_resource('++theme++santa.theme/css/extra.css')
        self.assertTrue(resource.getCookable())

    def test_cssregistry__extra__enabled(self):
        resource = self.get_css_resource('++theme++santa.theme/css/extra.css')
        self.assertTrue(resource.getEnabled())

    def test_cssregistry__extra__expression(self):
        resource = self.get_css_resource('++theme++santa.theme/css/extra.css')
        self.assertEqual(resource.getExpression(), 'request/HTTP_X_THEME_ENABLED | nothing')

    def test_cssregistry__extra__media(self):
        resource = self.get_css_resource('++theme++santa.theme/css/extra.css')
        self.assertEqual(resource.getMedia(), 'screen')

    def test_cssregistry__extra__rel(self):
        resource = self.get_css_resource('++theme++santa.theme/css/extra.css')
        self.assertEqual(resource.getRel(), 'stylesheet')

    def test_cssregistry__extra__rendering(self):
        resource = self.get_css_resource('++theme++santa.theme/css/extra.css')
        self.assertEqual(resource.getRendering(), 'link')

    def test_cssregistry__extra__applyPrefix(self):
        resource = self.get_css_resource('++theme++santa.theme/css/extra.css')
        self.assertTrue(resource.getApplyPrefix())

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
