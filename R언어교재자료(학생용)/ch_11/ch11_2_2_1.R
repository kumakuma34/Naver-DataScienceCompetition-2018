# ch11_2_2_1.R
# [1단계] 텍스트 파일 줄단위로 읽기
news  <- readLines("ch11_1_news.txt")

# [2단계] 텍스트 전처리하기
noun1 <- extractNoun(news)	# 명사 추출
noun2 <- unlist(noun1)		# 리스트를 벡터로 변환
# noun2에서 단어의 글자 수가 2이상인 단어 추출
noun3 <- noun2[nchar(noun2) >= 2]

# [3단계] : 단어의 빈도수 계산
nounCount1 <- table(noun3)
# 빈도가 큰 순서로 정렬해서 앞부분 15개 보기
nounCount <- head(sort(nounCount1, decreasing = TRUE), 15)
print(nounCount)

# [4단계] : WordCloud로 시각화하기(흑백)
wordcloud(names(nounCount), freq = nounCount, scale = c(4,1),
          rot.per = 0.25, min.freq = 2, random.order = FALSE, random.color = TRUE)
