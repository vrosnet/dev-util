# Copyright (c) 2009-2010 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import sys


class BuildObject(object):
  """
    Common base class that defines key paths in the source tree.
  """
  def __init__(self, root_dir, static_dir):
    self.devserver_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    self.static_dir = static_dir
    try:
      self.scripts_dir = '%s/src/scripts' % os.environ['CROS_WORKON_SRCROOT']
    except KeyError:
      # Outside of chroot: This is a corner case. Since we live either in
      # platform/dev or /usr/bin/, scripts have to live in ../../../src/scripts
      self.scripts_dir = os.path.abspath(os.path.join(
          self.devserver_dir, '../../../src/scripts'))
