pch <- readline(prompt="Enter (rock, paper or scissor): ")
cat("Player chose: ", pch)
choices <- c("rock", "paper", "scissor")
cch <- sample(choices, 1)
cat("\nComputer chose: ", cch)
if(pch == "rock" && cch == "scissor" || pch == "scissor" && cch == "paper" || pch == "paper" && cch == "rock"){
  cat("\nPlayer wins!")
} else if(pch == cch){
  cat("\nComputer and Player made the same choice. There is a tie.")
} else {
  cat("\nComputer wins!")
}
