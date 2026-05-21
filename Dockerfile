FROM python:3.12-slim
RUN mkdir /app
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
ENV export PIP_INDEX_URL=https://package-mirror.liara.ir/repository/pypi/simple 
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -i https://package-mirror.liara.ir/repository/pypi/simple --no-cache-dir -r requirements.txt
COPY ./core /app/
EXPOSE 8000