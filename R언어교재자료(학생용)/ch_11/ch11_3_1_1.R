# ch11_3_1_1.R
# install.packages("ggmap")
# library(ggmap)

# [단계 1] 데이터파일 불러오기
tempPerc <- read.csv("한국평균기온강수량.csv",header=TRUE)
print(tempPerc)

# [단계 2] 지도 불러오기
kor <- get_map("jeonju", zoom = 7, maptype = "terrain")
korMap <- ggmap(kor)
print(korMap)

# [단계3] 지도상의 도시에 평균강수량 표시하기
percMap <- korMap + geom_point(data = tempPerc, aes(x = LON, y = LAT, colour = 강수량, size = 강수량))
print(percMap)

# [단계 4] 지도상의 도시에 도시이름 표시하기
percMap1 <- percMap + geom_text(data = tempPerc, aes(x = LON + 0.2, y = LAT + 0.2, label = 지역), size = 5, colour = "black" )
print(percMap1)

# [단계 5] 한국 평균강수량 지도 그림파일로 저장하기
ggsave("한국_평균강수량.jpg", scale = 2, width = 7, height = 4, dpi = 800)
