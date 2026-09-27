# 팩트체크

> 프로젝트: mosquito-vanish ("모기가 갑자기 시야에서 사라지는 이유")
> 검증일: 2026-09-27
> 대상: 레퍼런스 001, 002, 003, 004, 005 (analysis.md 없음 — 자막만으로 진행)
> 표기: ✅ 검증됨 / ⚠️ 부분 일치·조건부(맥락 보정 필요) / ❌ 불일치 / ❓ 미확인
> ※ 005(EBS 초파리·시각 대담)는 주제와 거리가 먼 항목이 많아, 대본에 쓸 가능성이 있는 항목 위주로 검증함

## 1. 모기 비행 속도·비행 능력

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| 모기 비행 속도 시속 2.4~4.8km | 001 | ❌ | 미국모기방제협회(AMCA): 종에 따라 시속 1~1.5마일(약 1.6~2.4km). 실험실 3D 추적(말라리아모기, 사람 냄새+열 조건) 평균 초속 24.5cm(시속 약 0.9km). 001의 수치는 상한을 넘거나 그 상단 | AMCA FAQ https://www.mosquito.org/faqs/ · Spitzen et al. 2013, PLOS ONE (Wageningen대) https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0062995 |
| 모기 평균 비행 속도 시속 약 3.6km(사람 걷는 속도 4km와 비슷) | 002 | ⚠️ | "모기는 빠르지 않다"는 결론은 맞음. 다만 평균 3.6km/h(초속 1m)는 과대. 평균은 시속 1~2.4km 수준. 초속 1m 이상은 일부 연구의 이집트숲모기 값(1.12m/s, Bradley 2017 — 2차 인용으로만 확인) | AMCA FAQ · Spitzen 2013 (위와 동일) |
| 모기는 1초에 최대 약 1m 이동 | 002, 003 | ⚠️ | '최대'로는 가능 범위(이집트숲모기 평균 1.12m/s 보고가 2차 문헌에 있음). 원문 1차 확인은 못 함. 평균 비행은 초속 0.25~0.7m | AMCA FAQ · Spitzen 2013 · CSU ScholarWorks 논문 내 Bradley et al. 2017 인용(원문 접근 불가) |
| 파리 비행 속도 시속 8~15km, 모기의 3~4배 | 001 | ⚠️ | 집파리 순항 약 시속 7.2km(초속 2m), 순간 최대 시속 24km라는 2차 자료만 확인. "모기보다 몇 배 빠르다"는 방향은 맞지만 정확한 배수는 1차 출처 미확보 | Speed of Animals(2차) https://www.speedofanimals.com/animals/housefly · U. Michigan BioKIDS https://www.biokids.umich.edu/critters/Musca_domestica/ (단, 날갯짓 '분당 1,000회' 기술은 오류라 신뢰도 낮음) |
| 모기는 다른 곤충보다 더 빠르게 비행할 수 있다 | 003 | ❌ | 모기는 파리보다 느림. '빠른 비행'이 아니라 **예측 불가한 비행 경로(protean flight)와 회피 기동**이 핵심 | Cribellier et al. 2022, Current Biology (Wageningen대) https://doi.org/10.1016/j.cub.2022.01.036 |
| 날개가 길고 얇아 움직이는 각도가 작다 | 003 | ✅ | 모기 날갯짓 각도 약 40°, 다른 곤충의 절반 이하(꿀벌의 절반 미만). 날갯짓 초당 약 800회 | Bomphrey et al. 2017, Nature (옥스퍼드대·RVC·지바대) https://www.nature.com/articles/nature21727 · ScienceDaily 2017-03-30 https://www.sciencedaily.com/releases/2017/03/170330115241.htm |
| 모기는 날개 뒤쪽 소용돌이(후연 와류)까지 이용해 추가 양력을 얻는다(일반 곤충엔 없는 현상) | 002 | ✅ | 앞전 와류 + 후연 와류('wake capture') + 회전 항력 3가지 메커니즘 | Bomphrey et al. 2017, Nature (위와 동일) |
| 초파리는 날갯짓 한 번에 양력 2번, 모기는 약 4번 | 002 | ❓ | 원 출처(최해천 교수 연구로 추정) 확인 못 함. Bomphrey 2017은 메커니즘 3종을 제시할 뿐 "4번" 수치는 없음 | 검색 결과 없음 |

## 2. 사람의 인지·반응 시간

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| 빛이 망막에 맺히고 뇌가 모기를 인지하기까지 최대 0.1초 | 002, 003 | ⚠️ | 망막→1차 시각피질 신호 도달 약 50ms 이하, 의식적 인지는 추가 되먹임 처리가 필요해 더 걸림. "0.1초 전후"는 대략적 표현으로 허용 가능하나 '최대'는 부정확 | Cerebral Cortex 2022 "Early neural activity changes associated with stimulus detection" https://doi.org/10.1093/cercor/bhac140 |
| 인지 후 손을 움직이기까지 평균 0.3초 | 002, 003 | ✅ | 시각 자극 단순 반응시간 평균 약 0.2~0.3초(자 떨어뜨려 잡기 150~220ms) | 자 떨어뜨리기 검사 타당도 연구, PMC10920456 https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10920456/ · TopEndSports https://www.topendsports.com/testing/tests/reaction-stick.htm |
| 0.1초면 모기는 10cm, 0.3초면 30cm 이동 | 002, 003 | ⚠️ | 초속 1m 가정 시의 계산. 평균 속도(초속 0.25~0.7m) 기준이면 0.3초에 약 7~20cm | 위 속도 자료로 계산 |
| 가까이 있는 모기일수록 더 빨리 움직이는 것처럼 보인다 | 002 | ✅ | 기하학적 사실: 각속도 = 속도 ÷ 거리. 같은 속도라도 거리가 1/3이면 눈에 보이는 이동 각도는 3배 | 계산(각속도 공식) |

## 3. 눈의 움직임·깜빡임

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| 성인은 1분에 15~20번 눈을 깜빡인다 | 001 | ✅ | 분당 10~20회(15~20회로 인용하는 자료 다수) | PMC12733691 "The Role of Spontaneous Eye Blinks in Temporal Perception" https://pmc.ncbi.nlm.nih.gov/articles/PMC12733691/ |
| 깜빡임 속도 100~150(ms로 추정) | 001 | ⚠️ | 자막은 "100~150미터"로 오기. 깜빡임 1회 약 100~400ms(150~300ms 인용 다수), 깜빡임마다 약 110ms 시각 공백 | PMC12733691 (위와 동일) |
| 큰 물체를 따라갈 때 눈 속도는 최대 초당 700도 | 001 | ⚠️ | 초당 500~700도(최대 900도)는 **도약 안구운동(사카드)의 최고 속도**이지 '움직이는 물체를 따라가는 속도'가 아님. 부드러운 추적(smooth pursuit)은 초당 약 90도를 넘으면 정확도가 떨어짐 | Britannica "Saccade" https://www.britannica.com/science/saccade · PMC2887486 (Lisberger, 추적 안구운동 리뷰) https://pmc.ncbi.nlm.nih.gov/articles/PMC2887486/ · Frontiers 2013 (smooth pursuit 리뷰) https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2013.00004/full |
| 깜빡임 전후로 초점이 미세하게 달라지고, 모기가 직선으로 날지 않아 놓친다 | 001 | ⚠️ | '모기가 예측 불가한 경로로 난다'는 부분은 Cribellier 2022로 뒷받침됨. '깜빡임 때 초점이 어긋난다'는 1차 근거 미확인 | Cribellier et al. 2022 (위와 동일) |
| 복잡한 배경이 모기를 위장시키고 정보가 끊겨 들어온다 | 001 | ⚠️ | 주변시에서 주변 무늬가 대상 식별을 방해하는 '밀집 효과(crowding)'는 확립된 현상. 모기 사례에 직접 적용한 연구는 미확인 | Strasburger, Rentschler & Jüttner 2011, Journal of Vision https://doi.org/10.1167/11.5.13 |
| 눈만이 아니라 머리도 함께 움직이는 것이 좋다 | 001 | ❓ | 근거 연구 미확인. 오히려 '한 점을 응시하고 주변시로 보는 편이 움직임 변화를 더 잘 잡는다'는 연구가 있음(추가 리서치 참조) | 검색 결과 없음 |
| 눈은 초당 2~3번 움직인다(사카드) | 005 | ✅ | "사람은 초당 2~3회 도약 안구운동을 한다" | Crevecoeur & Kording 2017, eLife https://elifesciences.org/articles/25073 |
| 눈이 움직이는 동안의 흔들린 영상을 뇌가 지운다 | 005 | ✅ | 사카드 억제(saccadic suppression): 사카드 직전·도중 시각 감도가 크게 떨어짐 | Crevecoeur & Kording 2017, eLife (위와 동일) · ScienceDirect Topics "Saccadic Suppression" https://www.sciencedirect.com/topics/immunology-and-microbiology/saccadic-suppression |
| 중심와(fovea) 때문에 아주 좁은 영역만 선명하게 본다 | 005 | ✅ | 중심와 약 5.2°, 가장 선명한 중심소와 1~1.2°, 황반 약 17° | Wikipedia "Fovea centralis"(교과서 수치 정리) https://en.wikipedia.org/wiki/Fovea_centralis |
| 원추세포는 색·세밀함, 막대세포는 명암·어두운 곳, 넓게 드문드문 분포 | 005 | ✅ | 중심와 원추세포 밀도 mm²당 10만~32만 개, 주변으로 갈수록 급감 | PMC7416892 (원추세포 밀도·피질 확대) https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7416892/ |
| 비상구 표시등이 초록색인 이유는 막대세포가 초록을 잘 보기 때문 | 005 | ❓ | 막대세포 최대 감도가 청록(약 500nm)인 것은 사실이나, 비상구 등 색 선정 이유로 확인된 자료 없음 | 검색 결과 없음 |

## 4. 주의·시각 체계 일반 (005)

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| 보이지 않는 고릴라 실험 — 50%만 고릴라를 알아챔 | 005 | ✅ | Simons & Chabris 1999(하버드대), 고릴라 9초 등장, 관찰자 약 50%만 인지 | Simons & Chabris 1999, Perception https://journals.sagepub.com/doi/10.1068/p281059 |
| 사람 시신경은 약 100만 화소 | 005 | ✅ | 시신경 축삭 약 120만 개 | Mikelberg et al. 1989, Ophthalmology "The normal human optic nerve" https://pubmed.ncbi.nlm.nih.gov/2780002/ |
| 초파리 겹눈은 한쪽 약 800개 렌즈 | 005 | ✅ | 약 800개 낱눈(ommatidia) | Frontiers in Cellular Neuroscience 2009 "Drosophila photoreceptors and signaling mechanisms" https://www.frontiersin.org/journals/cellular-neuroscience/articles/10.3389/neuro.03.002.2009/full |
| 초파리 뇌세포 13만~15만 개 | 005 | ✅ | 139,255개(FlyWire 2024) | FlyWire Consortium 2024, Nature https://www.science.org/content/article/complete-map-fruit-fly-brain-circuitry-unveiled |
| 초파리 시야 약 330° | 005 | ❓ | 1차 출처 미확인 | 검색 결과 없음 |
| 초파리 반응 속도는 사람 눈의 약 5배 | 005 | ❓ | 1차 출처 미확인 | 검색 결과 없음 |
| 뇌에서 시각 담당 비율 사람 30%, 초파리 60% | 005 | ❓ | 1차 출처 미확인 | 검색 결과 없음 |
| 쥐의 Pax6 유전자를 초파리에 넣으면 다리에 (초파리) 눈이 생긴다 | 005 | ✅ | Halder, Callaerts & Gehring 1995(바젤대): eyeless 발현으로 날개·다리·더듬이에 겹눈 유도, 쥐 Pax6로도 겹눈 유도 | Halder et al. 1995, Science https://www.science.org/doi/10.1126/science.7892602 |
| 초파리는 붉은색을 잘 못 본다 / 곤충은 자외선을 본다 | 005 | ✅ (일반) | 초파리 시각 스펙트럼은 사람보다 단파장 쪽 | Frontiers 2009 (위와 동일) |

## 5. 모기 행동 (004)

| 데이터 | 레퍼 | 검증 | 실제값 | 출처 |
|--------|------|------|--------|------|
| 불을 켜면 모기는 순간적으로 눈이 멀어 멀리 못 가고 벽·커튼에 앉는다 | 004 | ⚠️ | '눈이 먼다'는 근거 없음. 다만 밤 시작 시점의 빛 펄스가 말라리아모기의 비행을 즉각 억제한다는 실험은 있음(시간대에 따라 오히려 활동 증가). 모기가 실내 벽 등에 앉아 쉬는 습성 자체는 사실 | Sheppard et al. 2017, Parasites & Vectors https://parasitesandvectors.biomedcentral.com/articles/10.1186/s13071-017-2196-3 · Dzul-Manzanilla et al. 2017, J. Med. Entomol. https://academic.oup.com/jme/article-abstract/54/2/501/2952758 |
| 전기 모기채를 휘두르면 바람 때문에 모기가 밀려나 잡기 어렵다 | 004 | ✅ | 모기는 휘두르는 물체가 만든 공기 파도(bow wave)로 능동적으로 파고들어 함께 밀려나며 탈출. 구멍 뚫린 채를 쓰면 명중률 2배 | Cribellier et al. 2024, Current Biology (Wageningen대) https://doi.org/10.1016/j.cub.2024.01.066 |
| 모기는 구조상 위아래 움직임이 느리니 수직으로 내리쳐라 | 004 | ❓ | 근거 연구 미확인 | 검색 결과 없음 |
| 모기는 발냄새 원인 이소발레르산을 미치도록 좋아한다 | 004 | ⚠️ | 말라리아모기가 사람 발냄새와 림버거 치즈 냄새에 비슷하게 끌린다(Knols & De Jong 1996, 2006 이그노벨상). 이소발레르산은 발냄새 성분 중 하나. 한국 주요 모기(빨간집모기·흰줄숲모기)에 대한 '미치도록'은 과장 | Knols & De Jong 1996, Parasitology Today — Wageningen 연구포털 https://research.wur.nl/en/publications/limburger-cheese-as-an-attractant-for-the-malaria-mosquito-anophe/ |

## 검증 요약

| 구분 | 건수 |
|------|------|
| ✅ 검증됨 | 17 |
| ⚠️ 부분 일치(조건부) | 12 |
| ❌ 불일치 | 2 |
| ❓ 미확인 | 8 |

(⚠️는 프롬프트의 3단계 분류상 "✅이되 맥락 보정 필요"로 취급 — verified-data.md에는 보정된 값으로 수록)

### 주요 불일치 항목
1. **모기 비행 속도 시속 2.4~4.8km(001)** → 실제는 시속 1~1.5마일(1.6~2.4km, AMCA), 실험실 추적 평균 초속 약 25cm(시속 0.9km). 002의 "평균 3.6km/h"도 과대.
2. **"모기는 다른 곤충보다 빠르게 난다"(003)** → 틀림. 파리보다 느림. 사라지는 이유는 속도가 아니라 예측 불가한 경로·회피 기동·사람 시각의 한계.
3. **"눈은 초당 700도로 물체를 따라간다"(001)** → 700도는 사카드(시선 점프) 속도. 부드러운 추적은 초당 약 90도 이하에서만 정확.
4. **"불 켜면 모기 눈이 먼다"(004)** → 근거 없음. 빛이 비행을 억제하는 실험은 있으나 '실명'은 아님.
