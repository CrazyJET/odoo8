# -*- coding: utf-8 -*-
import json

from openerp import models, fields, api

class tree_add_button(models.Model):
    _name = 'tree_add_button.tree_add_button'

    #     name = fields.Char()
    @api.multi
    def action_get_product_import_csv(self):
        # 跳转到url
        paras_str = json.dumps({'state': 'ok'}, encoding="UTF-8", separators=(',', ':'))
        url = '/w/product_import_qw';
        url = url + '?jdat=' + paras_str;
        return {
            "type": "ir.actions.act_url",
            "url": url,
            "target": "new",
        }
