pytriplet = function(a, b, c){
  if(a^2 + b^2 == c^2){ return (TRUE) } else { return (FALSE) }
}
x = as.integer(readline("Enter number1: "))
y = as.integer(readline("Enter number2: "))
z = as.integer(readline("Enter number3: "))
if(pytriplet(x, y, z)){ print("It is a Pythagorean triplet") } else { print("It is not a Pythagorean triplet") }
