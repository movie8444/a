library(stringi)
string = readline("Enter a string: ")
cat("Length of the string is: ", nchar(string))
rev_str = stri_reverse(string)
cat("\nReversed string: ", rev_str)
if(string == rev_str){
  cat("\nPalindrome")
} else {
  cat("\nNot a palindrome")
}
