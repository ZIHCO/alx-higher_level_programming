const myList = $('.my_list');
$('#add_item').on('click', function (event) {
  $(myList).append('<li>Item</li>');
});
