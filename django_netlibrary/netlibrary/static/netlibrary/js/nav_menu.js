var dropbtn = document.querySelector('.dropbtn');

var dropdownContent = document.getElementById('myDropdown');

var isDropdownOpen = false;

dropbtn.onclick = function(event) {
    isDropdownOpen = !isDropdownOpen;
    dropdownContent.style.display = isDropdownOpen ? 'block' : 'none';
}

window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        isDropdownOpen = false;
        dropdownContent.style.display = 'none';
    }
}