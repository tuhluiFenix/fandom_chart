# http_status.py
import requests

STATUS_OK = requests.codes.ok
STATUS_FORBIDDEN = requests.codes.forbidden
STATUS_NOT_FOUND = requests.codes.not_found
STATUS_INTERNAL_ERROR = requests.codes.internal_server_error
STATUS_UNAVAILABLE = requests.codes.service_unavailable

STATUS_DESCRIPTIONS = {
    STATUS_OK: "Успешный запрос",
    STATUS_FORBIDDEN: "Доступ запрещен",
    STATUS_NOT_FOUND: "Фандом не найден"
}
