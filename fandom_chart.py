import AO3
import plotly.express as px

fandoms = [
    'Detroit: Become Human (Video Game)',
    'One Piece',
    '天官赐福 - 墨香铜臭 | Tiān Guān Cì Fú - Mòxiāng Tóngxiù'
]

fandom_results = {}

for fandom in fandoms:
    try:
        search = AO3.Search(fandoms=fandom, crossovers=False)
        search.update()

        total_works = search.total_results
        fandom_results[fandom] = total_works

        print(f"Фандом '{fandom}': {total_works} работ")
    except Exception as errors:
        print(f"Ошибка при обработке фандома '{fandom}': {errors}")
        fandom_results[fandom] = 0

data = {
    'Fandom': list(fandom_results.keys()),
    'Count': list(fandom_results.values())
}

fig = px.pie(
    data,
    values='Count',
    names='Fandom',
    title='Количество работ по фандомам на AO3',
    hover_data=['Count'],
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
