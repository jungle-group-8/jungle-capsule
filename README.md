# Jungle Capsule

정글 구성원끼리 메시지를 타임캡슐로 보내고, 지정한 날짜에 열어볼 수 있는 웹 애플리케이션입니다. 같은 커리큘럼과 기수의 동료를 수신자로 선택해 글·이미지·링크를 담은 캡슐을 만들 수 있습니다.

## 주요 기능

- 회원가입, 아이디 중복 확인, 로그인 및 로그아웃
- 같은 커리큘럼·기수 구성원 조회 및 수신자 선택
- 제목, 미리보기 문구, 본문, 공개일, 링크, 이미지를 포함한 캡슐 생성
- 수신한 캡슐 목록과 공개일까지 남은 날짜 확인
- 공개일이 지난 캡슐의 상세 내용 조회 및 삭제
- AWS S3 이미지 업로드 및 1시간 동안 유효한 조회 URL 생성
- 오늘의 질문 조회 및 사용자 질문 등록
- 열린 캡슐, 오늘 보낸 캡슐, 오늘 받은 캡슐 수 집계

## 기술 스택

| 구분 | 기술 |
| --- | --- |
| Backend | Python, Flask, Jinja2 |
| Database | MongoDB, PyMongo |
| Storage | AWS S3, Boto3 |
| Frontend | HTML, JavaScript, Tailwind CSS |
| Configuration | python-dotenv |

## 프로젝트 구조

```text
jungle-capsule/
├── app.py                  # Flask 앱 생성 및 Blueprint 등록
├── database.py             # MongoDB 연결
├── requirements.txt        # Python 의존성
├── package.json            # Tailwind CSS 의존성
├── routes/
│   ├── auth.py             # 로그인·회원가입 페이지
│   ├── capsule.py          # 메인·캡슐 생성·보관함 페이지
│   ├── capmaking.py        # 캡슐 저장
│   ├── capsulelist.py      # 캡슐 목록 및 통계
│   ├── checkcap.py         # 사용자별 캡슐 조회
│   ├── deletecap.py        # 캡슐 삭제
│   ├── detailcpa.py        # 공개된 캡슐 상세 조회
│   ├── member.py           # 같은 기수 구성원 조회
│   └── question.py         # 오늘의 질문 관리
├── services/
│   ├── auth/login.py       # 인증 처리
│   └── imageupload.py      # S3 업로드 및 조회 URL 생성
├── templates/              # Jinja2 화면 템플릿
└── static/
    ├── css/                # Tailwind 입력·빌드 결과
    └── images/             # 화면 이미지 리소스
```

## 시작하기

### 1. 사전 준비

- Python 3.9 이상
- Node.js 및 npm
- MongoDB 인스턴스
- 이미지 기능을 사용할 경우 AWS S3 버킷과 접근 키

### 2. 저장소 복제 및 이동

```bash
git clone https://github.com/jungle-group-8/jungle-capsule.git
cd jungle-capsule
```

### 3. Python 가상환경 및 의존성 설치

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 4. 환경 변수 설정

프로젝트 루트에 `.env` 파일을 만들고 아래 값을 설정합니다.

```dotenv
SECRET_KEY=충분히-긴-임의의-문자열
MONGO_URL=mongodb://localhost:27017
S3_ACCESS_KEY=AWS_ACCESS_KEY_ID
S3_SECRET_KEY=AWS_SECRET_ACCESS_KEY
S3_BUCKET=버킷명
```

| 변수 | 설명 |
| --- | --- |
| `SECRET_KEY` | Flask 세션 서명에 사용하는 비밀 키 |
| `MONGO_URL` | MongoDB 연결 문자열 |
| `S3_ACCESS_KEY` | S3 접근 권한이 있는 AWS 액세스 키 |
| `S3_SECRET_KEY` | AWS 시크릿 액세스 키 |
| `S3_BUCKET` | 이미지를 저장할 S3 버킷 이름 |

S3 클라이언트의 리전은 현재 `ap-northeast-2`로 설정되어 있습니다. 다른 리전을 사용한다면 `services/imageupload.py`의 `region_name`을 변경해야 합니다.

### 5. 프런트엔드 의존성 및 CSS 빌드

```bash
npm install
npx @tailwindcss/cli -i ./static/css/input.css -o ./static/css/output.css
```

스타일을 수정하면서 자동으로 다시 빌드하려면 다음 명령을 별도 터미널에서 실행합니다.

```bash
npx @tailwindcss/cli -i ./static/css/input.css -o ./static/css/output.css --watch
```

### 6. 애플리케이션 실행

```bash
python app.py
```

브라우저에서 [http://localhost:5001](http://localhost:5001)에 접속합니다.

## 주요 URL

| Method | 경로 | 설명 |
| --- | --- | --- |
| `GET` | `/` | 메인 화면 |
| `GET` | `/login` | 로그인 화면 |
| `GET` | `/sign-up` | 회원가입 화면 |
| `POST` | `/login/check` | 로그인 처리 |
| `POST` | `/logout` | 로그아웃 |
| `POST` | `/signup` | 회원가입 처리 |
| `POST` | `/signup/idCheck` | 아이디 중복 확인 |
| `GET` | `/create` | 캡슐 수신자 선택 |
| `GET` | `/create-capsule` | 캡슐 작성 화면 |
| `POST` | `/capmaking/making_Capsule` | 캡슐 저장 |
| `GET` | `/capsule-storage` | 받은 캡슐 보관함 |
| `GET` | `/capdetail/detail_Capsule/<capsule_id>` | 공개된 캡슐 상세 조회 |
| `DELETE` | `/capdelete/delete_Capsule` | 캡슐 삭제 |
| `GET` | `/capmember/member` | 같은 커리큘럼·기수 구성원 조회 |
| `POST` | `/capquestion/making_QA` | 질문 등록 |

## 데이터베이스

애플리케이션은 `jungle-capsule` 데이터베이스에서 다음 컬렉션을 사용합니다.

- `Users`: 이름, 아이디, 비밀번호, 커리큘럼, 기수, 이메일
- `Capsule`: 발신자·수신자, 작성일·공개일, 제목·본문·링크·S3 객체 키, 공개 상태
- `Question`: 질문 내용과 작성일

`Question` 컬렉션이 비어 있으면 애플리케이션 시작 시 기본 질문 3개가 자동으로 등록됩니다.

## 개발 시 참고사항

- `.env`와 AWS 키, MongoDB 인증 정보는 저장소에 커밋하지 마세요.
- 현재 개발 서버는 `debug=True`로 실행됩니다. 운영 환경에서는 디버그 모드를 끄고 WSGI 서버를 사용하세요.
- 현재 회원 비밀번호는 애플리케이션 코드상 별도 해싱 없이 저장됩니다. 실제 서비스에 배포하기 전 비밀번호 해싱과 인증·권한 검증을 보강해야 합니다.
- 이미지가 없는 캡슐은 S3 설정 없이 생성할 수 있지만, 이미지 업로드·조회 기능에는 유효한 S3 설정이 필요합니다.

## 라이선스

`package.json`에 명시된 라이선스는 ISC입니다.
