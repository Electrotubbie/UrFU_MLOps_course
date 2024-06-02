# 3 практическая работа. Docker

- Создано небольшое web-приложение по детекции языка текста. 
Использована модель [papluca/xlm-roberta-base-language-detection](https://huggingface.co/papluca/xlm-roberta-base-language-detection)
- Для сборки образа создан Dockerfile.
- Образ запушен в репозиторий dockerhub 
[electrotubbie/wep-app-lang-classify](https://hub.docker.com/r/electrotubbie/wep-app-lang-classify).
- Также реализована docker-compose конфигурация, с помощью которой можно поднять 
докер-образ из репозитория с проброшенным на хост 8501 портом.
