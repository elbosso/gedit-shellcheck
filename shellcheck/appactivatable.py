# -*- coding: utf-8 -*-
#    ShellCheck plugin for Gedit
#    Copyright (C) 2016 Xavier Gendre <gendre.reivax@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import GObject, Gedit, Gio

class AppActivatable(GObject.Object, Gedit.AppActivatable):
    __gtype_name__ = "ShellCheckAppActivatable"

    app = GObject.property(type=Gedit.App)

    def __init__(self):
        GObject.Object.__init__(self)
        self._menu_ext = None

    def do_activate(self):
        self._menu_ext = self.extend_menu("tools-section")
        item = Gio.MenuItem.new("Check with ShellCheck", "win.check-with-shellcheck")
        self._menu_ext.append_menu_item(item)

        self.app.set_accels_for_action("win.check-with-shellcheck", ["<Ctrl>J"])

    def do_deactivate(self):
        self.app.set_accels_for_action("win.check-with-shellcheck", [])
        self._menu_ext = None
