$(document).ready(function() {
    "use strict";

    var website = openerp.website;
    var _t = openerp._t;

    if ($('.website_blog').length) {
        website.EditorBar.include({
            edit: function () {
                var self = this;
                $('.popover').remove();
                var smallHeight = 200;
                debugger;
                if ($('.cover')[0].attributes.class.textContent.indexOf('js_smallheight') !== -1) {
                    $('body').on('click','#change_cover_small',_.bind(this.change_bg_s, self.rte.editor, smallHeight));
                    $('body').on('click', '#clear_cover_small',_.bind(this.clean_bg_s, self.rte.editor, smallHeight));
                }

                this._super();
            },
            clean_bg_s : function(smallHeight) {
                var self = this;
                var _super = this._super;
                $('.js_smallheight').css({"background-image":'none', 'min-height': smallHeight});
            },
            change_bg_s : function(smallHeight) {
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
    }
});
