
// This triggers flashes with the class type "alert-message' to last for 3 seconds before fading out
setTimeout(() => {
             document.getElementById("alert-message").style.opacity = "0";
            }, 3000);



// This makes the confetti last 3 seconds before disappearing
let confetti = document.getElementsByClassName("confetti");
setTimeout(() => {
  Array.from(confetti).forEach((confetti) => {
  confetti.style.display='none';
})
  }, 3000);

// This triggers confetti to show when the flashes class type is "alert-success" - Hence when the user is correct
const successMessage = document.getElementsByClassName("alert-success")[0];
  if (successMessage) {
    let width = window.innerWidth;
    let height = window.innerHeight;
  
    for (let i = 0; i < 250; i++) {
      let confetti = document.createElement("div");
      confetti.classList.add("confetti");
      confetti.style.left = Math.random() * width + "px";
      confetti.style.top = Math.random() * height + "px";
      confetti.style.backgroundColor =
        "rgb(" +
        Math.floor(Math.random() * 255) +
        "," +
        Math.floor(Math.random() * 255) +
        "," +
        Math.floor(Math.random() * 255) +
        ")";
      confetti.style.transform =
        "rotate(" + Math.floor(Math.random() * 360) + "deg)";
      document.body.appendChild(confetti);
    }
  };