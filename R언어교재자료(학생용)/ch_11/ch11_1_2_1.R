# ch11_1_2_1.R
# 사칙연산 함수
fourCalcFun <- function(a, b) {
  totValue <- a + b;  minusValue <- a - b
  mulValue <- a * b;  divValue <- a / b
  cat(a, "+", b, "=", totValue, "\n")
  cat(a, "-", b, "=", minusValue, "\n")
  cat(a, "*", b, "=", mulValue, "\n")
  cat(a, "/", b, "=", divValue, "\n")
}

# 두 수의 나눗셈 계산과 나머지를 구하는 함수
divFun <- function(a, b) {
  quotient <- a / b
  remainder <- a %% b
  cat(a, "/", b, "=", quotient, "\n")
  cat(a, "%%", b, "=", remainder, "\n")
}
