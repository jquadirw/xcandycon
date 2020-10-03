$('#prefsForm').submit(function (e) {
    $.post('/settings/preferences/', $(this).serialize(), function (data) {
        alert('data = ' + data);
        alert('data.msg = ' + data.message);
        alert('data[msg] = ' + data['message']);
        $('.message').html(data.message);
    });
    e.preventDefault();
});