$('.btn-view').click(function(){
		$('.hidden-comments').toggleClass('unhide-comments');
				});

$('.btn-form').click(function(){
		$('.hidden-form').toggleClass('unhide-form');
				});

$('.toggle-like').click(function(){
		$('.no-color').toggleClass('like-color');
				});

function myFunction() {
  // Declare variables
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById('myInput');
  filter = input.value.toUpperCase();
  ul = document.getElementById("myUL");
  li = ul.getElementsByTagName('li');

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < li.length; i++) {
    a = li[i].getElementsByTagName("a")[0];
    txtValue = a.textContent || a.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}