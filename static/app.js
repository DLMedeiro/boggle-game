// Timer Example: W3 Schools
// https://www.w3schools.com/howto/howto_js_countdown.asp

// document.getElementById("start_btn").addEventListener("click", countdown);

// function showTimer() {
//   timer = document.getElementById("timer");
//   timer.innerHTML = "Game Timer: 60s"
// }

// function countdown() {
  // Set the date we're counting down to
  let countDownDate = new Date().setSeconds(new Date().getSeconds() + 61);


  // Update the count down every 1 second
  let x = setInterval(function() {

    // Get today's date and time
    let now = new Date().getTime();
      
    // Find the distance between now and the count down date
    let distance = countDownDate - now;
      
    // Time calculations for days, hours, minutes and seconds
    let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((distance % (1000 * 60)) / 1000);
      
    // Output the result in an element with id="demo"
    document.getElementById("timer").innerHTML = "Game Timer: " + minutes + "m " + seconds + "s ";
    console.log("Game Timer: " + minutes + "m " + seconds + "s ");
      
    // If the count down is over, write some text 
    if (distance < 0) {
      clearInterval(x);
      document.getElementById("timer").innerHTML = "EXPIRED";
      document.getElementById("player_input").innerHTML = "Game Over"
    }
  }, 1000);
