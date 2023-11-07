$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.ajax({
      url: apiUrl,
      method: 'GET',
      success: function (data) {
        $('#hello').text(data.hello);
      },
      error: function (error) {
        console.error('Error fetching translation:', error);
      }
    });
  });
});
