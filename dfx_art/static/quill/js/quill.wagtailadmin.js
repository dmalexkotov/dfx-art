function setupQuillAdmin(fieldId){
    const quill = new Quill(`#editor_${fieldId}`, {
        modules: {
            dragAndDrop: {
                draggables: [
                  {
                    content_type_pattern: '^image/', // Any file with matching type will result in ...
                    tag: 'img', // ... an 'img' tag ...
                    attr: 'src' // ... with 'src' equal to the file's base64 (or the result of `onDrop` [see below]).
                  }
                ]
            },
            toolbar: {
                container: `#editor_${fieldId}_toolbar`,
                handlers: {
                    'image': function () {
                        ModalWorkflow({
                            url: window.chooserUrls.imageChooser,
                            onload: IMAGE_CHOOSER_MODAL_ONLOAD_HANDLERS,
                            responses: {
                                imageChosen: function(imageData) {
                                    let range = quill.getSelection(true);
                                    const Delta = Quill.import('delta');
                                    const nameArray = imageData.preview.url.split('\\').pop().split('/').pop().split('.');
                                    let fileName;
                                    if (nameArray.length > 2) {
                                        nameArray.splice(-2, 1);
                                        fileName = nameArray.join('.');
                                    } else {
                                        fileName = nameArray.join('.');
                                    }
                                    quill.updateContents(
                                        new Delta()
                                        .retain(range.index)
                                        .delete(range.length)
                                        .insert({ image: `/media/original_images/${fileName}` }),
                                        Quill.sources.USER
                                    );
                                }
                            }
                        });
                    },
                    'link': function () {
                        ModalWorkflow({
                            url: chooserUrls.externalLinkChooser,
                            onload: PAGE_CHOOSER_MODAL_ONLOAD_HANDLERS,
                            responses: {
                                pageChosen: function(pageData) {
                                    let range = quill.getSelection(true);
                                    const Delta = Quill.import('delta');
                                    console.log(pageData, this);
                                    quill.formatText(
                                        range.index, range.length, 'link', pageData.url
                                    )
                                }
                            }
                        });
                    },
                }
            },
        },
        theme: 'snow',
    });
    const savedValue = $(`#${fieldId}`).attr("value");
    if (savedValue) {
        try {
            const editorContent = JSON.parse(savedValue)
            quill.setContents(editorContent)
        } catch (error) {
            quill.clipboard.dangerouslyPasteHTML(savedValue)
        }
    }
    quill.on('editor-change', function() {
        $(`#${fieldId}`).attr(
            "value",
            JSON.stringify(quill.getContents())
        );
    });
};