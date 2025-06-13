# Quacklytics

Quacklytics는 DuckDB를 사용하여 데이터를 효율적으로 분석하는 프로젝트입니다. 이 저장소는 텍스트 데이터를 불러와 SQL로 처리하고, 빠르게 분석하는 과정을 제공합니다. 전혀 할 줄 모르는 상태에서 시작해 LLM과 함께 만들고 있습니다.

## 프로젝트 개요

-   **DuckDB**를 사용하여 대규모 데이터를 빠르게 처리
-   **Python**과 **Jupyter Notebook**을 통해 데이터 전처리 및 분석

## 설치 방법

1. 이 저장소를 클론합니다:

```bash
git clone https://github.com/esnahn/quacklytics.git
```

2. 프로젝트 디렉토리로 이동합니다:

```bash
cd quacklytics
```

3. 가상 환경을 생성하고 활성화합니다:

```bash
# 가상 환경 생성
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

4. 필요한 패키지를 설치합니다:

```bash
scoop install python iconv gawk
pip install -r requirements.txt
```
