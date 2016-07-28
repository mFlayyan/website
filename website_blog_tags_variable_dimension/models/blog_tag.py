# -*- coding: utf-8 -*-
# © 2016 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import api, fields, models

class BlogTag(models.Model):
    _inherit = 'blog.tag'

    # doing it for all blogs. need to make it per-blog.
    min_font = 8.0
    max_font = 24.0

    @api.multi
    def get_blog_most_used_tag_cardinality(self):
        tags = self.env['blog.tag'].search([])
        # NOTE no need to iterate recordset, same value for all records.
        """
        NOTE setting max ranking to 1 to avoid division by 0 when there are 
        no blogposts with tags.
        """
        max_ranking = 1
        for tag in tags:
            max_ranking = max(
                len(tag.post_ids), 
                max_ranking
            )
        for this in self:
            this.max_ranking = float(max_ranking)
        
    max_ranking = fields.Float( 
        string="Higest tag cardinality in this blog", 
        compute=get_blog_most_used_tag_cardinality,
        help="The number of times the most used tag is used in this blog"
    )

    @api.multi
    def get_font_size(self):
        for this in self:
            hits = len(this.post_ids.ids)
            this.font_size_in_cloud = int(
                (hits)/(this.max_ranking) * (
                    this.max_font - this.min_font
                ) + this.min_font
            ) 
    @api.multi
    def get_tag_cardinality(self):
        for this in self:
            this.tag_cardinality = len(this.post_ids.ids)

    tag_cardinality = fields.Integer(
            string="In how many posts is the tag used", 
            compute=get_tag_cardinality
        )

    font_size_in_cloud = fields.Integer(
        string="Font Size of tag in cloud",
        help="size of tag font from 8 to 24 px relative"
             "to the most used tag, that will be allways displayed at 24px",
        compute=get_font_size
    )