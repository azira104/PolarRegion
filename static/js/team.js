$(document).ready(function() {
    $(".nav ul li:first-child").addClass("active");
    $(".tab:first-child").css("display", "block");
});

$(".nav ul li").click(function() {
    $(this)
        .addClass("active")
        .siblings()
        .removeClass("active");

    const index = $(this).index();
    tabs(index);
});

const tabBtn = document.querySelectorAll(".nav ul li");
const tab = document.querySelectorAll(".tab");

function tabs(panelIndex) {
    tab.forEach(function(node) {
        node.style.display = "none";
    });
    tab[panelIndex].style.display = "block";
}

function addLength() {
    bio.innerText = bio.oldText;
    bio.innerHTML +=
        "&nbsp;" + `<span onclick='bioText()' id='see-less-bio'>See Less</span>`;
    document.getElementById("see-less-bio").addEventListener("click", () => {
        document.getElementById("see-less-bio").style.display = "none";
    });
}

if (document.querySelector(".alert-message").innerText > 9) {
    document.querySelector(".alert-message").style.fontSize = ".7rem";
}