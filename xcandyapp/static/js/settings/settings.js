$('#prefsForm').submit(function (e) {
    alert('in the form');
    $.post('/settings/preferences/', $(this).serialize(), function (data) {
        alert('after posting');
        $('.message').html(data.message);
    });
    e.preventDefault();
});