# 3 практическая работа. Docker

- Создано небольшое web-приложение по детекции языка текста. 
Использована модель [papluca/xlm-roberta-base-language-detection](https://huggingface.co/papluca/xlm-roberta-base-language-detection)
- Для сборки образа создан Dockerfile.
- Образ запушен в репозиторий dockerhub 
[electrotubbie/web-app-lang-classify](https://hub.docker.com/r/electrotubbie/web-app-lang-classify).
- Также реализован docker-compose файл, с помощью которого можно поднять 
докер-образ из репозитория с проброшенным на хост 8501 портом.
