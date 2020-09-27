# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

# from odoo import api, fields, models
from odoo import api, fields

_logger = logging.getLogger(__name__)

try:
    from erpbrasil.base import misc
except ImportError:
    _logger.error("Biblioteca erpbrasil.base não instalada")


# class Partner(models.Model):
#     _inherit = "res.partner"

#     def _display_address(self, without_company=False):
#         country_code = self.country_id.code or ""
#         if self.country_id and country_code.upper() != "BR":
#             # this ensure other localizations could do what they want
#             return super(Partner, self)._display_address(without_company=False)
#         else:
#             address_format = (
#                 self.country_id
#                 and self.country_id.address_format
#                 or "%(street_name)s, %(street_number)s %(street2)s\n%(district)s"
#                 "\n%(zip)s - %(city)s-%(state_code)s\n%(country_name)s"
#             )
#             args = {
#                 "city_name": self.city_id and self.city_id.name or "",
#                 "state_code": self.state_id and self.state_id.code or "",
#                 "state_name": self.state_id and self.state_id.name or "",
#                 "country_code": self.country_id and self.country_id.code or "",
#                 "country_name": self.country_id and self.country_id.name or "",
#                 "company_name": self.parent_id and self.parent_id.name or "",
#             }

#             address_field = [
#                 "title",
#                 "street_name",
#                 "street2",
#                 "zip",
#                 "city",
#                 "street_number",
#                 "district",
#             ]
#             for field in address_field:
#                 args[field] = getattr(self, field) or ""
#             if without_company:
#                 args["company_name"] = ""
#             elif self.parent_id:
#                 address_format = "%(company_name)s\n" + address_format
#             return address_format % args

    city_id = fields.Many2one(domain="[('state_id', '=', state_id)]")

    country_id = fields.Many2one(default=lambda self: self.env.ref("base.br"))

    district = fields.Char(string="District", size=32)

    # @api.model
    # def _address_fields(self):
    #     """Returns the list of address
    #     fields that are synced from the parent."""
    #     return super(Partner, self)._address_fields() + ["district"]

    # def get_street_fields(self):
    #     """Returns the fields that can be used in a street format.
    #     Overwrite this function if you want to add your own fields."""
    #     return super(Partner, self).get_street_fields() + ["street_name"]

    # def _set_street(self):
    #     company_country = self.env.user.company_id.country_id
    #     if company_country.code:
    #         if company_country.code.upper() != "BR":
    #             return super(Partner, self)._set_street()

    @api.onchange("zip")
    def _onchange_zip(self):
        self.zip = misc.format_zipcode(self.zip, self.country_id.code)

    @api.onchange("city_id")
    def _onchange_city_id(self):
        self.city = self.city_id.name
