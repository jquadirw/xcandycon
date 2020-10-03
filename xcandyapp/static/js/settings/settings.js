$('#prefsForm').submit(function (e) {
    $.post('/settings/preferences/', $(this).serialize(), function (data) {
        alert('message: ' + data.message);
        $('.message').html(data.message);
    });
    e.preventDefault();
});