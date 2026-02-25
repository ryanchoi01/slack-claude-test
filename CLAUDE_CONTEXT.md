# 프로젝트 컨텍스트

## 프로젝트 개요
Slack Claude Bot 테스트용 Python 프로젝트입니다.

## 코딩 컨벤션
- Python 3.10+ 문법 사용
- 함수에 타입 힌트 필수
- 한국어 주석 사용
- 함수명은 snake_case

## 금지 사항
- print() 디버깅 코드를 커밋하지 마세요
- 하드코딩된 비밀번호/API키 절대 금지
- 테스트 없이 핵심 로직 변경 금지

## 파일 구조
- `app.py` : 메인 애플리케이션 로직
- `CLAUDE_CONTEXT.md` : 이 파일 (수정 금지)

## 테스트
- pytest 사용
- 새 함수 추가 시 반드시 테스트 함수도 함께 작성

---

## Git 규칙 (반드시 준수)

### 커밋 메시지 형식
`prefix: 짧은 설명`

| Prefix | 용도 |
|--------|------|
| feat: | 새 기능 |
| fix: | 버그 수정 |
| refactor: | 동작 변경 없는 코드 구조 변경 |
| perf: | 성능 개선 |
| docs: | 문서만 변경 |
| chore: | 유지보수 (의존성, 정리, 설정) |
| style: | 포맷, 공백 (로직 변경 없음) |
| test: | 테스트 추가/수정 |
| revert: | 이전 커밋 되돌리기 |

### 브랜치 명명 규칙
`prefix/설명` 형식

| Prefix | 용도 | 예시 |
|--------|------|------|
| feature/ | 신기능 | feature/add-farewell-function |
| fix/ | 버그 수정 | fix/null-reference-error |
| refactor/ | 리팩토링 | refactor/cleanup-greeting |
| docs/ | 문서 | docs/update-readme |
| test/ | 테스트 | test/add-greet-test |

### 브랜치 전략
- 기준 브랜치: **dev**
- dev에서 분기 → 작업 완료 후 PR로 dev에 머지
- 머지는 반드시 **--no-ff** (merge commit 생성, 트리 유지)
- main/master 직접 푸시 금지
- 다음 작업 시작 전 반드시 dev 기준으로 **rebase**

### 위험 작업 (실행 전 반드시 경고)
- `git push --force`
- `git reset --hard`
- `git clean`
- `git branch -D`
