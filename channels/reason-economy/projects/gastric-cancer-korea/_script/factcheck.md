# 팩트체크

> 프로젝트: gastric-cancer-korea (위암 — 미국은 33.1%, 한국은 68.9%)
> 검증일: 2026-09-23
> 대상: `verified-data.md` 「확인 실패 / 보강 필요」 6건 + 추가 리서치 3건

> ⚠️ **1단계(레퍼런스 transcript 데이터 추출)는 생략했다.** `_refs/001`(네팔 빙하·「한국에서 답을 찾았다」)과
> `_refs/002`(유럽 K웨이브)는 **위암과 무관한 구조 패턴 학습용** 수집물이라, 그 안의 수치는 이 대본에 쓰이지 않는다.
> 001 analysis의 「제3자 권위를 다리로 쓰는 구조」는 **검색 방향 가이드**로만 사용했다(→ 추가 리서치 ③).
>
> 1차 리서치(`verified-data.md` 1~11번)의 검증 결과는 **그대로 유효**하며 이 문서는 **갭 해소분만** 기록한다.

---

## A. 갭 해소 — 우선순위 항목

### ⑥ 한국의 병기별 위암 생존율 — ✅ 해소

| 데이터 | 검증 | 실제값 | 출처 |
|---|---|---|---|
| 한국 위암 **요약병기별 5년 상대생존율** (2019~2023 진단자) | ✅ | **국한 97.6% / 국소 62.2% / 원격 7.5% / 모름 47.1%** | 국가암정보센터 — 「주요 암종 요약병기별 5년 상대생존율: 남녀전체, 2019-2023」, https://cancer.go.kr/lay1/S1T648C652/contents.do |
| 병기별 **환자 분율** | ✅ | 국한 **65.3%** / 국소 18.8% / 원격 10.7% / 모름 5.1% | 〃 |
| 교차검증 — 별도 논문의 한국 병기별 값 | ✅ | 국한 **97.0%** / 국소 62.1% / 원격 6.4% (거의 동일) | *Epidemiology of Gastric Cancer in Korea (1999–2022)*, PMC12802026, https://pmc.ncbi.nlm.nih.gov/articles/PMC12802026/ |

> **지표가 미국 SEER과 같은 줄에 선다.** 양쪽 모두 **요약병기(localized/regional/distant) 기준 5년 상대생존율**이다.
> 단, **관측기간이 다르다** — 미국 SEER 2015~2021 vs 한국 2019~2023. 대본에서 **두 시점을 반드시 함께 말한다.**
>
> ⚠️ **주의 — 이 숫자는 기획의 논리를 한 번 흔든다.**
> 「같은 병인데 한국은 일찍 찾는다. 그 차이가 전부다」가 1차 리서치의 4막 논리였는데,
> **국한 병기끼리 비교해도 97.6% vs 75%로 벌어진다.** 즉 발견 시점만의 차이가 아니다.
> 다만 두 나라의 「국한」 안에 담긴 병변이 다를 수 있다(한국은 ESD로 치료되는 점막암 비중이 크다 — stage migration).
> → **대본 처방**: 「발견 시점의 차이가 전부다」로 단정하지 말고, **「일찍 찾고, 일찍 찾은 것을 잘 떼어낸다」**
> 두 축으로 쓴다. 국한 97.6% vs 75% 비교는 **관측기간과 병기 구성 차이를 한 문장으로 밝힌 뒤** 사용한다.

---

### ⑦ 2026년 위암 검진 기준 변경 — ✅ 해소 (2018년 변경과 **별개 사안**)

| 데이터 | 검증 | 실제값 | 출처 |
|---|---|---|---|
| 「위장조영술 대신 위내시경, 10년 만에 기준 변경」(2026-06 보도) | ✅ | **2026년 6월 24일**, 국립암센터가 대한가정의학회·대한내과학회·대한간암학회 등과 **GRADE 방법론**을 적용해 **국가 위암·간암 검진 권고안**을 개정 | 아시아경제 — 「위암 국가검진 시 '위내시경' 우선…10년 만에 권고안 개정」(2026-06-24), https://view.asiae.co.kr/article/2026062416374198714 |
| 직전 권고안 시점 | ✅ | **2015년판.** 「이번 개정은 2015년 이후 10년 만이다」 | 〃 |
| 변경 내용 | ✅ | 기존: 위내시경 우선 권고 + 위장조영 **선택적 고려** → 신규: **2년 간격 위내시경 단독 1차 검진법** | 〃 |
| 변경 사유 | ✅ | 「위내시경이 위장조영 검사보다 위암 사망률 감소 효과와 진단 정확도 측면에서 우수한 것으로 판단」 | 〃 |
| 검진 연령 | ✅ | **40~74세 유지.** 75세 이상은 의료진 상담 후 개별 결정 | 〃 |

> ✅ **2018년 변경과 별개다.** 두 사안을 구분해 쓴다:
> - **2018년** = 국가암검진**사업**(집행)에서 위내시경을 「기본 검사」로 전환
> - **2026년 6월** = 국립암센터·학회의 **검진 권고안**(학술 지침) 개정, **2015년판 이후 10년 만**, 위장조영술을 1차 검진법에서 **제외**
>
> **「10년 만」은 2015년 권고안 기준이지 2018년 사업 변경 기준이 아니다.** 이 구분을 놓치면 대본이 틀린다.

---

### ⑧ 「3년 이내 간격 검진 사망률 29%↓」 — ✅ 해소 (2017년 연구와 **별개 논문**)

| 데이터 | 검증 | 실제값 | 출처 |
|---|---|---|---|
| 원 논문 저널 | ✅ | ***Gastrointestinal Endoscopy*** (미국소화기내시경학회지) | 메디칼업저버 — 「위암 내시경 검진 '3년 이내' 간격 시 사망 위험 감소」, https://www.monews.co.kr/news/articleView.html?idxno=410478 |
| 연구진 | ✅ | **최현호** 교수(가톨릭의대 의정부성모병원 소화기내과) · **성수윤** 교수(서울성모병원 방사선종양학과) | 〃 |
| 코호트 규모·자료원 | ✅ | 위암 환자 **26,199명**, **국민건강보험공단(NHIS)** 자료 | 〃 |
| 핵심 수치 | ✅ | 3년 이내 검진군은 3년 초과 검진군 대비 사망 위험 **약 29% 낮음 (HR 0.71)** | 〃 |
| 2년 vs 3년 | ✅ | **두 간격 사이 사망률 차이 관찰되지 않음** | 〃 |
| 보도 시점 | ✅ | 2026년 4월 2일 | 금강일보·메디칼업저버·라포르시안·헬스경향 동일 보도 |
| 2017 Gastroenterology(47%) 연구와의 관계 | ✅ | **별개 논문이다.** 저자·저널·자료원·비교축이 모두 다르다 (2017: 검진군 vs 비검진군 / 2026: 검진 **간격**별 비교) | 양측 원 보도 대조 |

> ⚠️ **두 연구를 섞지 말 것.**
> - **47%** = 검진 방법(내시경 vs 조영술 vs 비검진) 비교, *Gastroenterology*(2017), 1,658만 명
> - **29%** = 검진 **간격**(3년 이내 vs 3년 초과) 비교, *Gastrointestinal Endoscopy*(2026), 위암 환자 26,199명
>
> 🎯 **대본 활용점**: 29% 연구는 「2년마다 오라는 그 문자 한 통이 왜 2년인가」를 뒷받침한다.
> **2년과 3년 사이에 차이가 없었다**는 결과까지 말해야 정직하다 — 이게 「인과를 한 단계 낮춰 쓴다」에 맞는다.

---

### ③ 해외 의료진 ESD·위암수술 연수 — ❓ **위암 특정 제3자 1차 출처 없음 → 「없음」으로 확정**

| 데이터 | 검증 | 실제값 | 출처 |
|---|---|---|---|
| 「해외 의료진이 위암 수술을 배우러 한국에 온다」 **제3자 1차 출처** | ❓ **미확인** | **검색 결과 없음.** 해외 기관·학회·언론이 「한국에 위암 수술을 배우러 간다」고 기록한 1차 자료를 찾지 못함 | — |
| 세브란스병원 자체 영문 소개 | ⚠️ **자기 진술** | "dozens of doctors visit our hospital every year to learn the surgical techniques" / 위암 로봇수술 연 140건 이상 | 세브란스병원 위장관외과 영문 페이지, https://sev.severance.healthcare/sev-en/department/department/gastrointestinal-surgery.do |
| 세브란스 국제 연수 프로그램 (SIF) | ⚠️ **일반 프로그램** | Severance International Fellowship — 외국인 의사 대상 임상 참관·연구 프로그램. **위암 특정이 아니다** | 연세의료원 제중원보건개발원, https://yigh.yuhs.ac/yigh/international/physician.do |
| 대한소화기내시경학회 국제학술대회(IDEN) | ⚠️ **간접** | KSGE가 2011년부터 IDEN 개최, **라이브 내시경 시연** 포함, 해외 초청 연자 다수. 다만 「배우러 온다」가 아니라 **학술 교류**다 | World Endoscopy Organization — IDEN 2026, https://www.worldendo.org/events/international-digetsive-endoscopy-network-iden-2026 |

> ⛔ **확정 판정: 대본에서 「해외가 배우러 온다」 문단을 뺀다.**
> 채널 규칙 「자부심은 화자가 직접 주장하지 않는다 — 제3자의 입을 빌린다」에 따르면
> **병원 자체 홈페이지의 자기 소개는 제3자 근거가 아니다.** 이걸 인용하면 자화자찬이 된다.
> `verified-data.md` 9번(몽골 연수 등 일반 의료연수)도 **위암과 무관**하므로 같이 뺀다.
> → **대체재는 아래 추가 리서치 ③(제3자 권위 인용거리)로 확보했다.** 그쪽이 훨씬 강하다.

---

### ④ 수검률 64.6% vs 77.4% — ✅ 해소 (**조사 주체·기준·연도가 전부 다르다**)

| 항목 | 64.6% | 77.4% |
|---|---|---|
| **조사 주체** | **국민건강보험공단** | **국립암센터** |
| **자료명** | 『2023 건강검진통계연보』 (공단 DW시스템) | 『암검진 수검행태조사』 (2004년부터 매년, 구조화 설문) |
| **연도** | **2023년** | **2024년** |
| **정의** | 국가암검진사업 대상자 중 **국가암검진사업을 통해** 검진받은 사람의 비율 | 40~74세 중 **최근 2년 이내 위내시경 또는 위장조영술**을 받은 분율 (**국가검진 + 민간검진 포함**, 「권고안 이행 수검률」) |
| **같이 발표된 값** | 전체 암검진 59.8% · 간암 76.1% · 유방암 65.1% | 전체 70.2% · 대장암 74.4% · 유방암 70.6% · 자궁경부암 62.0% |
| 검증 | ✅ | ✅ |
| 출처 | 국민건강보험공단 「2023 건강검진통계연보」(2024-12-31 배포) / 보도: 메디컬월드뉴스·팜뉴스 | 국립암센터 암검진 수검행태조사 / 암모니터링포털, https://www.cancerdata.re.kr/surveillance/data?menuId=36 |

> **참고 — 국가암검진 위암 수검률 추이** (국민건강보험공단, e-나라지표): 2021년 62.6% → 2022년 62.3% → 2023년 **64.6%**
> (https://www.index.go.kr/unity/potal/main/EachDtlPageDetail.do?idx_cd=1440)
>
> 🎯 **대본 처방: 77.4%(2024, 암검진 수검행태조사)를 쓴다.**
> ⑴ 더 최신이고 ⑵ **시청자가 실제로 받는 검진 전체**(회사검진·개인검진 포함)를 담아 체감과 맞으며
> ⑶ 「암종 중 1위」라는 서사가 성립한다. 단, **출처와 기준을 한 번 밝힌다** — 「국립암센터가 2024년에 조사한,
> 최근 2년 안에 위 검사를 받은 사람의 비율」. **두 숫자를 같은 대본에 함께 쓰지 않는다.**

---

### ⑨ 일본·중국 최신 시점 생존율 — ⚠️ **일본은 갱신 가능 / 중국은 CONCORD-3 유지**

**일본 — CONCORD-3 이후 자료 확보 ✅**

| 데이터 | 검증 | 실제값 | 출처 |
|---|---|---|---|
| 일본 위암 **5년 순생존율**, **2016년 진단자** | ✅ | **64.0%** (전체) | 후생노동성 「2016년 전국암등록 생존율 보고」(2026-01-14 발표), https://www.mhlw.go.jp/content/10901000/001630334.pdf |
| **국제비교용 연령조정** 5년 순생존율 | ✅ | **67.3%** | 〃 |
| 진전도별 | ✅ | 限局(국한) **90.8%** / 遠隔(원격) **6.0%** | 〃 |
| 교차검증 | ✅ | 동일 수치 (위 64.0%, 대장 67.8%, 폐 37.7%, 여성유방 88.0%, 전립선 92.1%) | 케어넷 — 「全国がん登録での初の5年生存率発表」, https://www.carenet.com/news/general/carenet/62139 |

> ⚠️ **지표는 순생존율로 CONCORD-3과 같다.** 그러나 **관측 시점이 다르다**(CONCORD-3 2000~2014 진단 vs 일본 2016년 진단).
> **한국의 동일 시점·동일 지표 값을 못 구했으므로 68.9%와 67.3%를 같은 줄에 놓으면 안 된다.**
> → **확정: 국가 간 대비표는 CONCORD-3(2000~2014) 하나로만 세우고, 시점을 명시한다.**
> 일본의 2016년 값은 **「일본도 계속 올라오고 있다」는 보조 서술**로만 쓴다(비교표에 넣지 않는다).

**중국 — CONCORD-3 이후 인구기반 전국 자료 ❓ 미확인**

| 데이터 | 검증 | 실제값 | 출처 |
|---|---|---|---|
| 중국 전국 인구기반 위암 5년 생존율(CONCORD-3 이후) | ❓ **미확인** | **전국 단위 인구기반 값 없음.** 병원기반·지역기반 자료만 존재 | — |
| (참고) 중국 국가암센터 **병원기반** 수술환자 병기별 5년 생존율 (2011~2018) | ⚠️ 참고용 | pTNM IA 94.9% / IB 91.8% / IIA 86.5% / IIB 76.1% / IIIA 61.1% / IIIB 44.2% / IIIC 29.7% / IV 8.1% | *Survival of patients with gastric cancer surgically treated at the National Cancer Center of China from 2011 to 2018*, PMC11256526 |
| (참고) 샤먼시 **지역 인구기반** 5년 생존율 (2016~2020) | ⚠️ 참고용 | 연령보정 **30.03%** | *Trends in incidence, mortality and survival of gastric cancer in Xiamen, China from 2011 to 2020*, PubMed 39615306 |

> ⛔ **중국 병원기반 수치를 CONCORD-3의 35.9%와 나란히 놓지 않는다.**
> 「수술받은 환자만」 집계한 값이라 인구기반 값보다 훨씬 높게 나온다. **이 장르 최대의 사고 유형이다.**
> → **확정: 중국은 CONCORD-3(35.9%, 2000~2014 진단, 순생존율)을 시점 명시하고 쓴다.**

---

## B. 추가 리서치 검증

### 1. KLASS-02 구체적 결과 수치 — ✅ 전부 확보

| 데이터 | 검증 | 실제값 | 출처 |
|---|---|---|---|
| **3년 무재발생존율** (1차 평가변수) | ✅ | **복강경 80.3%** (95% CI 76.0–85.0) vs **개복 81.3%** (95% CI 77.0–85.0), log-rank **P=.726** | *J Clin Oncol* (2020), KLASS-02-RCT, https://ascopubs.org/doi/10.1200/JCO.20.01210 |
| 비열등성 검정 | ✅ | HR **1.035** (95% CI 0.762–1.406), **비열등성 마진 HR 상한 1.43**, P for noninferiority **=.039** | 〃 |
| **5년 전체생존율** | ✅ | **복강경 88.9%** (95% CI 86.0–91.8) vs **개복 88.7%** (95% CI 85.8–91.6) — 차이 없음 | *JAMA Surgery* (2022), https://jamanetwork.com/journals/jamasurgery/fullarticle/2794452 |
| **5년 무재발생존율** | ✅ | **복강경 79.5%** (75.9–83.2) vs **개복 81.1%** (77.7–84.8) — 차이 없음 | 〃 |
| **후기 합병증** (21일 이후) | ✅ | **복강경 6.5%**(32/492) vs **개복 11.0%**(53/482), **P=.01** — 유의하게 낮음 | 〃 |
| 장폐색 | ✅ | 복강경 2.6%(13/492) vs 개복 5.0%(24/482) | 〃 |
| **단기(전체) 합병증** | ✅ | **복강경 16.6%** vs **개복 24.1%** | KLASS-02-RCT 단기 결과, *Ann Surg* (2019) |
| 환자 수 | ✅ | 무작위배정 **1,050명**, 5년 분석 대상(R0 절제) **974명** (복강경 492 / 개복 482) | *JAMA Surgery* (2022) |
| 참여 기관 | ✅ | **14개 기관** | 〃 |
| 5년 결과 제1저자 | ✅ | **Sang-Yong Son(손상용)** | 〃 |
| KLASS-02 + CLASS-01 개별환자데이터 메타분석 | ✅ | 5년 OS **82.7% vs 83.3%**(P=0.706), 5년 RFS **76.9% vs 77.9%**(P=0.666), 중앙추적 70개월. ⚠️ **pT4에서는 복강경이 RFS 열세** | *Chinese Journal of Cancer Research* (2025-06), PMC12240251 |

> 🎯 **대본에 쓸 한 줄**: 「5년을 따라가 보니 생존율은 같았고, 합병증은 개복 11.0%, 복강경 6.5%였습니다.」
> — **숫자가 스스로 말한다. 형용사를 붙이지 않는다.**
> ⚠️ **pT4 하위군에서 복강경이 열세**라는 메타분석 결과는 **「인과를 한 단계 낮춰 쓴다」의 근거**다.
> 「모든 진행성 위암에 복강경이 낫다」로 쓰면 틀린다.

---

### 2. KLASS-02의 가이드라인 등재 — ⚠️ **「세계 표준」은 과장. 톤을 낮춰야 한다**

| 가이드라인 | 검증 | 실제 문구 | 출처 |
|---|---|---|---|
| **일본 위암치료 가이드라인 2021 (6판)** — cStage I | ✅ | "Laparoscopic distal gastrectomy for cStage I gastric cancer is **strongly recommended**" (강한 권고, **근거수준 A**) | *Gastric Cancer* (2023), PMC9813208, https://pmc.ncbi.nlm.nih.gov/articles/PMC9813208/ |
| **일본 가이드라인 2021 (6판)** — **cStage II/III (진행성)** | ❌ **「등재됐다」는 표현이 틀린다** | "**Clear recommendations cannot be provided** for laparoscopic surgery for cStage II/III gastric cancer" (**근거수준 C**) | 〃 |
| 일본 가이드라인의 KLASS-02 언급 | ✅ | "Large-scale, randomized, clinical trials confirming safety and long-term survival of laparoscopic distal gastrectomy have been conducted in Japan, Korea, and China (**JLSSG0901, KLASS-02, CLASS-01**)." + CLASS-01·KLASS-02에서 전체생존 비열등성 확인 | 〃 |
| **한국 위암 진료 권고안 2024 (5판)** | ✅ | 「Laparoscopic distal gastrectomy (LDG) as well as open distal gastrectomy (ODG) **can be recommended for locally advanced gastric cancers** for comparable survival outcomes」 — KLASS-02·CLASS-01·JLSSG0901 메타분석이 근거. GRADE 방법론 적용 | *Korean Practice Guidelines for Gastric Cancer 2024*, PubMed 39822170 / https://jgc-online.org/DOIx.php?id=10.5230%2Fjgc.2025.25.e11 |
| **NCCN 위암 가이드라인** | ⚠️ **2차 출처만 확인** | 「2021년 NCCN 가이드라인이 국소진행성 위암에 복강경 수술을 권고했다」 — **리뷰 논문의 서술**이고 NCCN 원문을 직접 확인하지 못했다 | 2차 출처(리뷰 논문) |

> ⛔ **「KLASS-02가 세계 표준이 됐다」는 문장을 쓰지 않는다.**
> 확인된 사실은 여기까지다:
> - **조기위암(cStage I)** 복강경 수술은 일본 가이드라인에서 **강한 권고·근거수준 A** — 여기엔 KLASS-01/03의 지분이 있다
> - **진행성 위암(cStage II/III)**은 일본 가이드라인 2021년판 기준 **「명확한 권고 불가」(근거수준 C)**
> - **한국 권고안 2024**는 진행성 위암에도 **복강경을 권고**한다
> - 일본 가이드라인은 KLASS-02를 **근거 문헌으로 인용**한다
>
> 🎯 **대본 처방 — 이 표현으로 쓴다**:
> 「한국에서 나온 이 연구는 지금 **일본 위암치료 가이드라인의 근거 문헌 목록에** 올라가 있습니다.
> 그리고 **한국 진료 권고안은 2024년에 진행성 위암에도 복강경 수술을 권고**했어요.」
> — **「인용됐다」와 「권고됐다」는 다르다.** 이 구분을 지키면 반박당하지 않는다.

---

### 3. 제3자 권위 인용거리 — ✅ 4건 확보 (원문 그대로)

| # | 인용문(원문) | 화자 | 출처 | 검증 |
|---|---|---|---|---|
| **A** ⭐ | "Japan and South Korea are **ranked second and third, respectively, in terms of incidence but 38th and 64th, respectively, in terms of mortality**. … These two countries are unique in that they have **organized nationwide GC screening programs**." | **일본 연구진** (Kitasato University 등 4개 기관) | *DEN Open* (2025), 「Current Status of Gastric Cancer Screening and Future Perspectives」, PMC12106035 | ✅ |
| **B** ⭐ | "5-year net survival rate for GC is generally **<35%** (including **wealthy countries in North America and Western Europe**), but it is **>60% in Japan and South Korea**." | 〃 | 〃 | ✅ |
| **C** | "**Korea has an effective gastric cancer screening system.**" / "the proportion of gastric cancers diagnosed in earlier stages … has increased after implementation of the National Cancer Screening Program" / "5-year survival rates for gastric cancer has increased **owing to the NCSP-GC**." | **일본 연구진** (Hidekazu Suzuki, Tokai University School of Medicine) | *Korean J Helicobacter Up Gastrointest Res* (2024), 「Stomach Cancer Screening in Japan and Korea」, PMC11967706 | ✅ |
| **D** | "The investigators previously reported that laparoscopic distal gastrectomy was **noninferior** regarding the primary end point of 3-year recurrence-free survival, and now show that 5-year overall survival is also similar, but that **long-term morbidity is significantly lower in the laparoscopic group**." | **미국 연구진** — George Z. Li, Shoji Shimada, **Vivian E. Strong** (Memorial Sloan Kettering Cancer Center, New York) | *JAMA Surgery* (2022) 초청 논평 「Bigger May Not Be Better—Implications of Long-term Results From KLASS-02」, https://jamanetwork.com/journals/jamasurgery/article-abstract/2794458 | ✅ |
| **E** (보조) | 미국 AGA 임상진료 업데이트가 **미국 내 위암 검진 연령 기준을 정하면서 한국(40세 이상)과 일본(40~50세)의 기준을 참조**했다 | **미국소화기학회(AGA)** | *Gastroenterology* (2025), AGA Clinical Practice Update (Shah, Wang, Piazuelo, Gawron 등) | ⚠️ **2차 출처 경유** — 원문 직접 확인 실패(403) |
| **F** (보조) | "established screening programs in Japan and South Korea" / "as observed following the introduction of **Korea's national screening program**" | **미국·네덜란드 연구진** (Columbia University, Harvard Medical School, **Memorial Sloan Kettering**) | *Gastroenterology* (2025), 「Recent US Gastric Cancer Prevention Recommendations」, PMC12550653 | ✅ |

> 🎯 **A가 이 대본의 최고 무기다.** 「발생률 3위, 사망률 64위」 — **일본 연구자가 쓴 문장**이고,
> 화자가 한 마디도 보태지 않아도 된다. 레퍼런스 001의 「헤드라인을 통째로 인용한다」를 그대로 적용할 자리다.
>
> ⚠️ **A의 「38위/64위」는 국가 간 사망률 순위**다. `verified-data.md` 11번의 ⛔ 규칙
> (「한국 위암 사망률이 미국보다 낮다」 금지)과 충돌하지 않도록, **한국·일본의 발생률과 사망률 순위 격차**를
> 말하는 데까지만 쓰고 **미국과 직접 맞붙이지 않는다.**
>
> ⚠️ **D는 미국 최고 암센터(MSKCC)가 한국 연구를 평가한 문장**이다. KLASS 블록의 착지로 쓴다.
> 화자가 "세계가 인정했다"고 말할 필요가 없다 — **인용하고 넘어가면 된다.**

---

## 검증 요약

| 구분 | 건수 |
|------|------|
| ✅ 검증됨 | 33 |
| ❌ 불일치 | 1 |
| ❓ 미확인 | 3 |

### ❌ 불일치 항목

1. **「KLASS-02가 국내외 위암 수술 가이드라인에 등재됐다」** (`verified-data.md` 7번)
   → **일본 위암치료 가이드라인 2021(6판)은 cStage II/III 복강경 수술에 대해 「명확한 권고를 제시할 수 없다」(근거수준 C)**고 적었다.
   KLASS-02는 **근거 문헌으로 인용**됐을 뿐이다. 한국 권고안 2024는 권고했다.
   **「등재」·「세계 표준」 표현을 삭제하고 「인용」과 「한국 권고안의 권고」로 교체한다.**

### ❓ 미확인 항목

1. **해외 의료진의 ESD·위암수술 연수 (③)** — 제3자 1차 출처 없음. **「없음」으로 확정.** 해당 문단을 삭제한다
2. **중국의 CONCORD-3 이후 전국 인구기반 생존율 (⑨)** — 검색 결과 없음. **CONCORD-3 35.9%를 시점 명시하고 사용**
3. **NCCN 위암 가이드라인의 복강경 권고 원문** — 2차 출처(리뷰 논문)로만 확인. **대본에서 NCCN을 언급하지 않는다**
