# 웹 기반 AI 챗봇 서비스 (Term Project) — 진행 체크리스트

> 원본 과제: FastAPI + SQLite + AI API, 로그인 사용자 전용 챗봇, 대화 로그 저장/조회, 외부 배포.
> 혼자 진행하지만 브랜치/PR 흐름은 팀 프로젝트처럼 연습한다.

## 0. 프로젝트 뼈대
- [ ] Git 브랜치 전략 (main / develop / feature/*)
- [ ] 가상환경 + requirements.txt
- [ ] .gitignore / .env.example
- [ ] FastAPI 앱 기동 (헬스체크 라우트)

## 1. 설정 & DB
- [ ] 환경 변수 로딩 (config)
- [ ] SQLite 연결 + 세션 관리
- [ ] 모델: users, chats (user_id, created_at, question, answer)

## 2. 인증 / 접근 제어
- [ ] 회원가입 (비밀번호 해싱)
- [ ] 로그인 / 로그아웃 (세션 또는 토큰)
- [ ] 로그인 필요 의존성 (비로그인 접근 차단)

## 3. AI 챗봇 파이프라인
- [ ] AI API 클라이언트 (서버 측 호출, 타임아웃 설정)
- [ ] 실패/타임아웃 예외 처리 → 사용자 오류 응답 (예: AI_TIMEOUT)
- [ ] 컨텍스트 전략 (최근 N개 대화 포함)
- [ ] POST /api/chat (질문 수신 → AI 호출 → 응답 → DB 저장)
- [ ] 입력 검증 (빈 입력 차단, 길이 제한)
- [ ] 서버 로그: request_received / ai_call_start / ai_call_success·fail / db_save_success·fail

## 4. 로그 조회
- [ ] GET /api/me/chats (내 대화 로그)
- [ ] scripts/check_logs.sql (확인용 SQL)

## 5. 웹 UI
- [ ] 회원가입/로그인 페이지
- [ ] 채팅 페이지 (같은 화면에서 질문·응답 확인)

## 6. 배포 & 문서
- [ ] 외부 접속 가능한 배포 (URL 확보)
- [ ] README: 개요 / 아키텍처 / API 명세 / DB 구조 / 실행·배포 / 환경 변수 / 역할 / DB 확인 가이드
- [ ] PR 기반 merge 기록, 의미 있는 커밋 10회 이상
