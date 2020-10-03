$('#prefsForm').submit(function (e) {
    $.post('/settings/preferences/', $(this).serialize(), function (data) {
        alert(data);
        $('.message').html(data.message);
    });
    e.preventDefault();
});