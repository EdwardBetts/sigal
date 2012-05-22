#! /usr/bin/env python2
# -*- coding:utf-8 -*-

import os
import unittest

from sigal.image import Gallery
from sigal.settings import read_settings

class TestSettings(unittest.TestCase):
    "Read a settings file and check that the configuration is well done."

    def setUp(self):
        "Read the sample config file"
        self.path = os.path.dirname(__file__)
        default_conf = os.path.join(self.path, 'sample', 'sigal.conf')
        settings = read_settings(default_conf)
        self.gallery = Gallery(settings, os.path.join(self.path, 'sample'))

    def test_filelist(self):
        file_generator = self.gallery.filelist()
        dirpath, dirnames, imglist = file_generator.next()
        self.assertEqual(dirpath, os.path.join(self.path, 'sample'))
        self.assertListEqual(imglist, [])

        reflist = [os.path.join(self.path, 'sample', 'dir2', f)
                   for f in ['test1.jpg', 'test2.jpg']]
        dirpath, dirnames, imglist = file_generator.next()
        self.assertListEqual(imglist, reflist)
