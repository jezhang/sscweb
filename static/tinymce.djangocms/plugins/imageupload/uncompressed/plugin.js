(function() {
    tinymce.create('tinymce.plugins.ImageUploadPlugin', {
        init : function(ed, url) {
            url = tinyMCE.activeEditor.getParam('imageupload_rel') || url;
            var imageUploadUrl = tinyMCE.activeEditor.getParam('imageupload_url');
            var head = document.getElementsByTagName('body')[0];
            var css = document.createElement('link');                       
            css.type = 'text/css';
            css.rel = 'stylesheet';
            css.href = url + '/css/style.css';
            head.appendChild(css);
            
            // Register commands
            ed.addCommand('mceImageUpload', function() {
                django.jQuery('#image_upload_type').val('tinymce'); 
                django.jQuery('body').append('<div class="imageUploadBg"></div>');
                
                var showImageUploadError = function(msg) {
                    django.jQuery('.imageUploadError').html(msg).show();
                    removeForeground();
                };
                
                var removeForeground = function() {
                    django.jQuery('.imageUploadFg').remove();
                    django.jQuery('.imageUploadFgLoading').remove();
                };
                
                var removeBackground = function() {
                    django.jQuery('.imageUploadBg').remove();
                    django.jQuery('.imageUploadContainer').remove();
                };
                
                var container = '\
                    <div class="imageUploadContainer mce-container mce-panel mce-window">\
                        <div class="imageUploadContainerInner">\
                            <div class="mce-window-head">\
                                <div class="mce-title">本地图片上传</div>\
                                <button type="button" class="mce-close">×</button>\
                            </div>\
                            <form action="' + imageUploadUrl + '" method="POST"  enctype="multipart/form-data" id="uploadImageForm">\
                            <div class="mce-container imageUploadFormContainer" hidefocus="1" tabindex="-1">\
                                <div class="mce-container-body">\
                                    <label for="image-upload-area">选择一个文件</label>\
                                    <input type="file" name="file" id="image-upload-area" class="mce-textbox mce-placeholder" hidefocus="true" style="width: 258px;">\
                                </div>\
                                <p class="imageUploadError"></p>\
                            </div>\
                            </form>\
                            <div class="imageUploadConfirmCase mce-panel">\
                                <div class="mce-btn mce-primary">\
                                    <button role="presentation" class="imageUploadSubmit">上传</button>\
                                </div>\
                                <div class="mce-btn">\
                                    <button role="presentation" class="imageUploadClose">退出</button>\
                                </div>\
                            </div>\
                        </div>\
                    </div>\
                ';
                
                django.jQuery('body').append(container);
                
                django.jQuery('.imageUploadBg, .imageUploadContainer .imageUploadClose, .mce-close').on('click', function(){
                    removeForeground();
                    removeBackground();
                });
                
                django.jQuery('#uploadImageForm').iframePostForm({
                    json: true,
                    post: function(){
                        // Sending.
                    },
                    complete: function(response){

                        if (typeof response != "object" || response == null || typeof response.error == 'undefined') {
                            removeForeground();
                            showImageUploadError('An error occurred while uploading your image.');
                        } else {
                            if (response.error != false) {
                                switch (response.error) {
                                    case ("filetype"):
                                        showImageUploadError('Please select a valid image and try again.');
                                        break;
                                    default:
                                        showImageUploadError('An unknown error occurred.');
                                        break;
                                }
                            } else {
                                if (typeof response.path != 'undefined') {
                                    var tpl = '<img src="%s" />';
                                    ed.insertContent(tpl.replace('%s', response.path));
                                    ed.focus();
                                    removeForeground();
                                    removeBackground();
                                } else {
                                    showImageUploadError('An unknown error occurred.');
                                }
                            }
                        }
                    }
                });
                
                django.jQuery('.imageUploadSubmit').on('click', function(){
                    
                    django.jQuery('.imageUploadError').html('').hide();
                    
                    if (django.jQuery('#image-upload-area').val() != '') {
                        django.jQuery('body').append('<div class="imageUploadFg"></div>');
                        django.jQuery('body').append('<div class="imageUploadFgLoading"></div>');
                        django.jQuery('#uploadImageForm').submit();
                    } else {
                        showImageUploadError('Please select an image to upload.');
                    }
                    
                });
            });

            // Register buttons
            ed.addButton('imageupload', {
                title : 'Image Upload',
                cmd : 'mceImageUpload',
                image : url + '/img/icon.png'
            });
        },

        getInfo : function() {
            return {
                longname : 'Image Upload',
                author : 'BoxUK',
                authorurl : 'https://github.com/boxuk/tinymce-imageupload',
                infourl : 'https://github.com/boxuk/tinymce-imageupload/blob/master/README.md',
                version : '1.0.0'
            };
        }
    });

    tinymce.PluginManager.add('imageupload', tinymce.plugins.ImageUploadPlugin);
})();
