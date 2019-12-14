$(function () {
    var items;
    var fileIdCounter = 0;
    var filesToUpload = [];

    $(".frame-detail").each(function () {
        $(this).modalForm({
          formURL: $(this).data('id'),
          modalContent: ".modal-content-dbmf",
          modalForm: ".modal-content-dbmf form"
        });
    });

    $(".frame-stats").each(function () {
        $(this).modalForm({
          formURL: $(this).data('id'),
          modalContent: ".modal-content-dbmf",
          modalForm: ".modal-content-dbmf form"
        });
    });

    $(".frame-correlation").each(function () {
        $(this).modalForm({
              formURL: $(this).data('id'),
          modalContent: ".modal-content-dbmf",
          modalForm: ".modal-content-dbmf form"
        });
    });

    $(".frame-heatmap").each(function () {
        $(this).modalForm({
          formURL: $(this).data('id'),
          modalContent: ".modal-content-dbmf",
          modalForm: ".modal-content-dbmf form"
        });
    });

    $('#filecard').change(function() {
        alert('i am ready');
        var contains = filesToUpload.length == 0 ? false : true;
        if (contains) {
            $('#filecard').show();
        }
        else {
            $('#filecard').hide();
        }
    });

    $('#id_filefield').bind('change', function(evt) {
        var output = [];

        for (var i = 0; i < evt.target.files.length; i++) {
            fileIdCounter++;
            var file = evt.target.files[i];
            var fileId = fileIdCounter;

            filesToUpload.push({
                id: fileId,
                file: file
            });

            var removeLink = "<a class=\"removeFile\" href=\"#\" data-fileid=\"" + fileId + "\">Remove</a>";

            output.push("<tr><td>", escape(file.name), "</td><td>", formatBytes(file.size, 1), "</td><td>", removeLink, "</td></tr>");
        };

        var filelisthtml = output.join("");
        $('#filelist').html(filelisthtml);
    });

    $(document).on('click', "a.removeFile", function(e) {
        e.preventDefault();

        alert('filesToUpload (b) = ' + filesToUpload);
        var fileId = $(this).parent().children("a").data("fileid");

        for (var i = 0; i < filesToUpload.length; ++i) {
            if (filesToUpload[i].id === fileId)
                filesToUpload.splice(i, 1);
        }

        $(this).parent().parent().remove();
        alert('filesToUpload (a) = ' + filesToUpload);
    });

    $(this).on("click", ".removeFile", function (e) {
        alert('remove file clicked');
        e.preventDefault();

        var fileId = $(this).parent().children("a").data("fileid");

        for (var i = 0; i < filesToUpload.length; ++i) {
            if (filesToUpload[i].id === fileId)
                filesToUpload.splice(i, 1);
        }

        $(this).parent().remove();
    });

    function formatBytes(bytes,decimals) {
        if(bytes == 0) return '0 Bytes';
        var k = 1024,
        dm = decimals <= 0 ? 0 : decimals || 2,
        sizes = ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
        i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    }

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-frame .modal-title").html("");
                $("#modal-frame .modal-content").html("");
                $("#modal-frame .modal-footer .submit-btn").hide();
                $("#modal-frame").modal("show");
            },
            success: function (data) {
                $("#modal-frame .modal-title").html(data.html_title);
                $("#modal-frame .modal-content").html(data.html_form);
            }
        });
    };

    var loadDynamicForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-frame .modal-title").html("");
                $("#modal-frame .modal-content").html("");
                $("#modal-frame .modal-footer .submit-btn").show();
                $("#modal-frame").modal("show");
            },
            success: function (data) {
                $("#modal-frame .modal-title").html(data.html_title);
                $("#modal-frame .modal-content").html(data.html_form);
            }
        });
    };

    var saveDynamicForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                  $("#modal-frame .modal-title").html(data.html_title);
                  $("#modal-frame .modal-content").html(data.html_form);
                }
            }
        });

        return false;
    };

    $(".correlation-form").submit(function(e) {
        var postUrl = $(this).attr('action');

        var formdata = $(this).serialize();
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();

        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: postUrl,
            data: formdata,
            success: function(data) {
                alert('data = ' + data);
                var cresponse = jQuery.parseJSON(data);
                $('#correlationModal .modal-dialogs .modal-content .modal-body .correlation').html('<img src="' + cresponse.uri + '" />');
                $('#correlationModal').modal({backdrop:'static', keyboard:false, show:true});
            },
            error: function (jqXHR, textStatus, errorThrown) {
                $('#correlationModal').modal('hide');
                $('#errorModal').modal({backdrop:'static', keyboard:false, show:true});
            }
        });
        return false;
    });

    /* Binding */

    // Show head
    $(".card .card-body .js-frame-head").click(loadForm);

    // Show statistics
    $(".card .card-body .js-frame-statistics").click(loadForm);

    // Show correlation
    $(".card .card-body .js-frame-correlation").click(loadDynamicForm);
    $("#modal-frame").on("submit", ".js-correlation-form", saveDynamicForm);

    // Show heatmap
    $(".card .card-body .js-frame-heatmap").click(loadDynamicForm);
    $("#modal-frame").on("submit", ".js-heatmap-form", saveDynamicForm);
});
