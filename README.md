# Python Print Examples — Quick Guide

이 저장소는 Python의 다양한 `print()` 사용법을 짧은 예제로 보여주고, VS Code/터미널/Jupyter에서 실행하는 방법만 간단히 정리합니다.

---

## 파일 목록

### 1) `main_print_v1.py`
- **설명**: 표준 `print()` 활용 종합 예제.
- **동작/기능**:
  - 기본 출력, 여러 값 출력(`sep`, `end`)
  - f-string, `format()`, `%` 포맷팅 비교
  - 이스케이프 문자, 여러 줄 문자열
  - 소수점 자리수, 정렬, 천 단위 콤마

### 2) `main_print_v2.py`
- **설명**: 함수와 반복문을 이용한 응용 예제.
- **동작/기능**:
  - 제목(header) 가운데 정렬 출력
  - 표 형태로 학생 목록과 평균 출력
  - `\r`, `flush=True`를 이용한 진행률 표시줄

### 3) `main_print_v1.ipynb`
- **설명**: `main_print_v1.py` 예제를 Jupyter Notebook 셀 단위로 나눈 버전.

### 4) `requirements.txt`
- Jupyter 실행에 필요한 패키지 목록 (`ipykernel`).

---

## 실행 방법

### 터미널 / VS Code
```bash
python main_print_v1.py
python main_print_v2.py
```

### Jupyter (VS Code)
```bash
python -m venv venv
.\venv\Scripts\activate        # Windows
pip install -r requirements.txt
```
`main_print_v1.ipynb`를 열고 커널로 `venv`를 선택한 뒤 셀을 실행합니다.
