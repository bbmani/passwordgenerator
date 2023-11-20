$(document).ready(function(){
    $('#form').on('submit', function(e){
        $.ajax({
            data: {},
            type: 'POST',
            url: '/'
        })
        .done(function(data){
            $('#output').text(data['output']).show();
        });
        e.preventDefault()
    });
});

function copy_data(containerId) {
    var range = document.createRange();
    range.selectNode(containerId);
    window.getSelection().removeAllRanges();
    window.getSelection().addRange(range);
    document.execCommand("copy")
    window.getSelection().removeAllRanges();
}