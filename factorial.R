x <- as.integer(readline("Enter a no: "))
while(x <= 0) {
  x <- as.integer(readline("Enter no: "))
}
if(x > 0) {
  fact <- 1
  for(i in 1:x){
    fact <- fact * i
  }
  cat("Factorial: ", fact)
}
