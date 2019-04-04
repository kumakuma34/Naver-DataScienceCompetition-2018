# ch11_2_1_1.R
# 성적 데이터 프레임 생성하기
number <- seq(1:5); name <- c("송중기", "전지현", "송혜교", "김태희", "정우성")
kor <- c(58, 63, 85, 69, 90); eng <- c(100, 95, 63, 80, 32)
mat <- c(98, 45, 56, 89, 60); grade <- c("B", "D", "A", "C", "D")
stuInfo <- data.frame(number, name, kor, eng, mat, grade)
colnames(stuInfo) <-c("번호","이름", "국어", "영어", "수학", "등급")
cat("\n성적 데이터 :\n"); print(stuInfo); cat("\n")

# 각 학생의 세과목 합계와 평균 구하기
sPos <- 3;  tPos <- 5;
totScore <- apply(stuInfo[, c(sPos:tPos)],1, sum)
avgScore <- apply(stuInfo[, c(sPos:tPos)],1, mean)
resScore <- data.frame(stuInfo[2],totScore,avgScore)
cat("\n세과목 합계와 평균 :\n"); print(resScore, digits = 4)

# 평균 점수가 70점 초과 학생 추출하기
baseScore <- 70; stuOverBase <- resScore[resScore$avgScore > baseScore, ]
cat("\n", baseScore, "점 이상인 학생은 : \n"); print(stuOverBase, digits = 4)
