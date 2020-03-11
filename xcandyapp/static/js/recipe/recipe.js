// let tab__links = document.querySelectorAll(".tab__links");
// for (let i = 0; i < tab__links.length; i++) {
//   tab__links[i].addEventListener("click", function() {
//     let tab_name = this.id.replace("Link", "");
//     let section = this.id.split("-")[1];
//     let tabs_in_section = document.querySelectorAll(`.tab__shells-${section}`);
//     for (let j = 0; j < tabs_in_section.length; j++) {
//       tabs_in_section[j].style.display = "none";
//     }
//     document.getElementById(tab_name).style.display = "flex";
//   });
// }

// Overlay
$(".open").on("click", function() {
    $(".popup-overlay, .popup-content").addClass("active");
  });
  
  //removes the "active" class to .popup and .popup-content when the "Close" button is clicked
  $(".close").on("click", function() {
    $(".popup-overlay, .popup-content").removeClass("active");
  });
  // Overlay end