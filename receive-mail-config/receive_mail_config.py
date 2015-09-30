from openerp import models, fields, api, _

import logging
_logger = logging.getLogger(__name__)


class receive_mail_config(models.Model):
	_name = "mail.config.receiver"
	_description = "Receives mail config with XML-RPC"

	def receive_settings(self):
		_logger.warn(self)
		return