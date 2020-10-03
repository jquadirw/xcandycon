$('#prefsForm').submit(function (e) {
    $.post('/settings/preferences/', $(this).serialize(), function (data) {
        alert('data = ' + data);
        alert('msg = ' + data.message);
        $('.message').html(data.message);
    });
    e.preventDefault();
});