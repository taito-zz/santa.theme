import unittest


class BaseViewletTestCase(unittest.TestCase):

    def test_templatedir(self):
        from santa.theme.browser import viewlet
        self.assertEqual(getattr(viewlet, 'grokcore.view.directive.templatedir'), 'viewlets')

    def test_subclass(self):
        from five.grok import Viewlet
        from santa.theme.browser.viewlet import BaseViewlet
        self.assertTrue(issubclass(BaseViewlet, Viewlet))

    def test_baseclass(self):
        from santa.theme.browser.viewlet import BaseViewlet
        self.assertTrue(getattr(BaseViewlet, 'martian.martiandirective.baseclass'))

    def test_layer(self):
        from santa.theme.browser.viewlet import BaseViewlet
        from santa.theme.browser.interfaces import ISantaThemeLayer
        self.assertEqual(getattr(BaseViewlet, 'grokcore.view.directive.layer'), ISantaThemeLayer)

    def test_require(self):
        from santa.theme.browser.viewlet import BaseViewlet
        self.assertEqual(getattr(BaseViewlet, 'grokcore.security.directive.require'), ['zope2.View'])
