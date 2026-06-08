FROM apache/beam_python3.10_sdk:2.61.0

WORKDIR /template

COPY . .

RUN pip install -r requirements.txt

ENV FLEX_TEMPLATE_PYTHON_PY_FILE=/template/dataflow/main.py