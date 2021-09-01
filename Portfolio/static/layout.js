//checkbox.addEventListener( 'change', function() {
//         localStorage.setItem('dark',this.checked);
//         if(this.checked) {
//              body.classList.add('dark')
//         } else {
//              body.classList.remove('dark')
//         }
//    });

window.onload = function() {myFunction()};
function myFunction() {

  if(localStorage.getItem('dark')=="dark") {
        document.documentElement.setAttribute("data-theme", "dark");
        document.getElementById("theme-switcher").checked = true;

    }
    else {
    document.documentElement.setAttribute("data-theme", "light");
        document.getElementById("theme-switcher").checked = false;
    }
}

document.addEventListener("DOMContentLoaded", function(event) {
    document.documentElement.setAttribute("data-theme", "light");

    // Get our button switcher
    var themeSwitcher = document.getElementById("theme-switcher");

    // When our button gets clicked
    themeSwitcher.onclick = function() {
      // Get the current selected theme, on the first run
      // it should be `light`
      var currentTheme = document.documentElement.getAttribute("data-theme");

      // Switch between `dark` and `light`
      var switchToTheme = currentTheme === "dark" ? "light" : "dark"

      localStorage.setItem('dark',switchToTheme);

      // Set our currenet theme to the new one
      document.documentElement.setAttribute("data-theme", switchToTheme);
    }
  });