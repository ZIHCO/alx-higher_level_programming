$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, statusText) {
    $('DIV#hello').text(data.hello);
  });
});
