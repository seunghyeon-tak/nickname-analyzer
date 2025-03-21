## 형태소 분석

### 가상환경 활성화

**macOS 기준**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 의존성 패키지 설치

```bash
pip install -r requirements.txt
```

### 의존성 패키지 관리
```bash
pip freeze > requirements.txt
```

### .env 파일 예문

```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=your_database
```


### python 파일 실행하기

```bash
python konlpy_test.py
```