# ch11_3_2_1.R
# install.packages( "igraph" )
# library( igraph )

# [단계 1] 데이터파일 불러오기
emp <- read.csv("회사관계도.csv", header = TRUE)

# [단계 2] 관계도를 그리기 위한 데이터 편집하기
name <- paste(emp$성명, emp$직급)	      # “성명”, “직급” 컬럼 결합
superior <- emp$상사
employee <- data.frame(name , superior)	# 직원정보와 상사정보 데이터 프레임 생성

# [단계 3] 그래프 형식으로 데이터 변환하기
g <- graph.data.frame(employee, directed = TRUE)

# [단계 4] 회사 관계도 그리기
plot(g,layout = layout.svd, vertex.size = 5,edge.arrow.size = 0.3)
