document.addEventListener('DOMContentLoaded', () => {
  $(function () {
    $('#add_item').click(function () {
      const txt = document.createElement('li');
      txt.innerHTML = 'Item';

      $('ul.my_list').append(txt);
    });

    $('#remove_item').click(function () {
      $('.my_list li:last-child').remove();
    });

    $('#clear_list').click(function () {
      $('.my_list').empty();
    });
  });
});
