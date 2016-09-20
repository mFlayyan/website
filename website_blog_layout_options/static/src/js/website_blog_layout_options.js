$(document).ready(function() {
    "use strict";

    var website = openerp.website;
    var _t = openerp._t;
    
    if ($('.website_blog').length) {
       website.EditorBar.include({
            clean_bg : function(vHeight) {
                $('.js_fullheight').css({"background-image":'none', 'min-height': vHeight});
                $('.js_smallheight').css({"background-image":'none'});
            },
            change_bg : function(vHeight) {
                var self  = this;
                var element = new CKEDITOR.dom.element(self.element.find('.cover-storage').$[0]);
                var editor  = new website.editor.MediaDialog(self, element);
                $(document.body).on('media-saved', self, function (o) {
                    var url = $('.cover-storage').attr('src');
                    $('.js_fullheight').css({"background-image": !_.isUndefined(url) ? 'url(' + url + ')' : "", 'min-height': vHeight});
                    $('.js_smallheight').css({"background-image": !_.isUndefined(url) ? 'url(' + url + ')' : ""});
                    $('.cover-storage').hide();
                });
                editor.appendTo('body');
            },
        });
    }
});
