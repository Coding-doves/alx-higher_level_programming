$(function () {
  $('#add_item').click(function () {
    const txt = document.createElement('li');
    txt.innerHTML = 'Item';

    $('ul').append(txt);
  });
});
