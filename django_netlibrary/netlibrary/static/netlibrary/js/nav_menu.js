let nav_menu_is_showed = false

function showNavMenu() {
    if (!nav_menu_is_showed) {
        document.getElementById("dropdownMenu").classList.toggle("show");
    } else {
        document.getElementById("dropdownMenu").classList.remove("show");
    }
}

window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        let dropdowns = document.getElementsByClassName("dropdown-content");
        let i;
        for (i = 0; i < dropdowns.length; i++) {
            let openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}