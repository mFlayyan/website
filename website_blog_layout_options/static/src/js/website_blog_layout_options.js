$(document).ready(function() {
    "use strict";

    var website = openerp.website;
    var _t = openerp._t;

    if ($('.website_blog').length) {
        website.EditorBar.include({
            edit: function () {
                var self = this;
                debugger;
                $('.popover').remove();
                this._super();
                var smallHeight = $(window).height();
                $('body').on('click','#change_cover_small',_.bind(this.change_bgs, self.rte.editor, smallHeight));
                $('body').on('click', '#clear_cover_small',_.bind(this.clean_bgs, self.rte.editor, smallHeight));
            },
            save : function() {
                var self = this;
                var _super = this._super;
                if ($('.cover').length) {
                    return openerp.jsonRpc("/blogpost/change_background", 'call', {
                        'post_id' : $('#blog_post_name').attr('data-oe-id'),
                        'image' : $('.cover').css('background-image').replace(/url\(|\)|"|'/g,''),
                    }).then(function () {
                        return _super.call(self);
                    });
                } else {
                    return this._super();
                }
            },
            clean_bgs : function(smallHeight) {
                debugger;
                $('.js_smallheight').css({"background-image":'none', 'min-height': smallHeight});
            },
            change_bgs : function(smallHeight) {
                debugger;
                var self  = this;
                var element = new CKEDITOR.dom.element(self.element.find('.cover-storage').$[0]);
                var editor  = new website.editor.MediaDialog(self, element);
                $(document.body).on('media-saved', self, function (o) {
                    var url = $('.cover-storage').attr('src');
                    $('.js_smallheight').css({"background-image": !_.isUndefined(url) ? 'url(' + url + ')' : "", 'min-height': smallHeight});
                    $('.cover-storage').hide();
                });
                editor.appendTo('body');
            },
        });
        $('.js_smallheight').css('min-height', 200);
    }
});
