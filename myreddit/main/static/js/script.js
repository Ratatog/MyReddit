// const hamBurger = document.querySelector("#toggle-btn");

// hamBurger.addEventListener("click", function () {
//   document.querySelector("#sidebar").classList.toggle("expand");
// });

const searchBar = document.querySelector('.searchbar');
const searchElement = document.querySelector('.s-li');

searchElement.style.width = searchBar.offsetWidth + 'px';

document.addEventListener('click', function(event) {
    var target = event.target;
    var searcher = document.getElementById('searcher');
    if (!searcher.contains(target) && !target.classList.contains('has-dropdown')) {
      searcher.classList.remove('show');
    }
    var notif = document.getElementById('notif');
    if (!notif.contains(target) && !target.classList.contains('has-dropdown')) {
        notif.classList.remove('show');
    }
  });