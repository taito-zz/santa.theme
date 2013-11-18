# -*- coding: utf-8 -*-
from santa.theme.browser.interfaces import IPloneSiteTwitterFeedViewlet
from santa.theme.browser.viewlet import PloneSiteTwitterFeedViewlet
from santa.theme.tests.base import IntegrationTestCase


class PloneSiteTwitterFeedViewletTestCase(IntegrationTestCase):
    """TestCase for PloneSiteTwitterFeedViewlet"""

    def test_subclass(self):
        from collective.base.viewlet import Viewlet as Base
        from fourdigits.portlet.twitter.fourdigitsportlettwitter import Renderer
        self.assertTrue(issubclass(PloneSiteTwitterFeedViewlet, (Base, Renderer)))
        from collective.base.interfaces import IViewlet as Base
        self.assertTrue(issubclass(IPloneSiteTwitterFeedViewlet, Base))

    def test_verifyObject(self):
        from zope.interface.verify import verifyObject
        instance = self.create_viewlet(PloneSiteTwitterFeedViewlet)
        self.assertTrue(verifyObject(IPloneSiteTwitterFeedViewlet, instance))

    def test___init__(self):
        from santa.theme.browser.viewlet import TwitterData
        instance = self.create_viewlet(PloneSiteTwitterFeedViewlet)
        self.assertTrue(isinstance(instance.data, TwitterData))
