CKEDITOR.replace('editor', {
    toolbar: [
        {name: 'document', items: ['Source', '-', 'Bold', 'Italic', 'Underline']},
        {name: 'clipboard', items: ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
        {name: 'insert', items: ['Image', 'EmbedSemantic', 'Table', 'HorizontalRule']},
        {name: 'links', items: ['Link', 'Unlink']},
        '/',
        {name: 'styles', items: ['Styles', 'Format', 'Font', 'FontSize']},
        {name: 'colors', items: ['TextColor', 'BGColor']},
    ],
    extraPlugins: 'embed,autoembed',
    embed_provider: '//ckeditor.iframe.ly/api/oembed?url={url}&callback={callback}'
});