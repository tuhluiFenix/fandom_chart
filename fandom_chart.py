import AO3
import plotly.express as px
import requests

# Получаем коды статусов из requests
STATUS_OK = requests.codes.ok  # 200
STATUS_FORBIDDEN = requests.codes.forbidden  # 403
STATUS_INTERNAL_ERROR = requests.codes.internal_server_error  # 500

AO3_BASE_URL = "https://archiveofourown.org/tags/"

fandoms = [
    'Detroit: Become Human (Video Game)',
    'One Piece',
    '天官赐福 - 墨香铜臭 | Tiān Guān Cì Fú - Mòxiāng Tóngxiù'
]

fandom_results = {}  # Словарь для фандомов
status_results = {}  # Словарь для статусов

for fandom in fandoms:
    try:
        search = AO3.Search(fandoms=fandom, crossovers=False)
        search.update()

        total_works = search.total_results
        fandom_results[fandom] = total_works
        status_results[fandom] = STATUS_OK  # Добавляем статус 200

        print(f"Фандом '{fandom}': {total_works} работ | Статус: {STATUS_OK}")
    except Exception as errors:
        fandom_results[fandom] = 0
        status_results[fandom] = STATUS_INTERNAL_ERROR  # Статус 500
        print(f"Ошибка при обработке фандома '{fandom}': {errors} | Статус: {STATUS_INTERNAL_ERROR}")

data = {
    'Fandom': list(fandom_results.keys()),
    'Count': list(fandom_results.values()),
    'Status': [str(status) for status in status_results.values()]  # Добавляем статусы в данные
}

fig = px.pie(
    data,
    values='Count',
    names='Fandom',
    title='Количество работ по фандомам на AO3',
    labels={'Count': 'Работ'},
    hole=0.3
)

fig.update_traces(
    textposition='inside',
    textinfo='percent+label',
    marker=dict(line=dict(color='#000000', width=1))
)

fig.update_layout(
    uniformtext_minsize=12,
    uniformtext_mode='hide'
)

fig.show()