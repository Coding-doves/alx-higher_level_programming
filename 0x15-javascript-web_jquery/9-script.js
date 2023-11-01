$(function () {
  $.get({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    dataType: 'json',
    success: function (data) {
      $('#hello').html(data.hello);
    }
  });
});
