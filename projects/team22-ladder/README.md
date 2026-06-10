# 냉장고털이

> 냉장고 속 재료를 입력하면 보유 재료, 양념, 조리도구를 바탕으로 만들 수 있는 레시피를 추천해주는 AI 기반 레시피 추천 서비스입니다.

## 프로젝트 소개

`냉장고털이`는 집에 있는 재료를 효율적으로 활용하지 못해 음식물 쓰레기가 발생하거나, 매번 무엇을 요리할지 고민하는 문제를 줄이기 위해 만든 서비스입니다.

사용자는 냉장고 사진 또는 텍스트로 재료를 입력하고, 필수로 사용하고 싶은 재료와 유통기한이 임박한 재료를 표시할 수 있습니다. 이후 보유한 소스, 조리도구, 추가 재료를 선택하면 현재 조건에서 만들기 쉬운 레시피를 확인할 수 있습니다.

## 주요 기능

### 1. 재료 입력

- 냉장고 사진 업로드를 통한 재료 입력 흐름 제공
- 텍스트 단일 입력 및 여러 재료 일괄 입력 지원
- 입력된 재료를 카드 형태로 확인
- 재료별 `필수`, `유통기한 임박`, `삭제` 상태 관리
- Unsplash API를 활용한 재료 이미지 표시
- Upstage Solar API를 활용한 한국어 재료명 영어 검색어 변환

### 2. 재료 보강

- 보유 소스 및 양념 선택
- 사용 가능한 조리도구 선택
- 냉장고 밖 추가 재료 입력
- 최종 재료 목록 미리보기
- 필수 재료, 유통기한 임박 재료, 일반 재료를 구분해 확인

### 3. 레시피 추천

- 입력한 재료를 기준으로 추천 레시피 표시
- 초보 요리사를 위한 쉬운 레시피 구분
- 전자레인지로 만들 수 있는 간편 요리 구분
- 보유 재료와 부족한 재료를 함께 표시
- 난이도와 예상 조리 시간 제공


## 서비스 화면

### 홈 화면

<!-- 홈 화면: 서비스 진입 화면 및 3단계 사용 흐름 안내 -->
<img width="1008" height="812" alt="홈 화면" src="https://github.com/user-attachments/assets/8526ba76-6bdc-44b2-b0f8-0f878f34cbb3" />

### 재료 입력 화면

#### 사진 업로드로 재료 입력

<!-- 재료 입력 화면: 냉장고 사진 업로드 영역 -->
<img width="862" height="814" alt="재료 입력 - 사진 업로드" src="https://github.com/user-attachments/assets/12a4f2b2-6a64-4300-b190-56f52a9c9682" />

#### 재료 분석 결과

<!-- 재료 입력 화면: 사진 분석 후 추출된 재료 카드 목록 -->
<img width="720" height="812" alt="재료 입력 - 분석 결과" src="https://github.com/user-attachments/assets/33886550-5278-4b15-9ab2-de7331273338" />

#### 직접 입력으로 재료 추가

<!-- 재료 입력 화면: 텍스트로 단일 재료 또는 여러 재료를 직접 입력 -->
<img width="600" height="724" alt="재료 입력 - 직접 입력" src="https://github.com/user-attachments/assets/aae1d720-c924-413c-8699-61d07872c2ba" />

#### 재료 상태 관리

<!-- 재료 입력 화면: 필수 재료, 유통기한 임박 재료, 삭제 기능 -->
<img width="660" height="224" alt="재료 입력 - 재료 상태 관리" src="https://github.com/user-attachments/assets/c403148f-1667-4380-b862-32bf4952e31a" />

### 재료 보강 화면

#### 소스 및 조리도구 선택

<!-- 재료 보강 화면: 보유 소스와 사용 가능한 조리도구 선택 -->
<img width="688" height="812" alt="재료 보강 - 소스 및 조리도구 선택" src="https://github.com/user-attachments/assets/b223d7e2-2943-4d93-9dab-fa41a8c3fd2c" />

#### 최종 재료 목록 확인

<!-- 재료 보강 화면: 필수 재료, 유통기한 임박 재료, 소스, 추가 재료 최종 확인 -->
<img width="1022" height="820" alt="재료 보강 - 최종 재료 목록" src="https://github.com/user-attachments/assets/7457f52b-d822-4311-9836-d41bedeef982" />

### 레시피 추천 화면

#### 초보 요리사 추천

<!-- 레시피 추천 화면: 보유 재료 기반 초보자용 추천 레시피 -->
<img width="660" height="810" alt="레시피 추천 - 초보 요리사 추천" src="https://github.com/user-attachments/assets/2d47d066-af31-44ea-89e2-25f9fd20bfac" />

#### 전자레인지 간편 요리

<!-- 레시피 추천 화면: 전자레인지로 만들 수 있는 간편 요리 추천 -->
<img width="650" height="814" alt="레시피 추천 - 전자레인지 간편 요리" src="https://github.com/user-attachments/assets/ed3ad229-cd9e-453a-b593-f87b9c73d65c" />
## 기술 스택

| 영역 | 기술 |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI, Uvicorn |
| Language | Python |
| AI/API | Upstage Solar API, OpenAI SDK |
| Image API | Unsplash API |
| Environment | python-dotenv |

## 프로젝트 구조

```text
team22-ladder/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   └── main.py
│   └── requirements.txt
├── frontend/
│   ├── static/
│   │   └── logo.png
│   ├── views/
│   │   ├── home.py
│   │   ├── step1.py
│   │   ├── step2.py
│   │   └── step3.py
│   ├── app.py
│   ├── example.env
│   └── requirements.txt
└── README.md
```

## 실행 방법

### 1. Backend 실행

```bash
cd projects/team22-ladder/backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Windows 환경에서는 가상환경 활성화 명령어를 아래처럼 사용합니다.

```bash
.venv\Scripts\activate
```

Backend 실행 후 아래 주소에서 상태와 API 문서를 확인할 수 있습니다.

- Health Check: http://localhost:8000/health
- Swagger Docs: http://localhost:8000/docs

### 2. Frontend 실행

새 터미널을 열고 아래 명령어를 실행합니다.

```bash
cd projects/team22-ladder/frontend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Frontend 실행 후 아래 주소로 접속합니다.

- Streamlit App: http://localhost:8501

## 환경 변수

Frontend에서 외부 API를 사용하려면 `frontend/example.env`를 참고해 `.env` 파일을 생성합니다.

```bash
cd projects/team22-ladder/frontend
cp example.env .env
```

`.env` 파일에 필요한 값을 입력합니다.

```env
UNSPLASH_ACCESS_KEY=
UPSTAGE_API_KEY=
API_URL=http://localhost:8000
```

| 변수 | 설명 |
|---|---|
| `UNSPLASH_ACCESS_KEY` | 재료 이미지를 검색하기 위한 Unsplash Access Key |
| `UPSTAGE_API_KEY` | 한국어 재료명을 영어 이미지 검색어로 변환하기 위한 Upstage Solar API Key |
| `API_URL` | FastAPI 백엔드 주소 |

API Key가 없어도 앱 실행은 가능하지만, 재료 이미지는 기본 이모지로 대체되고 재료명 번역 기능은 비활성화됩니다.

## 현재 구현 상태

- Streamlit 기반 3단계 레시피 추천 UI 구현
- 재료 입력, 상태 표시, 재료 보강, 추천 결과 화면 구현
- Unsplash 재료 이미지 검색 연동
- Upstage Solar API 기반 재료명 번역 연동
- FastAPI 백엔드 기본 서버 및 `/health` 엔드포인트 구현

현재 레시피 추천 결과는 프론트엔드 내부의 샘플 데이터를 기반으로 표시됩니다. 이후 백엔드 API와 AI 추천 로직을 연결해 실제 입력 조건에 맞춘 추천 결과를 생성하도록 확장할 수 있습니다.

## 기대 효과

- 냉장고 속 남은 재료를 빠르게 파악하고 활용 가능
- 유통기한이 임박한 재료를 우선 사용하는 요리 선택 가능
- 초보자도 만들기 쉬운 레시피를 확인해 요리 진입 장벽 완화
- 보유한 조리도구와 양념을 반영해 현실적인 레시피 탐색 가능
