FROM gcr.io/dataflow-templates-base/python311-template-launcher-base

WORKDIR /template

COPY . .

RUN pip install --no-cache-dir -r dataflow/requirements.txt

RUN pip install .

ENV FLEX_TEMPLATE_PYTHON_PY_FILE="/template/dataflow/main.py"
ENV FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE="/template/dataflow/requirements.txt"

# IMPORTANT
ENV FLEX_TEMPLATE_PYTHON_SETUP_FILE="/template/setup.py"

ENV PYTHONPATH="/template"