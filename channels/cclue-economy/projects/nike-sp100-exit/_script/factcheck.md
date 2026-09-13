# 팩트체크

> 프로젝트: nike-sp100-exit
> 검증일: 2026-09-12
> 대상: 레퍼런스 001~007
> 환율 기준: 1달러 = 약 1,340원 (2026년 9월 초 서울 외환시장, 1,336~1,369원 구간)

---

## 1. 지수 제외 사건

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| "나이키가 에스앤피 100에서 퇴출" | 001,002,003,004,005,006,007 | ❌ | **"퇴출"이 아니라 정기 리밸런싱에 따른 구성종목 "제외(deletion)"**. S&P는 "각 지수가 해당 시가총액 구간을 더 잘 대표하도록 하기 위한 조정"이라고만 설명했고 나이키를 뺀 개별 사유는 밝히지 않았다 | S&P Global — "Bloom Energy, Illumina, and Everpure Set to Join S&P 500; Others to Join S&P 100…", https://press.spglobal.com/2026-09-04-Bloom-Energy,-Illumina,-and-Everpure-Set-to-Join-S-P-500-Others-to-Join-S-P-100,-S-P-MidCap-400,-and-S-P-SmallCap-600 |
| 발표 주체: 에스앤피 다우존스 인디시즈 | 005 | ✅ | S&P Dow Jones Indices, 분기 정기 리밸런싱 | 위 동일 |
| 발표일 "2026년 9월 6일" | 002 | ❌ | **2026년 9월 4일(금)** 발표 | 위 동일 |
| 발효일 "9월 20일" | 002 | ❌ | **2026년 9월 21일(월) 미국 장 개시 전**. 실제 리밸런싱 체결은 9월 18일(금) 종가 동시호가 | S&P Global 보도자료 / top1markets — "Nike's S&P 100 Removal: How to Size the Forced Selling", https://www.top1markets.com/insights/stocks/nike-index-deletion-passive-selling-estimate-2026 |
| 발효일 "9월 21일" | 005,006,002(일부) | ✅ | 정확 | 위 동일 |
| 에스앤피 500에는 잔류 | 005 | ✅ | S&P 500 구성종목 유지. 다우존스 산업평균지수에도 잔류 중 | Fortune — "Nike exits the S&P 100 after 18 years and a $200 billion market-cap wipeout", https://fortune.com/2026/09/08/nike-stock-plummets-sp500-market-cap-index/ |
| 2008년 12월 에스앤피 100 편입 | 002,005 | ✅ | 2008년 12월 편입. 제외까지 약 17년 9개월 | Vested Finance — "Why Nike Was Removed from the S&P 100 Index", https://vestedfinance.com/blog/us-stocks/why-is-nike-being-removed-from-sp-100/ |
| "18년 만" | 001~007 다수 | ⚠️ 반올림 | 정확히는 **17년 9개월**. 영문 보도는 "nearly 18 years"로 표기 | Seeking Alpha — "Nike booted from S&P 100 after nearly 18-year run", https://seekingalpha.com/news/4640534-nike-booted-from-sp-100-after-nearly-18-year-run |
| 함께 제외: 허니웰·사이먼프로퍼티그룹·콜게이트파몰리브 | 002,003,004 | ✅ | 정확. **단, 허니웰의 정체가 다르다** — 제외된 것은 2026년 6월 29일 분사 상장한 **허니웰 에어로스페이스(HONA)**이며, 6월 29일 에스앤피 100에 편입됐다가 3개월 만에 빠진 것이다. "전통 산업 대기업의 퇴조" 프레임으로 묶으면 부정확 | S&P Global — "Honeywell Aerospace Set to Join S&P 500 & S&P 100", https://press.spglobal.com/2026-06-23-Honeywell-Aerospace-Set-to-Join-S-P-500-S-P-100-Others-to-Join-S-P-MidCap-400-and-S-P-SmallCap-600 |
| 신규 편입: 델·팔로알토네트웍스·아리스타네트웍스·샌디스크 | 002,003,004 | ✅ | 4곳 전원 정보기술 섹터 | S&P Global 보도자료 / Vantage Markets — "Nike Exits The S&P 100 As Four Tech Stocks Move In", https://www.vantagemarkets.com/market-news/nike-exits-sp100-tech-stocks-replace-september-7-2026/ |
| "지수 추종 펀드는 기계적으로 매도할 수밖에 없다 → 나이키에 악재" | 001,003 | ⚠️ 과장 | 방향은 맞지만 **규모가 미미**하다. 아래 9번 항목 참조 | — |

---

## 2. 주가 · 시가총액

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| 2021년 11월 고점 주가 179달러 | 002 | ✅ | **2021년 11월 5일 179.10달러** (사상 최고가) | Benzinga — "NKE Stock Erases $200 Billion In Market Cap Since 2021 Peak", https://www.benzinga.com/markets/equities/26/08/61265732/nke-stock-erases-200-billion-in-market-cap-since-2021-peak-arvy-cio-warns-of-a-stage-4-decline |
| 고점 시총 2,640억 달러 | 002,006 | ✅ | 약 2,640억 달러 | 위 동일 / Fortune |
| 고점 시총 "한화 약 310조원" | 002 | ✅ | 2021년 11월 환율(약 1,180원) 기준 약 311조원 — 당시 기준으로는 정확 | 환율: 한국은행 기준 |
| 현재 주가 38.4달러 | 006 | ✅ | **2026년 9월 4일 종가 38.40달러** | top1markets, 위 URL |
| 현재 주가 "38달러" | 002,004 | ✅ | 동일 | 위 동일 |
| "주당 51달러 / 목표주가 50~52달러" | 002 | ✅ | 현재 주가가 아니라 **애널리스트 1년 목표주가**다. 2026년 9월 기준 컨센서스 평균 **49.9~50.7달러**(최고 94달러·최저 23달러), 투자의견 '보유' | StockAnalysis — "NIKE, Inc. (NKE) Stock Forecast & Analyst Price Targets", https://stockanalysis.com/stocks/nke/forecast/ |
| 고점 대비 78% 하락 | 002,004,006 | ✅ | **직접 계산: 38.40 ÷ 179.10 = 0.2144 → -78.6%** | 계산 검증 |
| 고점 대비 "80% 폭락" | 002(투자자 문단) | ❌ | 78.6%. 80%는 과장 | 계산 검증 |
| 현재 시총 570억 달러 | 006 | ✅ | 약 570억 달러 (약 76조원) | Fortune, 위 URL |
| 증발한 시총 "2,200억 달러 / 300조원" | 004 | ❌ | **2,640억 → 570억 = 약 2,070억 달러 증발**. 현 환율(1,340원) 기준 **약 277조원**. Fortune 헤드라인도 "$200 billion wipeout" | Fortune, 위 URL |
| 증발한 시총 "2,000억 달러 이상 / 270조원" | 002 | ✅ | 약 2,070억 달러. 원화 환산도 근사 | 위 동일 |
| "300조원이 증발" (훅) | 002 | ❌ | 약 277조원. 300조는 과장 | 계산 검증 |
| 2026년 들어서만 시총 -36% | — | ✅ | 2026년 연초 대비 시총 -36%, 주가 -38% | Fortune / StockAnalysis |
| 2024년 6월 하루 -20%, 시총 280억 달러 증발, 상장 이래 최악의 하루 | 002 | ✅ | **2024년 6월 28일**, 하루 20% 하락, 시총 약 280억 달러 증발. 1980년 상장 이후 일간 최대 낙폭 | Forbes — "Nike Stock Tanks 20% To 4-Year Low", https://www.forbes.com/sites/dereksaul/2024/06/28/nike-stock-tanks-almost-20-to-4-year-low-why-the-sneaker-giants-struggling/ |
| "같은 기간 비트코인보다 더 떨어졌다" | 002 | ❓ | 신뢰할 수 있는 비교 출처 없음. 사용 금지 | 검색 결과 없음 |
| 나이키의 현재 위상 | — | ✅(신규) | **에스앤피 500 구성종목 중 시가총액 213위**. 다우존스 산업평균지수 30종목 중 최하위, 지수 비중 0.4% | Motley Fool — "Nike Is Being Deleted From the S&P 100. Is Its Seat in the Dow Jones Industrial Average in Jeopardy?", https://www.fool.com/investing/2026/09/12/nike-just-got-deleted-from-the-sp-100-is-its-seat/ |

---

## 3. 실적

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| 2026 회계연도 매출 464억 달러 | 001 | ✅ | **FY2026 매출 464억 달러**, 보고 기준 보합, 환율중립 -2% | 나이키 IR — "NIKE, Inc. Reports Fiscal 2026 Fourth Quarter and Full Year Results", https://about.nike.com/en/newsroom/releases/nike-inc-reports-fiscal-2026-fourth-quarter-and-full-year-results |
| 환율중립 기준 -2% | 001 | ✅ | 동일 | 위 동일 |
| FY2024 514억 달러 → FY2025 463억 달러, -10% | 002 | ✅ | FY2024 514억 달러, FY2025 463억 달러, 보고 -10% / 환율중립 -9% | 나이키 IR FY2025 실적 발표, https://investors.nike.com/investors/news-events-and-reports/investor-news/investor-news-details/2025/NIKE-Inc--Reports-Fiscal-2025-Fourth-Quarter-and-Full-Year-Results/default.aspx |
| 순이익 추이 | — | ✅(신규) | FY2024 57억 달러 → **FY2025 32.2억 달러(-44%)** → **FY2026 31.1억 달러(-3%)**. FY2026 주당순이익 2.10달러 | 나이키 IR FY2026 발표 / Fibre2Fashion — "US' Nike FY25 revenue falls 10%, net income drops 44%", https://www.fibre2fashion.com/news/retail-industry/us-nike-fy25-revenue-falls-10-net-income-drops-44--303568-newsdetails.htm |
| 앱·직영 -8%, 도매 +4% (환율중립) | 001 | ✅ | FY2026 나이키 다이렉트 177억 달러(보고 -6%, 환율중립 -8%), 도매 275억 달러(보고 +6%, 환율중립 +4%) | 나이키 IR FY2026 발표 |
| FY2026 중화권 매출 58.5억 달러, -11% | 002 | ✅ | 중화권 FY2026 보고 기준 -11%, 환율중립 -13%. 4분기 13.0억 달러(-12% 보고, -17% 환율중립) | 나이키 IR FY2026 / Retail Insight Network — "Nike swings to Q4 profit on tariff refund boost, but China slump deepens", https://www.retail-insight-network.com/news/nike-q4-profit-china-slump-deepens/ |
| 중국 "7분기 연속 하락" | 002 | ❌ | **8분기 연속** | CNBC — "Nike was once China's sneaker king. Here's why its sales have fallen 30%", https://www.cnbc.com/2026/07/29/nike-china-sales-decline.html |
| 중국 "8개 분기 연속 매출 감소" | 003 | ✅ | 정확 | 위 동일 |
| 중국 매출 2021년 이후 30% 가까이 감소 | 002 | ✅ | 2026년 5월 기준 중국 연 매출이 8년 만의 최저. 2021년 정점 대비 약 30% 감소 | 위 동일 |
| FY2026 4분기 순이익 급증 | — | ✅(신규·중요) | Q4 순이익 11억 달러(+407%)인데 이는 **미국 관세(IEEPA) 환급 9.86억 달러** 덕분. 주당 0.52달러가 관세 환급분. 본업 개선이 아니다 | CNBC — "Nike results top estimates even as China sales drop 12%; retailer expects $986 million tariff refund", https://www.cnbc.com/2026/06/30/nike-nke-q4-2026-earnings.html |
| 재고 | — | ✅(신규) | FY2026 말 재고 75억 달러, 전년과 동일 | 나이키 IR FY2026 발표 |
| 컨버스 | — | ✅(신규) | FY2026 매출 -31~32% | 나이키 IR FY2026 발표 |
| 2021년 6월 분기 매출 +96% | 005 | ✅ | FY2021 4분기(2021년 3~5월) 매출 123억 달러, 전년 동기 대비 +96%. **단 전년 동기는 코로나 봉쇄로 무너진 분기**라 기저효과 | 나이키 IR — FY2021 4분기 실적, https://investors.nike.com/investors/news-events-and-reports/investor-news/investor-news-details/2021/NIKE-Inc.-Reports-Fiscal-2021-Fourth-Quarter-and-Full-Year-Results/default.aspx |
| 2021년 6월 "순이익 +291%" | 005 | ❌ | 성립하지 않는 수치. 전년 동기는 **7.9억 달러 순손실**이라 증가율 계산이 불가하고, 해당 분기 순이익은 15억 달러. 연간 기준으로는 순이익 25.4억 달러 → 57억 달러로 **+125%**, 희석 주당순이익 +123% | 나이키 IR FY2021 실적 / CNBC — "Nike (NKE) reports Q4 2021 earnings beat", https://www.cnbc.com/2021/06/24/nike-nke-q4-2021-earnings.html |

---

## 4. 창업 · 성장사

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| 블루리본 스포츠 1964년 설립, 각 500달러 | 002 | ✅ | **1964년 1월 25일**, 필 나이트 + 빌 바우어만 각 500달러(총 1,000달러) 출자 | Wikipedia — "Nike timeline", https://en.wikipedia.org/wiki/Nike_timeline / Sneakerjagers — "How Phil Knight made history 60 years ago", https://www.sneakerjagers.com/en/n/how-phil-knight-made-history-60-years-ago-with-founding-blue-ribbon-sports/76181 |
| "1963년으로 가야 합니다" | 002 | ❌ | 창업은 **1964년** | 위 동일 |
| 필 나이트: 오리건대 육상 선수, 스탠퍼드 경영대학원, 오니츠카 타이거 수입, 차 트렁크 판매 | 002 | ✅ | 정확. 오리건주 유진에서 시작, 육상 대회장에서 차 트렁크로 판매 | Wikipedia — "Nike, Inc.", https://en.wikipedia.org/wiki/Nike,_Inc. |
| 빌 바우어만: 올림픽 선수 31명 배출한 오리건대 육상 코치 | 002 | ✅ | 정확 | 위 동일 |
| 창업 첫해 실적 | — | ✅(신규) | 첫해 일본산 러닝화 **1,300켤레 판매, 매출 8,000달러** | Wikipedia — "Nike timeline" |
| 와플 밑창 일화 (아내가 굽던 와플 틀) | 002 | ✅ | 바우어만이 와플 틀 격자무늬에서 접지력을 착안, 고무를 부어 밑창 제작. 제품화는 **1974년 와플 트레이너** | 위 동일 |
| 1971년 나이키로 사명 변경 | — | ✅ | 1971년 나이키로 개명, 같은 해 스우시 로고 제작·와플 트레이너 개발 | 위 동일 |
| 스우시 로고 35달러 | — | ✅ | 포틀랜드주립대 그래픽디자인 전공생 **캐롤린 데이비드슨**이 17.5시간 작업, 시급 2달러로 **35달러** 수령. 1983년 나이키가 주식과 금 스우시 반지를 선물(주식 가치 100만 달러 이상으로 추정) | CNBC — "Here's how much Nike's billionaire founder paid for the infamous swoosh logo in 1971", https://www.cnbc.com/2018/09/05/heres-how-much-nikes-billionaire-founder-paid-for-its-swoosh-logo.html |
| 1980년 상장 | — | ✅ | **1980년 12월 2일 상장, 공모가 주당 22달러**. 1972년 매출 200만 달러 미만 → 1980년 2억 6,980만 달러 | Shortform — "Nike's IPO: When Nike Finally Went Public", https://www.shortform.com/blog/nike-ipo-1980/ |
| 1984년 마이클 조던 계약 "5년 총 250만 달러 + 매출 로열티" | 002 | ✅ | 5년 250만 달러 + 에어조던 판매 로열티. 당시 농구선수 최대 계약의 3배 규모. **로열티율은 공개된 적 없고 업계 추정치는 4~5%** ("25%"로 도는 수치는 근거 없음) | Sportico — "How Michael Jordan Made $300 Million in 2024", https://www.sportico.com/personalities/athletes/2025/michael-jordan-earnings-nike-million-1234849422/ |
| 아디다스가 "키가 작다는 이유로" 거절 | 002 | ❓ | 조던이 아디다스를 선호했고 아디다스가 계약하지 않은 것은 사실이나, "키" 사유는 1차 출처 확인 불가. 대본에서는 사유를 빼고 "아디다스가 잡지 않았다"로만 쓸 것 | 검색 결과 불충분 |
| 에어조던 첫해 매출 1억 2,600만 달러, 목표의 42배 | 002 | ✅ | 나이키 목표 300만 달러 → 실제 첫해 1억 2,600만 달러 (**42배**. 002가 말한 "40 몇 배"와 일치). 일반 판매 개시는 1985년 4월 | JD Sports — "The History of Air Jordan", https://blog.jdsports.com/air-jordan-history/ |
| 조던이 2024년 한 해 나이키에서 약 3억 달러 수령 | 002 | ✅ | 스포티코 추정 2024년 총수입 약 3억 달러(대부분 나이키 로열티). 2025년 나이키 로열티만 약 2.75억 달러. 1984년 이후 누적 지급 추정 23.5억 달러 | Sportico, 위 URL |
| "한화 약 4천억 원" | 002 | ✅ | 3억 달러 × 1,340원 ≈ 4,020억 원 | 계산 검증 |
| 1988년 "저스트 두 잇" 캠페인 시작 | 002 | ✅ | 카피는 1987년 위든+케네디에서 작성, **캠페인 집행은 1988년 8월**. 같은 해 시총 첫 10억 달러 돌파 | Wikipedia — "Just Do It", https://en.wikipedia.org/wiki/Just_Do_It / WWeek — "1988: Just Do It", https://www.wweek.com/culture/2024/11/12/1988-just-do-it/ |
| 1990년대 성장 | — | ✅(신규) | 1988~1998년 북미 운동화 점유율 **18% → 43%**, 세계 매출 **8억 7,700만 달러 → 92억 달러** | Creative Review — "Nike (1987) – Just Do It", https://www.creativereview.co.uk/just-do-it-slogan/ |
| 1990년대 후반 하청공장 노동 논란 | — | ✅(신규) | 1991년 제프 밸린저가 인도네시아 하청공장 보고서 발표 — **시급 14센트, 현지 최저임금 미달**. 1992년 바르셀로나 올림픽 시위, 1993년 CBS 보도, 1997년 미국 대학가 불매. **1998년 5월 필 나이트 연설**: "나이키 제품은 노예 임금과 강제 노동, 자의적 학대의 동의어가 됐다"며 최저임금 인상·공장 공기질 개선 약속 | PRX The World — "How Nike solved its sweatshop problem", https://theworld.org/stories/2016/07/30/how-nike-solved-its-sweatshop-problem |
| 2000년대 매출 | — | ✅(신규) | 2003년 사상 처음 해외 매출이 미국 매출 추월. 컨버스를 3억 500만 달러에 인수. 2005년 137.4억 달러 → 2008년 186억 달러 | Wikipedia — "Nike timeline" |
| 2017년 베이퍼플라이, 마라톤 2시간 벽 | 002 | ✅ | 2017년 카본 플레이트 탑재 베이퍼플라이 출시, 마라톤 2시간 도전 프로젝트의 핵심 장비 | Wikipedia — "Nike timeline" |
| 1982년 에어포스 1 | — | ✅(신규) | 나이키 에어 기술을 처음 탑재한 농구화 | Wikipedia — "Nike timeline" |

---

## 5. 직접판매(디티시) 전환

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| 존 도나호 2020년 1월 CEO 취임 | 002,005 | ✅ | **2020년 1월** 취임. 베인앤컴퍼니 대표, 이베이 CEO, 서비스나우 CEO 출신 | 나이키 IR — "Nike Announces Senior Leadership Changes to Unlock Future Growth Through the Consumer Direct Acceleration", https://investors.nike.com/investors/news-events-and-reports/investor-news/investor-news-details/2020/Nike-Announces-Senior-Leadership-Changes-to-Unlock-Future-Growth-Through-the-Consumer-Direct-Acceleration/default.aspx |
| "컨슈머 다이렉트 액셀러레이션" 전략 | — | ✅(신규) | **2020년 6월 발표**. 조직을 종목별이 아니라 남성·여성·키즈 소비자 축으로 재편 | 위 동일 |
| 도매 파트너 "50% 넘게 축소, 40개 핵심 거래처만" | 002 | ⚠️ 시점 오류 | "40개 전략 파트너 집중"은 **2017년 컨슈머 다이렉트 오펜스**에서 나온 방침이다. 2017년 약 3만 개 소매처 → 2019년 전략 파트너 40곳. 도나호는 이를 이어받아 가속했다 | Indigo9 Digital — "Nike's eCommerce Strategy", https://www.indigo9digital.com/blog/nikedigitalstrategy |
| 소매업체 "30% 거래 중단" | 005 | ❓ | 정확한 비율의 1차 출처 확인 불가. 확인 가능한 것은 **거래를 끊은 업체 명단**: 어반아웃피터스, 딜라즈, 자포스, 메이시스, DSW | RetailWire — "Nike says goodbye to more longtime wholesale partners", https://retailwire.com/discussion/nike-says-goodbye-to-more-longtime-wholesale-partners/ |
| 2019년 아마존 철수 | 005 | ✅ | 2019년 11월 아마존 직판 종료 | WWD — "All the Retailers Nike Left & Then Returned", https://wwd.com/footwear-news/shoe-industry-news/lists/nike-wholesale-strategy-amazon-dtc-retail-return-1237809601/ |
| 2025년 아마존 복귀 ("6년 만") | 005 | ✅ | 2025년 공식 스토어 재개설. 러닝·트레이닝·농구 핵심 라인부터 단계적 복귀 | Modern Retail — "Nike says it's making progress with its wholesale turnaround as it readies for its return to Amazon", https://www.modernretail.co/operations/nike-says-its-making-progress-with-its-wholesale-turnaround-as-it-readies-for-its-return-to-amazon/ |
| 도나호의 실책 시인 | 005 | ✅ | **2024년 4월**, "우리 자체 웹사이트와 매장에 대한 집중이 지나쳤다"고 인정하고 도매 복귀 선언 | CNBC — "Nike CEO says focus on its own website and stores went too far as it embraces wholesale retailers again", https://www.cnbc.com/2024/04/12/nike-ceo-acknowledges-it-went-too-far-in-direct-push.html |
| 2020년 7월 본사 인력 700명 해고 | 002 | ❓ | 2020년 구조조정은 사실이나 "700명"의 1차 출처 확인 불가. 대본 사용 비권장 | 검색 결과 불충분 |
| 매킨지 자문으로 종목별 조직 해체 | 002 | ❓ | 조직을 성별 축으로 재편한 것은 사실이나 매킨지 자문 여부는 1차 출처 확인 불가 | 검색 결과 불충분 |
| 마시모 지운코 전 임원 발언 인용 | 002 | ❓ | 발언 원문·출처 확인 불가. 사용 금지 | 검색 결과 불충분 |
| 판다 덩크 리셀가가 정가 아래로 폭락 | 002 | ✅ | 스톡엑스 기준 일부 판다 덩크 계열이 **정가 대비 -23% 프리미엄**(즉 정가 이하)에 거래. 덩크 로우 계열 최저 호가가 26~49달러까지 내려온 품목 존재(정가 115~125달러) | StockX 상품 페이지 — Nike Dunk Low Retro SE Suede Panda, https://stockx.com/nike-dunk-low-retro-se-suede-panda |
| "2023년 스톡엑스에서 40만 건 넘게 거래" | 002 | ❓ | 확인 불가 | 검색 결과 없음 |
| "덩크 라인이 2024년 전체 매출의 18%, 58.5억 달러 → 17.5억 달러로 70% 축소 전망" | 002 | ❓ | 출처 확인 불가. 58.5억 달러는 중화권 연 매출 수치와 우연히 겹쳐 혼동 가능성 있음. 사용 금지 | 검색 결과 없음 |

---

## 6. 경쟁사 · 점유율

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| 세계 스포츠 신발 점유율 2022년 25.9% → 2025년 22.9% | 001 | ⚠️ 출처 불일치 | **2025년 22.9%는 확인됨(3년 연속 하락, 전년비 약 3%p 하락)**. 다만 출처는 글로벌데이터가 아니라 **유로모니터 인터내셔널**이다. 2022년 25.9%라는 시작점은 별도 확인 불가 | Logos-Pres — "Nike loses market share as Adidas and rivals gain ground", https://logos-pres.md/en/news/nike-loses-market-share-and-competitors-gain-ground/ |
| "신발 점유율 3년 연속 하락, 22%까지" | 003 | ✅ | 22.9%, 3년 연속 하락 | 위 동일 |
| 아디다스 점유율 상승 | — | ✅(신규) | 아디다스 세계 운동화 점유율 **12.2%**로 상승, 나이키 이탈분의 최대 수혜 | 위 동일 |
| 호카 FY2025 매출 22.3억 달러, +23.6% | 002 | ✅ | 정확 | Deckers IR |
| 호카 최신 실적 | — | ✅(신규) | 데커스 FY2026(2026년 3월 종료) 총매출 **54.7억 달러(+9.8%)**, 호카 **25.9억 달러(+16%)** — 그룹 매출의 절반 가까이 | Deckers IR — "Deckers Brands Reports Fourth Quarter and Full Fiscal Year 2026 Financial Results", https://ir.deckers.com/news-events/press-releases/detail/656/deckers-brands-reports-fourth-quarter-and-full-fiscal-year-2026-financial-results |
| 온러닝 연매출 30억 스위스프랑 돌파, +30% | 002 | ✅ | 2025년 매출 **30.14억 스위스프랑**, 보고 +30.0% / 환율중립 +35.6%. 사상 첫 30억 프랑 돌파 | On Holding IR — "On Announces Fourth Quarter and Full Year Results… for 2025", https://press.on-running.com/on-announces-fourth-quarter-and-full-year-results-and-the-filing-of-its-annual-report-on-form-20-f-for-2025 |
| 온러닝 2026년 | — | ✅(신규) | 1분기 8.32억 프랑(+14.5%, 환율중립 +26.4%), 2분기 8.50억 프랑(+13.5%, 환율중립 +21.6%) | On Holding IR — "On Reports Results for the Second Quarter…", https://press.on-running.com/on-reports-results-for-the-second-quarter-and-six-month-period-ended-june-30-2026 |
| 아디다스 2025년 연매출 248억 유로, 사상 최대 | 002 | ✅ | **248.11억 유로**, 보고 +5% / 환율중립 +13%. 영업이익 20.56억 유로, 영업이익률 8.3%(+2.6%p) | adidas Group — "adidas reports record revenues in 2025 and launches share buyback", https://www.adidas-group.com/en/media/press-releases/adidas-reports-record-revenues-in-2025-and-launches-share-buyback |
| 아디다스 2026년 분기 환율중립 +14%, 퍼포먼스 +39% | 001 | ✅ | **2026년 2분기** 매출 67.43억 유로, 환율중립 +14%(보고 +13%). 축구·러닝 주도 퍼포먼스 부문 환율중립 **+39%** | adidas Group — "adidas grows top line 14% and achieves record sales in Q2", https://www.adidas-group.com/en/media/press-releases/adidas-grows-top-line-14percent-and-achieves-record-sales-in-q2 |
| 아디다스 2023년 30년 만의 순손실(이지 사태) | 002 | ✅ | 2022년 예(칸예 웨스트)와 이지 계약 파기, 2023년 순손실 기록. 2022년 말 비에른 굴덴 CEO 영입 후 삼바·가젤로 반등 | adidas Group / 다수 보도 |
| 2026 북중미 월드컵 유니폼 후원 "아디다스 14개국, 나이키 12개국" | 002 | ❓ | 확인 불가. 사용 비권장 | 검색 결과 없음 |
| 중국에서 안타·리닝이 점유율 잠식 | 001,002,004,005 | ✅ | **안타가 중국 스포츠웨어 점유율 21.8%로 1위**(유로모니터 2025). 안타 매출은 나이키 중화권의 1.9배, 리닝의 2.7배, 아디다스 중화권의 2.8배 | 유로모니터 2025 데이터 인용 — Briefs.co, "Nike Loses Ground in China: Revenue Falls 30%", https://www.briefs.co/news/nike-loses-ground-in-china-revenue-falls-30-amid-local-compe/ |
| 미국 러닝화 시장 구도 | — | ✅(신규) | 2025년 9월까지 12개월 기준 미국 성인 러닝화에서 **브룩스와 호카가 각각 약 23%**, 나이키 24.1%. 온·호카·뉴발란스·아디다스가 나이키의 이탈분을 나눠 가짐. 러닝 부문 시장 자체는 +8.9% 성장, 라이프스타일은 -0.9% | YipitData — "Footwear Market Trends 2026: Running Shoes Drive Growth as Brand Share Shifts", https://www.yipitdata.com/resources/blog/corporate-footwear-market-trends-running-growth |
| 경쟁사 주가 "80~100% 상승" | 005 | ❓ | 기간·기준이 불명확해 검증 불가 | 검색 결과 불충분 |

---

## 7. 엘리엇 힐 · 재건

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| 엘리엇 힐 2024년 CEO 복귀 | 002,005 | ✅ | **2024년 10월 14일 취임**(발표는 9월). 도나호 후임 | Modern Retail / 나이키 IR |
| "2024년 9월 도나호 해임" | 002 | ⚠️ | 사임·교체 발표가 2024년 9월, 힐 취임은 10월. "해임"이라는 표현은 회사 공식 발표에 없음 | 위 동일 |
| 1988년 인턴 입사, 32년 근무, 14개 직책 | 002,005 | ✅ | 1988년 인턴으로 입사해 32년간 근무 후 2020년 퇴사, 4년 만에 CEO로 복귀 | 나이키 IR |
| "나이키 매출을 390억 달러까지 끌어올린 인물" | 002 | ❓ | 개인 기여로 특정한 수치는 확인 불가 | 검색 결과 없음 |
| "스포츠 오펜스" 전략 | 005 | ✅ | 직원 **8,000명**을 종목별 수직 조직으로 재배치하는 운영 모델 | House of Heat — "Here Are Four Ways Nike, Inc. Is Innovating in the Elliott Hill Era", https://houseofheat.co/nike/nike-inc-sport-offense-innovations |
| 러닝 5분기 연속 두 자릿수 성장 | 005 | ✅ | FY2026 4분기 콜에서 힐 CEO: "러닝이 **50억 달러 사업**이 됐다. 최근 **5개 분기에 10억 달러**가 늘었고 **점유율 5%포인트**를 가져왔다" — 5개 분기 연속 두 자릿수 성장 | WWD — "Nike's Running Business Is a Definitive Bright Spot", https://wwd.com/footwear-news/shoe-industry-news/nike-running-1-billion-5-billion-business-turnaround-shoes-1239050786/ |
| "러닝화 한 켤레가 3개월 만에 1억 달러 판매" | 005 | ❓ | 개별 모델의 3개월 1억 달러 매출은 1차 출처 확인 불가. 대신 위의 "러닝 5개 분기 +10억 달러"를 쓸 것 | 검색 결과 불충분 |
| 서유럽·북미 러닝 점유율 | — | ✅(신규) | FY2026 기준 서유럽·북미 러닝화 점유율 상승폭이 **상위 5개 브랜드 중 최대** | WWD, 위 URL |
| 도매 관계 복원 | 005 | ✅ | 힐: "날카로운 스포츠 관점과 덜 할인에 의존하는 마켓플레이스로 도매 파트너의 신뢰를 되찾고 있다". DSW는 2023년 10월 복귀, 아마존 2025년 복귀 | Modern Retail / RetailWire |
| 힐 취임 일성 "우리는 스포츠에 대한 집착을 잃어버렸다" | 005 | ✅ | 취임 후 공개 발언으로 널리 인용됨 | Fox Business — "Nike CEO Elliott Hill outlines sports-focused strategy", https://www.foxbusiness.com/media/nike-ceo-elliott-hill-outlines-sports-focused-strategy-revive-iconic-sportswear-company |
| 캄노우 경기장 비유 | 002 | ❓ | 실적 발표 콜 발언으로 소개됐으나 원문 확인 불가 | 검색 결과 없음 |
| 2024년 6월 주주 소송 | 005 | ❓ | 확인 불가 | 검색 결과 불충분 |

---

## 8. 한국

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| 나이키코리아 매출 2년 연속 하락 | 002 | ✅ | 2022년 2조 109억원(+20.1%)이 정점. 이후 2조 50억원(-0.3%) → **1조 8,913억원(-5.7%)**. 감사보고서 기준 최신 회계연도(2024.6~2025.5) 영업이익 378억원(-4.2%), 당기순이익 313억원(-35.1%) | 어패럴뉴스 — "나이키, 한국 시장 2년 연속 뒷걸음질", https://www.apparelnews.co.kr/news/news_view/?idx=220355&cat=CAT100 / 이코노믹리뷰 — "잘 나가던 나이키코리아, 왜 성장세 멈췄나", https://www.econovill.com/news/articleView.html?idxno=667360 |
| "2024 회계연도 2조 50억원, 전년 대비 0.3% 감소" | 002 | ✅ | 정확 | 위 동일 |
| 한국에서 호카·온이 가파르게 성장 | 002 | ✅ | 국내 러닝 인구 약 1,000만 명, 러닝화 시장 약 1조 원. 국내 운동화 시장 4조 원 이상(2021년 2조 7,700억원). 플랫폼 기준 온러닝 거래량 +1,252%, 호카 +70% | 한국경제 — "2026 러닝화 계급도 바뀐다…노스페이스까지 참전", https://www.hankyung.com/article/202510209027g / 서울경제TV — "'러닝 전성시대'…산업도 뛰고 있다", https://www.sentv.co.kr/article/view/sentv202601220089 |
| 한국 개인투자자 해외주식 보유 상위권에 나이키 포함 | 002 | ❓ | 예탁결제원 보관금액 상위 종목(테슬라 272억 달러, 엔비디아 186억 달러, 알파벳 93억 달러 등)에 나이키는 확인되지 않음. **상위권 진입 근거 없음 — 사용 금지** | 헤럴드경제 — "빅테크에 돌아온 서학개미…美 주식 보관액 300조원 넘어섰다", https://biz.heraldcorp.com/article/10739334 |
| "9월 21일 리밸런싱 이후 자동으로 포트폴리오에서 나이키가 빠진다" | 002 | ⚠️ | **에스앤피 100 추종 상품에 한한 이야기**다. 국내 개인·연금이 주로 보유한 것은 에스앤피 500 추종 상품이고, 거기서는 나이키가 빠지지 않는다 | S&P Global 보도자료 |

---

## 9. 지수 제외의 실제 파급 (대본 최대 차별 포인트)

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| "지수에서 빠지면 추종 펀드가 기계적으로 매도해 악재" | 001,003 | ⚠️ 방향은 맞으나 규모 과장 | 아래 수치로 검증 | — |
| 에스앤피 100 추종 자금 규모 | — | ✅(신규) | 최대 공개 추종 상품인 **아이셰어즈 에스앤피 100 상장지수펀드(티커 OEF)** 순자산 **200.4억 달러**(2026년 6월 30일 기준). 별도관리계좌·기관 위탁분은 집계되지 않아 실제 추종 자금은 이보다 크지만 규모는 미상 | top1markets — "Nike's S&P 100 Removal: How to Size the Forced Selling", https://www.top1markets.com/insights/stocks/nike-index-deletion-passive-selling-estimate-2026 |
| 기계적 매도 규모 | — | ✅(신규·핵심) | 나이키의 지수 내 비중 **0.11%** × 200.4억 달러 = **약 2,200만 달러**, 주식 수로 **약 57만 3,000주**(9월 4일 종가 38.40달러 기준) | 위 동일 |
| 하루 거래량 대비 비중 | — | ✅(신규·핵심) | 나이키 하루 거래량이 1,970만 주(2026년 6월 9일) 수준이므로 **평범한 하루 거래량의 3% 미만** | 위 동일 |
| 리밸런싱 체결일의 변수 | — | ✅(신규) | 체결일인 **9월 18일은 네 마녀의 날**(선물·옵션 동시만기)로 시장 전체 거래량이 평소의 2~3배. 지수 제외에 따른 가격 충격을 사후에 분리해 보는 것 자체가 사실상 불가능 | 위 동일 |
| 결론 | — | — | **에스앤피 100 제외의 직접적 매도 압력은 사실상 무시할 수 있는 수준이다. 사건의 무게는 자금 유출이 아니라 "나이키가 더 이상 미국 초대형주로 분류되지 않는다"는 재분류 그 자체에 있다.** 실제 근거: 나이키는 현재 에스앤피 500 중 시총 **213위**이며, 다우 30종목 중 최하위(지수 비중 0.4%)로 다우 제외 가능성까지 거론된다 | Motley Fool, https://www.fool.com/investing/2026/09/12/nike-just-got-deleted-from-the-sp-100-is-its-seat/ |

---

## 10. 시청자 반발 지점 (팩트체크 블록용)

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| "품질이 나빠졌다" | 001(댓글),005(댓글) | ❓ 데이터로 입증 불가 | 나이키 제품 품질이 객관적으로 하락했음을 보여주는 공신력 있는 통계는 없다. **다만 재무제표에 잡히는 것은 정반대 신호다** — 아래 매출총이익률 항목 참조 | — |
| 매출총이익률 추이 | — | ✅(신규·핵심) | FY2022 **46.0%(정점)** → FY2023 43.5% → FY2024 44.6% → FY2025 **42.7%** → FY2026 42.9%. 나이키 스스로 밝힌 하락 원인은 **"할인 확대, 채널 믹스 변화, 재고 평가손"**이지 원가 절감이 아니다. 즉 회사가 원가를 깎아 이익을 남긴 게 아니라, **정가에 못 팔아서 이익률이 깎인 것**이다 | 나이키 IR FY2025·FY2026 실적 발표 / 나이키 10-K, https://www.sec.gov/Archives/edgar/data/0000320187/000032018726000088/nke-20260531.htm |
| 원가 대비 소비자가 구조 | — | ❓ | "100달러 신발의 제조원가 16~40달러" 류 추정치가 돌지만 신뢰할 만한 1차 출처가 없다. 대본 사용 금지 | 검색 결과 불충분(2차 블로그 출처뿐) |
| "자본력 있으니 금방 회복한다" 낙관의 근거 | — | ✅ 근거 있음 | FY2026 현금 **74.6억 달러**, 총부채 110.2억 달러. FY2026 주주환원 약 25억 달러(대부분 배당). 러닝 부문 5개 분기 연속 두 자릿수 성장, 도매 매출 +6%로 전환 | 나이키 10-K FY2026 / WWD |
| 반례 ① 코닥 | — | ✅(신규) | 1990년대 중반 미국 필름 시장 **90%**, 카메라 **85%** 점유. 1996년 매출 **162억 달러**, 시총 310억 달러 초과. → **2012년 1월 19일 챕터 11 파산**, 매출 30억 달러 미만. 1999년 정점 이후 시가총액 약 300억 달러 소멸 | The Week — "The rise and fall of Kodak: By the numbers", https://theweek.com/articles/481308/rise-fall-kodak-by-numbers / Harvard d3 — "Eastman Kodak: From Market Leader to Bankruptcy", https://d3.harvard.edu/platform-rctom/submission/eastman-kodak-from-market-leader-to-bankruptcy/ |
| 반례 ② 노키아 | — | ✅(신규) | 2007년 세계 휴대폰 점유율 약 **50%** → 2013년 스마트폰 점유율 **5% 미만**. 2013년 휴대폰 사업을 마이크로소프트에 매각 | INSEAD Knowledge — "The Strategic Decisions That Caused Nokia's Failure", https://knowledge.insead.edu/strategy/strategic-decisions-caused-nokias-failure |
| "지수에서 밀려났다가 돌아온 사례가 있다(제너럴일렉트릭·아이비엠)" | 002 | ❓ | 개별 사례의 지수 재편입 이력은 확인하지 못함. 대본 사용 비권장 | 검색 결과 불충분 |

---

## 검증 요약

| 구분 | 건수 |
|------|------|
| ✅ 검증됨 | 62 |
| ❌ 불일치 | 9 |
| ⚠️ 부분 불일치·과장 | 9 |
| ❓ 미확인 | 19 |

### 주요 불일치 항목 (대본에서 반드시 교정할 것)

1. **"퇴출"이 아니라 "제외"다.** 레퍼런스 005는 이 단어 하나로 최다 공감 댓글에 정정 지적을 받았다. 훅에서 쓰더라도 본론 첫머리에서 화자가 먼저 자백·정정해야 한다.
2. **발표일은 9월 6일이 아니라 9월 4일**, 발효일은 9월 20일이 아니라 **9월 21일**(체결은 18일 종가).
3. **증발한 시가총액은 2,200억 달러(300조원)가 아니라 약 2,070억 달러(약 277조원)다.**
4. **하락률은 78.6%.** "80% 폭락"은 과장.
5. **중국은 7분기가 아니라 8분기 연속 감소.**
6. **2021년 "순이익 +291%"는 성립하지 않는 수치.** 전년 동기가 순손실이라 계산 자체가 불가능하다. 연간 기준 +125%로 바꿔 쓸 것.
7. **창업은 1963년이 아니라 1964년 1월 25일.**
8. **"도매 파트너 40곳으로 축소"는 도나호가 아니라 2017년 컨슈머 다이렉트 오펜스에서 시작된 방침.** 도나호는 가속한 쪽이다.
9. **함께 빠진 "허니웰"은 2026년 6월 분사 상장한 허니웰 에어로스페이스**로, 6월에 편입됐다가 3개월 만에 제외된 특수 사례다. "전통 제조업의 퇴조"로 묶으면 사실과 다르다.
10. **한국 개인투자자 해외주식 보유 상위권에 나이키가 있다는 주장은 근거 없음.**
11. **에스앤피 100 제외의 기계적 매도 압력은 약 2,200만 달러 · 57만 주로, 하루 거래량의 3% 미만이다.** "돈줄이 끊긴다", "기계적 매도로 악재"라는 레퍼런스들의 서술은 방향은 맞지만 규모를 크게 과장했다.
