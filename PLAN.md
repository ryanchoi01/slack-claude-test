# 영어 학습 앱 구현 계획서

## 개요

**목적**: CLI 기반 영어 학습 앱 구축
**범위**: 어휘 학습(플래시카드), 퀴즈, 학습 진도 추적 기능을 갖춘 Python 앱
**대상 사용자**: 영어를 공부하는 한국어 사용자
**기술 스택**: Python 3.10+, 표준 라이브러리 + rich(터미널 UI)

---

## 변경 파일 목록

### 신규 추가
| 파일 | 설명 |
|------|------|
| `app.py` | 메인 진입점 (기존 내용 대체) |
| `english_app/vocabulary.py` | 단어장 관리 (추가/삭제/조회) |
| `english_app/quiz.py` | 퀴즈 엔진 (4지선다, 빈칸 채우기) |
| `english_app/flashcard.py` | 플래시카드 학습 모드 (SM-2 알고리즘 기반 반복 학습) |
| `english_app/progress.py` | 학습 진도 기록 및 통계 |
| `english_app/storage.py` | JSON 파일 기반 데이터 영속성 |
| `english_app/__init__.py` | 패키지 초기화 |
| `data/words.json` | 기본 단어 데이터베이스 (초급~중급 200단어) |
| `data/progress.json` | 사용자 학습 진도 저장소 (자동 생성) |
| `requirements.txt` | 의존성 목록 (rich) |

### 수정
| 파일 | 변경 내용 |
|------|-----------|
| `app.py` | 영어 학습 앱 메인 메뉴로 교체 |
| `README.md` | 앱 설명 및 실행 방법 추가 |

---

## 구현 단계

### 1단계: 프로젝트 구조 및 데이터 설계
- `english_app/` 패키지 디렉토리 생성
- `data/words.json` 단어 데이터 구조 설계 및 초기 단어 200개 입력
  ```json
  {
    "id": "w001",
    "word": "abandon",
    "meaning_ko": "버리다, 포기하다",
    "example": "He abandoned his car on the highway.",
    "level": "intermediate",
    "category": "verb"
  }
  ```
- `data/progress.json` 진도 스키마 설계

### 2단계: 핵심 모듈 구현
- **`storage.py`**: JSON 읽기/쓰기 유틸리티
- **`vocabulary.py`**: 단어 CRUD, 레벨/카테고리별 필터링, 오늘의 단어(Word of the Day)
- **`progress.py`**: 학습 이력 기록, 정답률 계산, 연속 학습일(streak) 추적

### 3단계: 학습 모드 구현
- **`flashcard.py`**: SM-2 기반 간격 반복(Spaced Repetition) 플래시카드
  - 정답/오답에 따른 복습 간격 자동 조정
  - 한국어 뜻 → 영어 단어 / 영어 단어 → 한국어 뜻 양방향 지원
- **`quiz.py`**: 퀴즈 엔진
  - 4지선다 (영→한, 한→영)
  - 빈칸 채우기 (예문에서 단어 맞추기)
  - 레벨별 난이도 조정

### 4단계: 메인 앱 및 UI 조립
- **`app.py`**: rich 라이브러리를 활용한 터미널 UI 메인 메뉴
  ```
  ┌─────────────────────────────┐
  │   📚 영어 학습 앱           │
  │  오늘의 단어: abandon       │
  ├─────────────────────────────┤
  │  1. 플래시카드 학습         │
  │  2. 퀴즈                    │
  │  3. 단어장 보기             │
  │  4. 학습 통계               │
  │  5. 종료                    │
  └─────────────────────────────┘
  ```
- 메뉴 라우팅 및 세션 흐름 구현

### 5단계: 문서화 및 마무리
- `README.md` 업데이트 (설치, 실행 방법, 기능 설명)
- `requirements.txt` 작성
- 기본 단어 데이터 품질 검수

---

## 고려사항

### 의존성
- `rich` 라이브러리: 터미널 컬러/테이블/패널 렌더링. `pip install rich`로 설치.
- Python 표준 라이브러리(`json`, `random`, `datetime`, `pathlib`)만 그 외 사용하여 의존성 최소화.

### 데이터 영속성
- 별도 DB 없이 `data/progress.json`에 로컬 저장. 단순성 우선.
- 단어 데이터(`words.json`)와 진도 데이터(`progress.json`)를 분리하여 관리.

### SM-2 알고리즘 (간격 반복)
- 기억 과학 기반 복습 스케줄링: 쉬운 단어는 긴 간격, 어려운 단어는 짧은 간격으로 반복.
- 구현 복잡도는 낮지만 학습 효과가 높음.

### 확장 가능성 (현재 미구현)
- 웹 UI (Flask/FastAPI) 전환 경로 고려하여 비즈니스 로직과 UI 분리 설계.
- 추후 Claude API 연동으로 AI 튜터 기능 추가 가능.
- 사용자 단어 추가 기능(커스텀 단어장).

### 리스크
- 초기 단어 데이터(200개) 품질: 예문, 번역 정확성 검수 필요.
- Windows/Linux/macOS 터미널 인코딩(UTF-8) 차이로 인한 한글 출력 문제 → `PYTHONIOENCODING=utf-8` 설정 안내.
