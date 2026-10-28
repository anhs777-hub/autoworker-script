# 팩트체크

> 프로젝트: lmr-two-american-batteries
> 검증일: 2026-10-29
> 대상: 레퍼런스 001 (경제를 알리자 「중국산 배터리랑 가격은 똑같은데 주행거리는 33% 더 나간다?…」, 2026-10-25)
> 참고: temp-analysis90/expansion-topics.md 「LMR 비튼 각도 검토」 사실 재검증 포함

## 1. 원가·가격 구조

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| 양극재가 배터리 원가의 40% 이상 | 001 | ✅ | 셀 원가의 40~60%가 양극재 원료(화학 조성에 따라) — BNEF 인용 | S&P Global(2024-03) spglobal.com/market-intelligence/en/news-insights/articles/2024/3/lower-lithium-prices-support-adoption-of-lithium-rich-ev-batteries-80627369 · IDTechEx(2025) 양극재 원가 NMC811 <40$/kWh, LFP <35$/kWh powersystemsdesign.com/articles/battery-cell-costs-drop-to-almost-us100kwh-despite-lithium-price-volatility-finds-idtechex/8/23187 |
| LFP가 기존 배터리보다 20~30% 쌈 | 001 | ✅ (과거 기준) / 최신은 더 벌어짐 | BNEF 2023: LFP 셀이 NMC보다 평균 32% 쌈 · IEA GEVO 2026: 2025년 LFP 팩이 NMC보다 kWh당 40% 이상 쌈 | BNEF 2023 서베이(thedriven.io/2023/11/28/…) · IEA Global EV Outlook 2026 iea.org/reports/global-ev-outlook-2026/electric-vehicle-batteries |
| 코발트 값이 망간의 수십 배 | 001 | ✅ | 2026년 상반기 코발트 약 5.6만 달러/t vs 전해망간 약 2,200~2,350달러/t → 약 24배 | Trading Economics(코발트 2026-03) tradingeconomics.com/commodity/cobalt · SMM 전해망간(2026-01·05) news.metal.com |
| 망간 값 = 코발트의 1/20, 니켈의 1/10 | 001 | ✅ (근사) | 코발트 대비 약 1/24, 니켈(약 1.7만 달러/t) 대비 약 1/7 — 시점에 따라 변동 | 위 동일 + Petromindo 2026-04 광물 기준가 petromindo.com |
| 코발트 콩고 아동노동 문제 | 001 | ✅ (상식 수준, 대본에서 1줄) | 콩고민주공화국 코발트 채굴 아동노동은 국제 보고서 다수 | (일반 상식 — 세부 수치 미사용) |

## 2. 중국·LFP 시장

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| 저가 전기차 시장 중국 90% 넘게 장악 | 001 | ❓ | 「저가 전기차 시장」 점유율 통계는 찾지 못함. 대신 LFP 양극재 생산은 「거의 전부 중국」(IEA), 99%(Benchmark) | IEA GEVO 2026 · Benchmark Minerals(2025-01) source.benchmarkminerals.com |
| 세계 LFP 배터리 시장 중국 90% 이상 | 001 | ✅ | LFP 양극재·전구체 생산 거의 전부 중국(IEA), LFP 양극재 99%(Benchmark), 유럽·미국 판매 전기차 LFP 배터리 거의 전부 중국산 — IEA는 「사실상 독점」 | IEA GEVO 2026 / 2025 · Benchmark · batterytechonline.com/ev-batteries/iea-report-lfp-dominates-as-ev-battery-prices-fall |
| LFP 그램당 약 170mAh | 001 | ✅ | LiFePO4 이론 용량 약 170mAh/g (교과서 값) | Padhi·Goodenough 1997 JES 논문 계열 문헌 · IEA 문헌 공통 |
| LFP 배터리 리튬 함량 2%도 안 됨 | 001 | ❓ | 기준 불명. 양극재 기준 LiFePO4 리튬은 약 4.4wt%(폐 LFP 양극 실측 4.26~4.43%) → 레퍼 수치와 상충 | PMC12196130 (LFP 리튬 회수 논문) ncbi.nlm.nih.gov/pmc/articles/PMC12196130/ · RSC 보조자료 |
| LMR 리튬 함량 8%, LFP의 4배 이상 | 001 | ❓ | 1차 출처 없음. 대표 조성(Li1.2Mn0.54Ni0.13Co0.13O2) 계산 시 양극재 리튬 약 9.8wt% → LFP(4.4%)의 약 2.2배. 「4배」는 근거 없음 | 화학식 계산(검색 결과 없음) |
| LFP 재활용은 돈이 안 됨 | 001 | ✅ | 「LFP에서 유일한 가치 원소는 리튬」, 습식 재활용은 대체로 비경제적이라는 학계 평가 | PMC12196130 · RSC Mechanochemistry 2024 |
| 미국 정부, 중국산 부품·광물 쓰면 보조금 배제 | 001 | ✅ (서술 수준) | IRA 「해외 우려 기업」 규정 — 2025년 세액공제 축소 등 변동 있음 → 대본은 시점 명시 필요 | (일반 정책 사실, 본편 미사용 권장) |

## 3. 망간·LMR 기술

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| 망간 세계 매장량 15억 톤 | 001 | ❌ | USGS 2026: 세계 매장량 약 18억 톤(망간 함량 기준, 2025) · 남아공 5.5억 톤·호주 5.8억 톤 · 세계 자원의 약 70%가 남아공 | USGS Mineral Commodity Summaries 2026 — Manganese pubs.usgs.gov/periodicals/mcs2026/mcs2026-manganese.pdf |
| LMR 망간 비율 60~70% | 001 | ✅ | GM: LMR은 니켈 약 35%·망간 약 65%·코발트 거의 0 | Argus(2025-05) argusmedia.com/…/2688027-gm-lges-to-commercialize-lmr-batteries · GM 발표 |
| LMR 그램당 250~350mAh (LG 공개) | 001 | ❓ | LG 공개 출처 미확인. LG·서울대 2026 논문은 양극 활물질 기준 비에너지 663Wh/kg 제시 | TokenPost(2026-09) tokenpost.kr/news/tech/403568 |
| 리튬 1.2~1.6배 우겨 넣음 | 001 | ❓ | 대표 조성 Li1.2(금속 대비 리튬 과잉)는 문헌 공통, 1.6은 출처 없음 | DOE·아르곤 xLi2MnO3·(1-x)LiMO2 문헌 energy.gov/eere/vehicles/articles/solid-state-nmr-studies-and-local-structure-voltage-fade-materials |
| 1990년대 초중반 처음 학계에 등장, 아르곤 연구소 등 연구 | 001 | ✅ (보정) | 아르곤 연구원 마이클 새커리가 첫 특허를 2000년 출원, 특허군 2004~2008년 등록(US 6,677,082 등) | Greentech Media 「Argonne's Battery Tech: A Government Licensing Success Story」 · chargedevs.com (BASF·아르곤 vs 유미코어 소송) |
| 30년 동안 아무도 상용화 못 함 | 001 | ✅ | 2026-10 현재 LMR 전기차 배터리 양산 사례 없음. 얼티엄셀즈가 「상업 생산하는 첫 제조사」가 될 것이라 발표(2026-09-29) | CBT News(2026-09-30) cbtnews.com/gm-and-lg-expand-lmr-battery-production-500/ · 헤럴드경제(2026-09-30) biz.heraldcorp.com/article/10888409 |
| 충전 반복 시 전압 강하(voltage fade) | 001 | ✅ | 전압 강하가 수명 동안 에너지 밀도를 깎는다 — 미 에너지부·아르곤 연구 | energy.gov (voltage fade 연구) · OSTI 1237912 |
| 산소가 반응에 참여해 빠져나가며 구조 붕괴 | 001 | ✅ (단순화) | 산소 손실 → 저전압 산화환원쌍 활성화(아르곤·브룩헤이븐 2019). 단 산소 방출이 원인이냐 증상이냐는 학계 이견 | energy.gov · ECS 초록 |
| 첫 충전 때 리튬 일부가 돌아오지 않음 | 001 | ✅ | LMR의 첫 사이클 비가역 용량 손실은 공지 사실 (LG도 실리콘 음극 조합으로 보완했다는 맥락) | LG에너지솔루션 뉴스룸(2026-06-21) news.lgensol.com/company-news/supplementary-stories/5025/ |

## 4. LG에너지솔루션

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| LMR 첫 특허 2010년 | 001 | ✅ | GM·LG 공동 발표(2025-05-13): 「LMR 화학 첫 특허는 2010년」 · 헤럴드경제(2026-09-30) 동일 | GM 투자자 발표 investor.gm.com/news-releases/news-release-details/gm-and-lg-energy-solution-pioneer-lmr-battery-cell-technology/ · 헤럴드경제 biz.heraldcorp.com/article/10888409 |
| 연구 시작 2009년 (17년) | 001 | ❓ | 2009년 착수를 밝힌 공개 출처 찾지 못함 | 검색 결과 없음 |
| LMR 특허 300건 이상 (올해 상반기까지) | 001 | ✅ | 2024-12-31 기준 200건 이상(IP5 출원 기준, GM·LG 발표) → 2026년 상반기까지 300건 이상 출원(헤럴드경제) | GM·LG 발표(2025-05) · electrive(2026-06-12) · 헤럴드경제(2026-09-30) |
| 실리콘 음극과 짝지어 첫 리튬 손실을 메움 | 001 | ✅ | 「업계가 본격 확보 전부터 LMR 양극+실리콘 음극 조합에 주목해 선제적 특허 기반 구축」— 박병천 양극재기술담당 2026 발명왕 금상 | 아시아경제(2026-05-18) view.asiae.co.kr/article/2026051809104588967 · LG 뉴스룸(2026-06-21) |
| 10년 전 서랍 속 선배 연구원의 특허 메모(첫 충전만 고전압) | 001 | ❓ | 해당 인터뷰를 찾지 못함 | 검색 결과 없음 |
| 처음 4.6V 이상으로 깨우고 이후 4.3V로 운전 | 001 | ✅ (보정) | LG·서울대(임종우 교수) Nature Communications(2026-09-07): 충전 상한 4.6V→4.3V로 낮추자 산화 산소 환원율 86%→97%, 방전 하한 3.0V→2.0V로 확대 시 산소 거의 원상 회복, 40Ah 셀 883회 후 초기 에너지 92.2% 유지, 저온 활성화로 가스 억제 | LG 보도자료(2026-09-07) lg.co.kr/media/release/30540 · 파이낸셜뉴스(2026-09-07) fnnews.com/news/202609070908289383 |
| 이 기술 2022년 특허 출원 | 001 | ❓ | 출원 연도 확인 출처 없음 | 검색 결과 없음 |
| 건식 전극 공정을 LMR에 결합 연구 | 001 | ✅ (부분) | LG 건식전극 특허 약 450건 출원. LMR 결합 연구 자체는 별도 확인 못 함 | LG 보도자료(2026-06) lg.co.kr/media/release/30258 |
| AI로 소재 조합 실험 | 001 | ❓ | 출처 미확인 | 검색 결과 없음 |
| UAM까지 확장 전망 | 001 | ❓ | 전문가 전망 출처 미확인 (미래 주장 — 사용 금지) | — |

## 5. GM·얼티엄셀즈

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| GM도 2015년부터 LMR 자체 연구 | 001 | ✅ | GM 「2015년부터 망간 리치 셀 연구」, GM 보유 LMR 특허 50건 이상 | electrive(2026-06-12) electrive.com/2026/06/12/gm-advances-lmr-battery-cells-as-lfp-plans-fade · TechCrunch(2025-05-13) |
| 미국 소비자 트럭 400마일(약 640km) 원함 / GM 목표 400마일+ | 001 | ✅ | 켈티: LMR로 「트럭에서 400마일 이상」 — 목표치(EPA 인증 아님) | TechCrunch(2025-05-13) techcrunch.com/2025/05/13/gms-new-manganese-rich-battery-promises-cheaper-evs-in-2028 |
| LFP 쓰면 주행거리 400km대 초반 | 001 | ✅ (보정) | 실버라도 EV: NMC 492마일 vs 계획 LFP판 350마일(약 563km) | TechCrunch(2025-05-13) |
| NCM 트럭은 1억 원 넘는다 / 대당 수백만~천만 원 절감 | 001 | ❓ | 환산 근거 없음. 참고: LFP판은 가격을 6,000달러 낮출 계획(TechCrunch) | TechCrunch(2025-05-13) |
| 9월 말 얼티엄셀즈 발표 | 001 | ✅ | 2026-09-29 GM 성명 / 테네시주 경제개발부 발표 | CBT News(2026-09-30) · 헤럴드경제(2026-09-30) |
| 파우치 대신 각형 | 001 | ✅ | 각형(prismatic) LMR 셀 | 동일 |
| LFP와 비슷한 가격, 에너지 밀도 33%↑ | 001 | ✅ (회사 주장) | GM: 「LFP 대비 33% 높은 에너지 밀도, 비슷한 원가」— 독립 검증 아님 | CBT News · electrive(2026-06) · Argus(2025-05) |
| 각형 셀로 팩 부품 50% 이상 감소 | 001 | ✅ (보정) | 모듈 부품 75%↓, 팩 전체 부품 50%↓ (GM, 2025-05) | GM 발표 · Automotive Fleet automotive-fleet.com/news/gm-and-lg-energy-solution-introduce-the-prismatic-battery-cell |
| 스프링힐 LFP 계획을 수정해 LMR로 | 001 | ✅ (보정 필요) | 2025-07-14 「스프링힐을 전기차용 LFP로 전환, 2027년 말 상업생산」 발표 → 2026-03 LFP 라인을 ESS(에너지저장장치)용으로 전환(약 7,000만 달러) → 2026-06~07 ESS용 LFP 생산 시작 → 2026-09-29 LMR 라인 추가 10억 달러. 즉 LFP를 「버린」 것이 아니라 차량용 LFP 계획이 ESS로 돌고 LMR이 추가됨 → 2028년 이후 고니켈·LFP·LMR 3종 생산 | Manufacturing Dive(2025-07) manufacturingdive.com/news/ultium-cells-lfp-battery-production-tennessee-ev-lgenergy/753210/ · Electrek(2026-03-18) · Korea Times(2026-07-08) · 헤럴드경제(2026-09-30) |
| 올해 말 설비 공사 착수 | 001 | ✅ | 2026년 안 착공, 2028년 완료 | CBT News · 헤럴드경제 |
| 2027년 말 시범 생산 | 001 | ✅ (2025-05 발표 기준) | 2025-05 발표: 2027년 말 LG 시설에서 사전 생산(pre-production). 2026-09 발표엔 시범 생산 언급 없음 | Argus(2025-05) · TechCrunch |
| 2028년 세계 최초 양산 | 001 | ✅ (계획) | 2028년 완공 후 생산, 「상업 생산하는 첫 제조사」 / GM 첫 LMR 차량 2028년 예상(켈티, 2026-02) | CBT News · evinfrastructurenews.com |
| 2030년까지 약 10억 달러(1조 3천억 원) | 001 | ❌ (일부) | 10억 달러 맞음, 완료 시점은 2030년 아닌 2028년. 일자리 500개 추가 | CBT News · 헤럴드경제 |

## 6. LMR 비튼 각도 검토 재검증 (expansion-topics.md)

| 데이터 | 검증 | 실제값 | 출처 |
|--------|------|--------|------|
| 엔비아, 아르곤 망간계 양극재 라이선스 | ✅ | 2011-01-28 아르곤이 엔비아에 라이선스(다섯 번째 라이선스사, 앞선 사용권자: GM·LG화학·BASF·도다공업) | American Ceramic Society(2011-01-28) ceramics.org/ceramic-tech-today/argonne-extends-cathode-technology-to-envia/ · R&D World |
| 엔비아 400Wh/kg 세계 기록, 해군 연구소 검증 | ✅ | 2012-02-27 발표, ARPA-E 에너지혁신서밋에서 공개, 인디애나주 크레인 해군수상전센터 전기화학전원부 시험(45Ah 셀, 378~418Wh/kg) | Business Wire(2012-02-27) · Greentech Media · Automotive Fleet(2012-02-28) |
| GM Ventures 투자 700만~1,700만 달러 | ✅ (정리) | GM Ventures 700만 달러 투자 = GM이 주도한 1,700만 달러 투자 라운드(2011-01). 별도 계약으로 엔비아 양극재 사용권 확보 | The Engineer · just-auto · R&D World |
| 2013-02 GM 시험에서 재현 실패 | ❌ (시점 보정) | 「2013년 2월」 확인 불가. 소송 문서 기준 「2013년 봄」 재현 불가가 드러남 → 「2013년 여름」 GM 계약 취소 | MIT Technology Review(2013-12-06) technologyreview.com/2013/12/06/175207/… |
| 기술 도용 의혹 소송, 판결 미확인 | ✅ | 2013-11 전 경영진 3명(전 CEO 아툴 카파디아 포함)이 부당해고 소송 제기, CTO 수지트 쿠마르가 전 직장(NanoeXa) 지식재산을 가져왔다는 등 주장 → 2014-01 「without prejudice」로 자진 취하, 카파디아 「법원 판결이 아니다」. 별도 NanoeXa 소송(2012 제기)은 결과 미확인. 엔비아는 「근거 없다」 반박 | Charged EVs(2014-02-18) chargedevs.com/newswire/former-envia-systems-execs-drop-their-lawsuit/ · CleanTechnica(2013-12-05) · S&P AutoTechInsight |
| 포드, 2025-04 단독 LMR | ✅ | 2025-04 찰스 푼(전동화 추진 엔지니어링 디렉터) 링크드인, 미시간 로물루스 아이언파크에서 2세대 LMR 셀 시범 라인 생산, 「이번 10년 안」 | InsideEVs insideevs.com/news/757794/ · Carscoops(2025-04) · electrive(2025-04-30) |
| GM 2015 연구·2025-05 발표·2028 | ✅ | 위 5절 | — |
| A123 경기부양 자금 2.49억 달러 | ✅ | 2009-08 2억 4,910만 달러 보조금(리보니아 공장) | Green Car Reports greencarreports.com/news/1075370 · White House 아카이브 |
| A123 2012-10-16 파산 | ✅ | 2012-10-16 챕터11 신청 | Wikipedia · CBS Detroit |
| 완샹 2억 5,660만 달러 인수, 2012-12 법원 승인 / 2013-01 완료 | ✅ | 2012-12 경매 낙찰(존슨컨트롤스·NEC 약 2억 5,100만 달러 제치고), 2012-12-11 법원 승인, 2013-01-28 CFIUS 승인, 2013-01-29 종결. 국방 사업은 제외(나비타스, 225만 달러) | NBC News · AllBright Law · Renewable Energy World |
| LFP 원천 = 텍사스대 굿이너프 연구진 | ✅ | 1997 JES 논문(Padhi·Nanjundaswamy·Goodenough) / 1996 최초 기술 — 문헌마다 1995~1997로 표기 상이 | JES 144(4) 1997 · elektroauto-news(2026-10-13) · 아시아경제(2023-12) |

## 검증 요약

| 구분 | 건수 |
|------|------|
| ✅ 검증됨 (보정 포함) | 44 |
| ❌ 불일치 | 4 |
| ❓ 미확인 | 12 |

### 주요 불일치 항목
1. **망간 매장량 15억 톤 → 약 18억 톤** (USGS MCS 2026, 망간 함량 기준)
2. **스프링힐 「LFP 계획 수정」** — LFP를 접은 게 아니라 차량용 LFP 계획(2025-07)이 ESS용 LFP(2026-06 생산 시작)로 바뀌고 LMR 라인이 추가(2026-09). 한 공장에서 3종 생산 예정
3. **10억 달러 「2030년까지」 → 2028년 완공** 목표
4. **엔비아 「2013년 2월 재현 실패」 → 「2013년 봄」 재현 불가 드러남, 「여름」 GM 계약 취소** (MIT Technology Review)
5. (미확인 주의) **LG 2009년 착수·10년 전 서랍 특허·2022년 특허** 근거 없음 → 대본 사용 금지. 「첫 특허 2010년」만 사용
6. (미확인 주의) **리튬 함량 LFP 2% vs LMR 8%(4배)** — 양극재 기준 LFP 약 4.4%로 상충, 사용 금지
