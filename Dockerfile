FROM python:3.13-slim

WORKDIR /app

# pyproject.toml, poetry.lock 복사
COPY pyproject.toml poetry.lock ./

# Poetry 설치
RUN pip install --no-cache-dir poetry

# Poetry가 별도 .venv를 안 만들도록 설정
RUN poetry config virtualenvs.create false

# 프로젝트 의존성 설치
RUN poetry install --no-dev

# 나머지 코드 복사
COPY . .

EXPOSE 8000

# uvicorn 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
