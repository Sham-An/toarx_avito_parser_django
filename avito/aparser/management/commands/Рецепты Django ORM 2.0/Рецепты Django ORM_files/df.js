const nav = document.getElementById('df-nav');
const bar_open = document.getElementById('df-nav-bar');
const bar_close = document.getElementById('df-nav-close');


document.addEventListener('click', function(e) {
    if(e.target && e.target == bar_open) {
        nav.style.display = 'block';
        e.preventDefault();
    }

    if(e.target && e.target == bar_close) {
        nav.style.display = 'none';
        e.preventDefault();
     }
});
