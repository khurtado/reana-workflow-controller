# -*- coding: utf-8 -*-
#
# This file is part of REANA.
# Copyright (C) 2017 CERN.
#
# REANA is free software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# REANA is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# REANA; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307, USA.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization or
# submit itself to any jurisdiction.

"""Models for REANA Workflow Controller."""

from __future__ import absolute_import

from sqlalchemy_utils.types import UUIDType

from .factory import db


class Tenant(db.Model):
    """Tenant model."""

    id_ = db.Column(UUIDType, primary_key=True)
    api_key = db.Column(db.String(120))
    create_date = db.Column(db.DateTime, default=db.func.now())
    email = db.Column(db.String(255), unique=True)
    last_active_date = db.Column(db.DateTime)

    def __init__(self, id_, email, api_key):
        """Initialize tenant model."""
        self.id_ = id_
        self.email = email
        self.api_key = api_key

    def __repr__(self):
        """Tenant string represetantion."""
        return '<User %r>' % self.id_