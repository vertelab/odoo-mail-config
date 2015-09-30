# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api, _
import xmlrpclib

import logging
_logger = logging.getLogger(__name__)

class mail_config(models.Model):
	_inherit = "res.users"

	@api.one
	def sync_settings(self):


		url = 'http://odooutv.vertel.se'
		db = 'xmlrpc_mail_config'
		username = 'admin'
		password = 'admin'

		config = {
			"postfix_active" : self.postfix_active,
			"vacation_active" : self.vacation_active,
			"forward_active" : self.forward_active,
			"forward_address" : self.forward_address,
			"forward_cp" : self.forward_cp,
			"virus_active" : self.virus_active,
			"spam_active" : self.spam_active,
			"spam_tag" : self.spam_tag,
			"spam_tag2" : self.spam_tag2,
			"spam_killevel" : self.spam_killevel,
			"maildir" : self.maildir,
			"transport" : self.transport,
			"quota" : self.quota,
			"domain" : self.domain,
			"password" : self.passwd_mail,
			"mail_alias" : self.mail_alias,
		}


		common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
		uid = common.authenticate(db, username, password, {})		

		models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))

		models.execute_kw(db, uid, password,
		'res.users', 'create', [{
			"postfix_active" : self.postfix_active,
			"vacation_active" : self.vacation_active,
			"forward_active" : self.forward_active,
			"forward_address" : self.forward_address,
			"forward_cp" : self.forward_cp,
			"virus_active" : self.virus_active,
			"spam_active" : self.spam_active,
			"spam_tag" : self.spam_tag,
			"spam_tag2" : self.spam_tag2,
			"spam_killevel" : self.spam_killevel,
			"maildir" : self.maildir,
			"transport" : self.transport,
			"quota" : self.quota,
			"domain" : self.domain,
			"password" : self.passwd_mail,
			"mail_alias" : self.mail_alias,
		}])

		return